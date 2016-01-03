# A Night At Ponyville - narrative_data.rpy
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
# ==================================

init python:
    
    
    # Variables of ending
    ending = False
    ending_name = ""
    
    # Variables for the subchapter "character_creation" in prologue
    character_creation = True
    
    # Variables for the subchapter "on_the_way_to_the_castle" in prologue
    applejack_presentation = False
    fluttershy_presentation = False
    pinkie_presentation = False
    rainbow_presentation = False
    rarity_presentation = False
    twilight_presentation = False
    mane_six_presentation = True
    
    # Variables for the subchapter "meeting_the_mane_six" in chapter 1
    dinner_meet_applejack = False
    dinner_meet_fluttershy = False
    dinner_meet_pinkie = False
    dinner_meet_rainbow = False
    dinner_meet_rarity = False
    dinner_meet_twilight = False
    dinner_meet_spike = False
    
    dinner_meet_twilight_first = False
    joke = 0 #If you told a joke to pinkie