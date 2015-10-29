# A Night At Ponyville - script.rpy
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

init python:
    
    # Various important variables used in the game.
    show_relationship_screen = False

    
# The game starts here.
label start:
    
    show screen relationship_button # Shows the button of relationship on everyscreen.
    
    # Chapter 0: Welcome in Ponyville
    call character_creation from _call_character_creation  # Found in "prologue.rpy"
    $ show_relationship_screen = True
    call welcome_in_ponyville from _call_welcome_in_ponyville  # Found in "prologue.rpy" 
    
    if (ending == True and ending_name == "ending_1_leave_me_alone"):
        call ending_1_leave_me_alone from _call_ending_1_leave_me_alone
        jump end
        
        
    call on_the_way_to_the_castle from _call_on_the_way_to_the_castle  # Found in "prologue.rpy"
    call the_friendship_castle from _call_the_friendship_castle  # Found in "prologue.rpy"
    
    
    # Chapter 1: My first friends.
    
    call meeting_the_mane_six from _call_meeting_the_mane_six
    
    scene black with Dissolve(1.5)
    "{b}TO BE CONTINUED ... {/b}"
    jump end
    

label end:
    
    return
