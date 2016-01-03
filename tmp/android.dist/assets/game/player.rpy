# A Night At Ponyville - player.rpy
# Created by Therozin 2015
# My Little Pony: Friendship is Magic © and all its rights belongs to Hasbro, I don't claim any right about this franchise and this game is made by a fan for the fans.
# The images used in this game are from http://mlp-vectorclub.deviantart.com/gallery/ - Be sure to check the awesome work of those artists.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# TL;DR: You may use all the code of this project for you own purpose and/or please, as long as you don't claim any right on My Little Pony: Friendship is Magic © franchise, who belongs to Hasbro.
# Please give credits to the awesome artists who created the art of this game and do NOT remove this header.
# You can't use this project in commercial purposes. If you do, you might be sued.
#
# This game was created using Ren'Py.
# ===================================

init:
    
    #Player's Creation
    define player = DynamicCharacter("player_name", color = "#FFFFFF", show_two_window=True)

init python:
    
    #Player's informations
    player_gender = ""
    player_hometown = ""
    player_pronom = ""  # He or she
    player_reflective = ""  #Him or her
    player_possesive = ""  # His or her
    
    class AffinitiesManager(object):
        """
        Manages the affinities between the player and the characters.
        """

        def __init__(self):
            """
            Creates the Manager
            """
            
            #Has the player meet the caracters?
            self._applejack_met = False
            self._fluttershy_met = False
            self._pinkie_met = False
            self._rainbow_met = False
            self._rarity_met = False
            self._twilight_met = False
            self._spike_met = False
    
            # Initiatization of frienship'o'meters
            # It shouldn't be modified outside of the class.
            self.maximum_friendship = 300
            self._applejack_friendship = 150
            self._fluttershy_friendship = 150
            self._pinkie_friendship = 150
            self._rainbow_friendship = 150
            self._rarity_friendship = 150
            self._spike_friendship = 150
            self._twilight_friendship = 150

            # Initiatization of love'o'meters
            # Spike is not avalaible here. For obvious reasons.
            # It shouldn't be modified outside of the class.
            self.maximum_romance = 300
            self._applejack_romance = 100
            self._fluttershy_romance = 100
            self._pinkie_romance = 100
            self._rainbow_romance = 100
            self._rarity_romance = 100
            self._twilight_romance = 100

        @staticmethod
        def friendship_description(friendship_level):
            """
            Returns the message about the state of the relationship between the player and a character.
            """
            if friendship_level >= 280:
                friendship_description = "I have never been so close to anyone. Surely, this is my best friend."
            elif friendship_level >= 240:
                friendship_description = "Truly a good friend. I love to spend time with this pony."
            elif friendship_level >= 200:
                friendship_description = "A good friend of mine, I enjoy talking with this pony."
            elif friendship_level >= 175:
                friendship_description = "I like this pony, we share some center of interest. It could be a very good friend."
            elif friendship_level >= 140:
                friendship_description = "We barely know each other. I don't have a particular opinion on this pony."
            elif friendship_level >= 100:
                friendship_description = "I don't really like this pony. But I suppose we can get along just fine."
            elif friendship_level >= 60:
                friendship_description = "This pony is a pain. I can't stay with him in the same room."
            elif friendship_level >= 20:
                friendship_description = "How can you be so annoying? I'd rather be dead than talking with this pony."
            else:
                friendship_description = "This pony is a royal pain. The only thought of this pony disgust me."

            return friendship_description
    
        @staticmethod
        def romance_description(romance_level):
            """
            Returns the message about the state of the romance relationship between the player and a character.
            """
            if romance_level >= 280:
                romance_description = "She is definitively the one. I have never loved someone so much."
            elif romance_level >= 240:
                romance_description = "I am in love with this pony. She is perfect."
            elif romance_level >= 200:
                romance_description = "There is something very special between us... I can feel it."
            elif romance_level >= 160:
                romance_description = "I am often thinking about her."
            elif romance_level >= 120:
                romance_description = "I like this pony. I'm feeling well when she is around."
            elif romance_level >= 80:
                romance_description = "I don't have any particular interest in her."
            elif romance_level >= 40:
                romance_description = "I am not interested in this mare."
            elif romance_level >= 20:
                romance_description = "Having a relationship with this pony? Are you kidding me?"
            else:
                romance_description = "I'd rather marry Discord himself than having a relationship with this pony."
            
            return romance_description
           
        
        #APPLEJACK'S METHODS
        @property
        def applejack_met(self):
            """
            Tells if Applejack has been met or not.
            """
            return self._applejack_met
            
        @applejack_met.setter
        def applejack_met(self, has_been_met):
            """
            Change the state about the acquaintance with Applejack.
            """
            self._applejack_met = has_been_met
        
        @property
        def applejack_friendship(self):
            """
            Return Applejack's friendship value.
            """
            return self._applejack_friendship

        @applejack_friendship.setter
        def applejack_friendship(self, value):
            """
            Add the new value of applejack_friendship.
            """
            if value > 0:
                self._applejack_friendship = min(self._applejack_friendship + value, self.maximum_friendship)
            else:
                self._applejack_friendship = max(self._applejack_friendship + value, 0)

        @property
        def applejack_romance(self):
            """
            Return Applejack's romance value.
            """
            return self._applejack_romance

        @applejack_romance.setter
        def applejack_romance(self, value):
            """
            Add the new value of applejack_romance.
            """
            if value > 0:
                self._applejack_romance = min(self._applejack_romance + value, self.maximum_romance)
            else:
                self._applejack_romance = max(self._applejack_romance + value, 0)

        #FLUTTERSHY'S METHODS     
        @property
        def fluttershy_met(self):
            """
            Tells if Fluttershy has been met or not.
            """
            return self._fluttershy_met
            
        @fluttershy_met.setter
        def fluttershy_met(self, has_been_met):
            """
            Change the state about the acquaintance with Fluttershy.
            """
            self._fluttershy_met = has_been_met
            
        @property
        def fluttershy_friendship(self):
            """
            Return Fluttershy's friendship value.
            """
            return self._fluttershy_friendship

        @fluttershy_friendship.setter
        def fluttershy_friendship(self, value):
            """
            Add the new value of fluttershy_friendship.
            """
            if value > 0:
                self._fluttershy_friendship = min(self._fluttershy_friendship + value, self.maximum_friendship)
            else:
                self._fluttershy_friendship = max(self._fluttershy_friendship + value, 0)

        @property
        def fluttershy_romance(self):
            """
            Return Fluttershy's romance value.
            """
            return self._fluttershy_romance

        @fluttershy_romance.setter
        def fluttershy_romance(self, value):
            """
            Add the new value of fluttershy_romance.
            """
            if value > 0:
                self._fluttershy_romance = min(self._fluttershy_romance + value, self.maximum_romance)
            else:
                self._fluttershy_romance = max(self._fluttershy_romance + value, 0)

        #PINKIE'S METHODS
        @property
        def pinkie_met(self):
            """
            Tells if Pinkie Pie has been met or not.
            """
            return self._pinkie_met
            
        @pinkie_met.setter
        def pinkie_met(self, has_been_met):
            """
            Change the state about the acquaintance with Pinkie Pie.
            """
            self._pinkie_met = has_been_met
            
        @property
        def pinkie_friendship(self):
            """
            Return Pinkie's friendship value.
            """
            return self._pinkie_friendship

        @pinkie_friendship.setter
        def pinkie_friendship(self, value):
            """
            Add the new value of pinkie_friendship.
            """
            if value > 0:
                self._pinkie_friendship = min(self._pinkie_friendship + value, self.maximum_friendship)
            else:
                self._pinkie_friendship = max(self._pinkie_friendship + value, 0)

        @property
        def pinkie_romance(self):
            """
            Return Pinkie's romance value.
            """
            return self._pinkie_romance

        @pinkie_romance.setter
        def pinkie_romance(self, value):
            """
            Add the new value of pinkie_romance.
            """
            if value > 0:
                self._pinkie_romance = min(self._pinkie_romance + value, self.maximum_romance)
            else:
                self._pinkie_romance= max(self._pinkie_romance + value, 0)

        #RAINBOW'S METHODS
        @property
        def rainbow_met(self):
            """
            Tells if Rainbow Dash has been met or not.
            """
            return self._rainbow_met
            
        @rainbow_met.setter
        def rainbow_met(self, has_been_met):
            """
            Change the state about the acquaintance with Rainbow Dash.
            """
            self._rainbow_met = has_been_met
            
        @property
        def rainbow_friendship(self):
            """
            Return Rainbow's friendship value.
            """
            return self._rainbow_friendship

        @rainbow_friendship.setter
        def rainbow_friendship(self, value):
            """
            Add the new value of rainbow_friendship.
            """
            if value > 0:
                self._rainbow_friendship = min(self._rainbow_friendship + value, self.maximum_friendship)
            else:
                self._rainbow_friendship = max(self._rainbow_friendship + value, 0)

        @property
        def rainbow_romance(self):
            """
            Return Rainbow's romance value.
            """
            return self._rainbow_romance

        @rainbow_romance.setter
        def rainbow_romance(self, value):
            """
            Add the new value of rainbow_romance.
            """
            if value > 0:
                self._rainbow_romance = min(self._rainbow_romance + value, self.maximum_romance)
            else:
                self._rainbow_romance = max(self._rainbow_romance + value, 0)

        #RARITY'S METHODS
        @property
        def rarity_met(self):
            """
            Tells if Rarity has been met or not.
            """
            return self._rarity_met
            
        @rarity_met.setter
        def rarity_met(self, has_been_met):
            """
            Change the state about the acquaintance with Rarity.
            """
            self._rarity_met = has_been_met
            
        @property
        def rarity_friendship(self):
            """
            Return Rarity's friendship value.
            """
            return self._rarity_friendship

        @rarity_friendship.setter
        def rarity_friendship(self, value):
            """
            Add the new value of rarity_friendship.
            """
            if value > 0:
                self._rarity_friendship = min(self._rarity_friendship + value, self.maximum_friendship)
            else:
                self._rarity_friendship = max(self._rarity_friendship + value, 0)

        @property
        def rarity_romance(self):
            """
            Return Rarity's romance value.
            """
            return self._rarity_romance

        @rarity_romance.setter
        def rarity_romance(self, value):
            """
            Add the new value of rarity_romance.
            """
            if value > 0:
                self._rarity_romance = min(self._rarity_romance + value, self.maximum_romance)
            else:
                self._rarity_romance = max(self._rarity_romance + value, 0)

        #TWILIGHT'S METHODS
        @property
        def twilight_met(self):
            """
            Tells if Twilight Sparkle has been met or not.
            """
            return self._twilight_met
            
        @twilight_met.setter
        def twilight_met(self, has_been_met):
            """
            Change the state about the acquaintance with Twilight Sparkle.
            """
            self._twilight_met = has_been_met
            
        @property
        def twilight_friendship(self):
            """
            Return Twilight's friendship value.
            """
            return self._twilight_friendship

        @twilight_friendship.setter
        def twilight_friendship(self, value):
            """
            Add the new value of twilight_friendship.
            """
            if value > 0:
                self._twilight_friendship = min(self._twilight_friendship + value, self.maximum_friendship)
            else:
                self._twilight_friendship = max(self._twilight_friendship + value, 0)

        @property
        def twilight_romance(self):
            """
            Return Twilight's romance value.
            """
            return self._twilight_romance

        @twilight_romance.setter
        def twilight_romance(self, value):
            """
            Add the new value of twilight_romance.
            """
            if value > 0:
                self._twilight_romance = min(self._twilight_romance + value, self.maximum_romance)
            else:
                self._twilight_romance = max(self._twilight_romance + value, 0)

        #SPIKE'S METHODS
        @property
        def spike_met(self):
            """
            Tells if Spike has been met or not.
            """
            return self._spike_met
            
        @spike_met.setter
        def spike_met(self, has_been_met):
            """
            Change the state about the acquaintance with Spike.
            """
            self._spike_met = has_been_met
            
        @property
        def spike_friendship(self):
            """
            Return Spike's friendship value.
            """
            return self._spike_friendship

        @spike_friendship.setter
        def spike_friendship(self, value):
            """
            Add the new value of spike_friendship.
            """
            if value > 0:
                self._spike_friendship = min(self._spike_friendship + value, self.maximum_friendship)
            else:
                self._spike_friendship = max(self._spike_friendship + value, 0)