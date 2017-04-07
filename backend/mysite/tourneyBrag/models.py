from django.db import models
import uuid

#If you make changes, make sure to do makemigrations and then migrate.
#If you add another table, add it to the admin.py so admins can see the table

class Player(models.Model):
	playerName = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=30)
	gamePlayed = models.CharField(max_length=50)
	mainCharacter = models.CharField(max_length=30)
	playerID = models.CharField(max_length=15, primary_key=True)

	def __str__(self):
		return str(self.playerID) + ", " + self.playerName + ", " + self.password + ", " + self.gamePlayed + ", " + self.mainCharacter


class Organizer(models.Model):
	organizerID = models.CharField(primary_key=True, max_length=30)
	organizerName = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	
class Administrator(models.Model):
	adminID = models.CharField(primary_key=True, max_length=30)
	admin_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	
class Tournament(models.Model):
	organizerOwner = models.CharField(max_length=30)
	organizerOwnerID = models.ForeignKey('Organizer', on_delete=models.DO_NOTHING, related_name= '+')
	tournamentTitle = models.CharField(max_length=30, unique= True, primary_key=True)
	date_created = models.DateTimeField('date_created')
	date_start = models.DateTimeField('start date')

	#def __str__(self):
	#	return self.organizerOwner + ", " + str(self.organizerOwnerID) + ", " + self.tournamentTitle + ", " + self.date_created + ", " + self.date_start


class Fan(models.Model):
	user_Fan = models.CharField(max_length=30) #user_fan is a fan of user_idol
	user_Idol = models.CharField(max_length=30)
	idolID = models.ForeignKey('Player', on_delete=models.DO_NOTHING,related_name= '+')

class Voucher(models.Model):
	user_voucher = models.CharField(max_length=30) #user_voucher vouches for user_receiver
	user_receiver = models.CharField(max_length=30)
	receiverID = models.ForeignKey('Organizer', on_delete=models.DO_NOTHING,related_name= '+')


class Entrant(models.Model):
	player_entrant = models.CharField(max_length=30)
	tournament_entered = models.ForeignKey('Tournament', on_delete=models.DO_NOTHING,related_name= '+')
	has_been_accepted = models.BooleanField()

class Record(models.Model):
	tournament_name = models.ForeignKey('Tournament',on_delete=models.CASCADE,related_name= '+')
	player_winner = models.CharField(max_length=30)
	player_loser = models.CharField(max_length=30)

class Banned(models.Model):
	adminID = models.ForeignKey('Administrator', on_delete=models.DO_NOTHING,related_name= '+')
	bannedUser = models.CharField(max_length=30)


class Match(models.Model):
    matchID = models.IntegerField(primary_key=True, unique=True)
    tournamentName = models.ForeignKey('Tournament', on_delete=models.DO_NOTHING, related_name= '+')
    playerWinner = models.CharField(max_length=30)
    playerLoser = models.CharField(max_length=30)

class Comment(models.Model):
	#comment_ID = models.CharField(primary_key=True, max_length=15)
	author_name = models.CharField(max_length=30)
	receiver_name = models.CharField(max_length=30)
	actual_comment = models.CharField(max_length=150)
	#date_created = models.DateField(auto_now_add=True, default="2017-01-01")