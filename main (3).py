'''Implement a class called player that represents a cricket player.The player class should have a
method called play() which prints "The players is playing cricket. Derive a two classes,Batsman and
Bowler, From the player class.override the play() method in each derived class to print "The batsman
is batting" and "The blower is blowing",respectively. write a program to create subjects or both the 
Batsman and Bowler classes and call tha play() method for each object.'''


# Define the base class player
class player:

  def play(self):
    print("The player is playing cricket.")


# Define the derived class Batsman
class Batsman(player):

  def play(self):
    print("The batsman is batting.")


# Define the derived class Bowler
class Bowler(player):

  def play(self):
    print("The bowler is bowling.")


# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()
