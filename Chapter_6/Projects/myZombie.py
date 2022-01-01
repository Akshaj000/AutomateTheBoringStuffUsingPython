#incomplete
import zombiedice
import random
import sys

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombierandom:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults is not None:
            choice = random.randint(0,1)
            if choice==1:
                diceRollResults = zombiedice.roll()
            else:
                break


class Twobrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        brains=0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains >= 2:
                break
            else:
                diceRollResults = zombiedice.roll()
            
class Twoshotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotgun=0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun >= 2:
                break
            else:
                diceRollResults = zombiedice.roll()

class Decideonetofour:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotgun=0
        i=0
        chance = random.randint(0,3)
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            i+=1
            if(i<=chance):
                if shotgun>=2:
                    break
                else:
                    diceRollResults = zombiedice.roll()
            else:
                break

class Stopatshotgunsgbrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotgun=0
        brains=0
        chance = random.randint(0,3)
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if(shotgun>=brains):
                break
            else:
                diceRollResults = zombiedice.roll()



zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    MyZombierandom(name='Randombot'),
    Twobrains(name="Twobrainbot"),
    Twoshotguns(name="Twogunbot"),
    Decideonetofour(name="decide1tofour"),
    Stopatshotgunsgbrains(name="Stopshotgun>brains")

    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)