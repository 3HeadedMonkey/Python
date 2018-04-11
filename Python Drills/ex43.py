from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print('This scene is yey incomplete')
        print('Subclass it and implement enter().')


class Engine(object):

    def __init__(self, scene_map):
        # klasyczne przemianowanie na self.
        self.scene_map = scene_map

    def play(self):
        # current scene to scene map przemielone przez opening scene
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


        current_scene.enter()

class Death(Scene):

    quips = [
        "You died 1",
        "You died 2",
        "You died 3",
        "You died 4",
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""Central Corridor room, enter 'YES' to win, 'NO' to lose and anything else to repeat"""))

        action = input(">  ")

        if action == "YES":
            print("You pass the trial, young padawan")
            return 'laser_weapon_armory'
        elif action == "NO":
            print("You have failed the trail, you die, mortal!")
            return 'death'

        else:
            print ("DOES NOT COMPUTE, MR IRISHMAN")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        Now we have entered the chapter 2 of the story
        that I am simplifying greatly
        the task is to enter a double digit number that is made from numbers 1 and 2 (Yes, I' simplifying the stuff to the max)
        or to enter 00 to pass, else you die. There are 10 tries so that should be enough"""))
        # the code is a string made up from a set of 2 random numbers
        code =f"{randint(1,2)}{randint(1,2)}"
        guess = input("[KEYPAD]>")
        guesses = 0

        while guess != code and guesses < 10:
            print(" NOT THIS TIME YOUNG LAD")
            guesses += 1
            guess = input("[KEYPAD]> ")

        if guess == code:
            print(dedent("""
            The code is correct! Bravado
            you sly slythering slyther
            new room awaits!
            """
            ))
            return 'the_bridge'
        else:
            print(dedent("""
            something somethin you die something
            we erace the tripple ""/" with a dedent()
            have a nice have a nice have a nice day
            LOOOSER
            """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        Now we are at the brigde
        maybe there is another game going on
        just enter whatever the value to get futher
        """))
        whatever_value = input(">   ")
        return "escape_pod"

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            Escape_pod, \n\n\tnothing interesting as I dow't want to continue on
            playing games
                They bore me. Maybe I sould play with making a hangman, but I really hate the idea of those study drills
                I mean, a base of funciton for starts would be nicer
                Unless waisting time is what we're playing there


        """))
        togo = input("ANYTHING>  ")
        return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        YAS = input("< ")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
