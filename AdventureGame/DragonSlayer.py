from AdventureGame.utils.GameEngine import GameEngine
from AdventureGame.game_files.locations.Location import Location
from AdventureGame.game_files.actions.Action import Action
from AdventureGame.game_files.actions.Move import Move
from AdventureGame.game_files.actions.BattleAction import BattleAction
from AdventureGame.game_files.actions.Win import Win

game_engine = GameEngine()


class DragonSlayer:
    def __init__(self):
        self.game = game_engine

    def generate_game_rooms(self):
        ## Starting branch. Walk down alley and become a heroic knight. Go back to your room and become maybe a dragon.

        # First room
        start_room: Location = Location(description="""It is a cold, dark night. You have been working a long, hard day. 
        Each step you take, you can feel your legs ache and your head throb. Training to be a knight is 
        tough work.\n As you walk down the street you can hear loud voices echoing from an alleyway. You 
        pause and listen for a moment. Suddenly you feel a chill run down your spine. An ungodly sound arises, 
        followed by a bellowing roar.""")

        # Alley way to find dragon
        alley_way: Location = Location(description="You walk down the alleyway, taking each step slowly.")

        fair_maiden: Location = Location(description="""
        As you get closer to the source of the noises, you begin to be able to identify the sources better. The screams
        are in fact screams for help, coming from what sounds like a damsel in distress. This barely registers though, as the source
        of the roars becomes very apparent. A massive dragon's head is visible over the building and he's pissed. Roars echo
        through your very bones, causing you to stumble.
        """)

        help_maiden: Action = BattleAction(chance_to_win=0, win_action=None, win_message="",
                                           lose_message="""You turn your back to the dragon, reaching your hand out to help the 
                woman to her feet. Your eyes lock on with hers, bringing you into a hypnosis. The dragon then reaches down and
                gobbles you up. Yummy.""")

        save_fair_maiden: Location = Location(description="""
        You rush into the scene, sword drawn. You almost faint at the sight of the absolutely beautiful woman cowering in the corner, 
        but the adrenaline from facing down the monsterous dragon is enough to keep you on your feet.
        """)

        win_kill_dragon: Location = Location(description="""You have triumped versus the evil that invaded your town.
        You become a renowned knight dubbed 'Dragon Slayer'. You Win!""")

        stab_woman: Action = BattleAction(chance_to_win=.7, win_action=Move(new_location=win_kill_dragon),
                                          win_message="""You see the evil flash in the woman's eye. After a moment of
                                          brief hesitation, you swing your sword at her, striking her down. Her body
                                          instantly transforms into a hideous monster before disolving into the air.""",
                                          lose_message="""You lean forward, hesitating before you stab the most beautiful woman you
                                           have ever seen. Then the woman's beautiful face begins to melt away, revealing 
                                           a hideous monster. She jumps on you and
                                          ruthlessly kills you.""")

        trust_woman: Action = BattleAction(chance_to_win=0, win_action=None, win_message="",
                                           lose_message="""You lean forward, looking to gain a reward for your valient deed. The woman's 
                                          beautiful face begins to melt away, revealing a hideous monster. She jumps on you and
                                          ruthlessly kills you.""")

        dragon_defeated: Location = Location(description="""
        The dragon is dazed for a moment as he stumbles and falls to the ground. You leap victoriously on his dead body
        before noticing the woman who had been having a stand off with the dragon. She is breathing heavily and gives you a
        big smile.""")

        attack_dragon_stab: Action = BattleAction(chance_to_win=.4, win_action=Move(dragon_defeated),
                                                  lose_message="""The dragon swings his tail in anticipation to attack the
                                                  madien. While doing so he impales you with his spiked tail.""",
                                                  win_message="""You lunge into the dragon's belly, thrusting savagely.
                                                  The sword sinks into him, causing him to let out a ruthless roar.""")

        attack_dragon_climb: Action = BattleAction(chance_to_win=.6, win_action=Move(dragon_defeated),
                                                   lose_message="""The dragon swings his tail in anticipation to attack the
                                                   madien. While doing so he impales you with his spiked tail.""",
                                                   win_message="""You lunge onto the dragon's back and run along it's length:
                                                   he doesn't seem to feel you on his scales. You jump onto his head thrusting down savagely.
                                                   The sword sinks into him, causing him to let out a ruthless roar."""
                                                   )
        attack_dragon: Location = Location(description="""
        You creep around the corner and see the dragon's attention is focused on the lady. You sneak behind the dragon...
        """)

        # To Home
        to_home: Location = Location(description="""As you continue down the cobblestones back home, the loud noises begin to give
        way to silence. The scream fades, as does the feroucious roaring. It's as if the silence gets stronger
        with each step. The heavy feeling in your chest, instead of fading as you escape the awful scene,
        intensifies.""")

        pathetic_dragon: Action = BattleAction(chance_to_win=0, win_action=None, win_message="",
                                               lose_message="""The moment your choice is made 
                                               you hear a voice ring through your head.
                                               'You are a dragon. You are strong. Proud!
                                               Yet you cower in fear and block out your true potential.
                                               You will suffer the consequences.' A pillar of fire 
                                               drops from the sky incinerating you and all around you.""")

        become_dragon_win: Action = Win(win_message="""You continue to beat down the lesser beings.
        You grow incomprehensibly strong with each kill. You are the nightmare story mothers
        whisper to their children and, when they do, they call you 'Slayer'.""")

        grow_stronger: Location = Location(description="""You feel yourself grow with power. You know you will soon be unstoppable.
        Such a powerful beast could do so much!""")

        kill_guards: Action = BattleAction(chance_to_win=.8, win_action=Move(new_location=grow_stronger),
                                           win_message="""You leap on each guard as they arrive, tearing them apart with 
                                           your razor sharp claws. You feel yourself burn with power as you defeat each enemy.""",
                                           lose_message="""Your clumsy new limbs struggle to react and the guards cut you down.""")

        baby_dragon: Location = Location(description="""The first thing you feel is pain. The throbbing in your head is 
        excructiating. You begin to roll over to stand, but something red catches your eye - a claw. You quickly jump
        back in a panic, remembering the crazy night before. As you move though, you realize the claw is your own! You look
        down and see you have a small dragon body. Attempting to scream in panic, you let out a roar. Immediately you hear
        panicked voices and people shouting nearby.""")

        home: Location = Location(description="""Finally, you reach your front door. Images of the terrifying
        wizard that were bombarding your mind disappear at last. Joy rushes over you
        as you step across the threshold. Safety at last! Relief overwhelms you. 
        Then you collapse onto your face, 
        blacking out in your entryway.""")

        fight_wizard: Action = BattleAction(chance_to_win=.5, win_action=Move(home),
                                            win_message="""
                                            There are a flurry of fireballs that suddenly blast towards you.
                                            You narrowly dodge, feeling your eyebrows singe as you duck. You quickly race 
                                            toward the wizard. You can feel an immense presence of fear and dispair envelop you,
                                            but your push through and lunge at the wizard, driving your sword into his chest.
                                            The wizard evaporates into a dark cloud that floats above his body, growing larger and
                                            pulsing with power. Suddenly, it launches towards you, clouding your face and you can feel it
                                            force its way down your nostrils and throat. You would scream, but the pain is too agonizing.
                                            It stops after what seems like an eternity and you sprint toward home as fast as your legs carry you.
                                            """,
                                            lose_message="""
                                            The wizard launches an array of magic missles at you, vaporizing you instantly.
                                            """)
        wizard_interaction: Location = Location(description="""A wizard appears. Instantly you know where the feelings of dread 
        originated. Dark clouds billow out from him. His face is shrowded by a cloak, but you are thankful because
        even just his glowing eyes are enough to make you pee a little.""")
        wizard_interaction.add_action(description="There is no other option. Fight!", action=fight_wizard)

        # Link rooms to adjacent rooms and provide prompts
        start_room.adjacent_locations = {
            "Follow the noises down the alleyway": alley_way,
            "Walk as quickly as possible back home": to_home
        }
        # Become Dragon Locations
        to_home.adjacent_locations = {
            "Rush home.": wizard_interaction,
            "Return to the alleyway entrance.": start_room
        }
        baby_dragon.add_action(description="Metalic footsteps promise the arrival of guards. Stand and fight!",
                               action=kill_guards)
        baby_dragon.add_action(description="Better get away before they kill you!", action=pathetic_dragon)

        grow_stronger.add_action(
            "You see your potential! You will soon rule the world, starting with this pathetic town.",
            action=become_dragon_win)

        # Fight Dragon Locations
        alley_way.adjacent_locations = {
            "Return to the road.": start_room,
            "Swallow your fear. Move onward.": fair_maiden
        }
        save_fair_maiden.adjacent_locations = {
            "Turn to help the maiden": help_maiden
        }
        save_fair_maiden.add_action("Ram your sword into the dragon's dumb skull.", attack_dragon_stab)
        fair_maiden.adjacent_locations = {
            "The lady needs me! Rush to her rescue.": save_fair_maiden,
            "This is my chance to prove myself! Sneak up on the stupid lizard.": attack_dragon
        }
        attack_dragon.add_action("As you move behind his back, you notice his underside is free of scales. Stab him!",
                                 attack_dragon_stab, )
        attack_dragon.add_action("You see a glistening spot on the top of the dragon's head. Let's ride this critter!",
                                 attack_dragon_climb)
        dragon_defeated.add_action("Her charm is too much. You smile back at her.", trust_woman)
        dragon_defeated.add_action("You are not fooled by her. Attack!", stab_woman)
        home.add_action("You feel conciousness returning. Get up!", Move(baby_dragon))
        home.add_action("You don't have enough energy. Go back to sleep", pathetic_dragon)

        # Return a list of all rooms fully constructed.
        return start_room

    def start(self):
        room = self.generate_game_rooms()
        self.game.start(room)


DragonSlayer().start()
