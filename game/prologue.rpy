# A Night At Ponyville - prologue.rpy
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

label character_creation:
    
    play music ponyville_day_theme
    
    scene bg ponyville_city with Dissolve(1.5)
    
    "Ponyville.\nA small yet picturesque village near the Everfree Forest. Well known for its cider, its wonderful landscapes, its proximity with Canterlot and for being the hometown of the Princess of Frienship."
    "This town was very important for a lot of ponies. Some stories have begun in Ponyville and some have finished here. As for me, I was going to write my very own story in Ponyville."
    
    # Player's identity is defined below this line
    while character_creation:
        
        "I am a pegasus who had just moved in Ponyville and..."
        
        menu:
            "I am a mare.":
                $ player_gender = "mare"
                $ player_pronom = "she"
                $ player_possesive = "her"
                $ player_reflective = "her"
                
            "I am a stallion.":
                $ player_gender = "stallion"
                $ player_pronom = "he"
                $ player_possesive= "his"
                $ player_reflective = "him"
                
        $ player_name = renpy.input("My name is... {color=#f00}Please enter your name.{/color}") 
        
        if player_name == "":
            if player_gender == "mare":
                $ player_name = "Silver Night"
            else:
                $ player_name = "Golden Sky"    
                
        menu:
            "I used to live in..."
            
            "Cloudsdale.":
                "I used to live in Cloudsdale, the city in the sky."
                $ player_hometown = "Cloudsdale"
                
            "Manehattan.":
                "I used to live in Manehattan, the great metropolis near the Celestial Sea in the East."
                $ player_hometown = "Manehattan"
            
            "Los Pegasus.":
                "I used to live in Los Pegasus, in the Western part of Equestria near the South Luna Ocean."
                $ player_hometown = "Los Pegasus"
                
        "My name is %(player_name)s, I am a %(player_gender)s and I used to live in %(player_hometown)s. Is that correct?"
        
        menu:
            "Yes... This is me.":
                $ character_creation = False
            "No... I've made a mistake.":
                pass
    # End of the player's identity creation
    
    $ affinities = AffinitiesManager()  # Creation of the Affinities Manager, used throught all the game.
    
    "Why did I choose to live in such a small town? Yes, %(player_hometown)s had everything a young pegasus like me could ask for. I had plenty of friends, I had graduate from a prestigious university. But something was missing in my life."
    "When you have grown in a big city as %(player_hometown)s, you are often dreaming of living in the middle of the nature. On the other hoof, you don't want to leave the urban comfort behind you. Ponyville was the perfect mix between city and countryside."
    
    return
    
    
label welcome_in_ponyville:
    
    scene bg ponyville_riverside_city with Dissolve(1.5)
    
    "After a few weeks of search, I had found a lovely house near a lake in Ponyville. Some of my friends of %(player_hometown)s helped me to move in. After three days of going back and forth between Ponyville and %(player_hometown)s to bring my belongings, it was finally the day."
    "Everything was ready to start my new life. I had a new home, I had a mind full of ideas and dreams. I was ready to live the life I always wanted. But... There was one small problem."
    "I had lost the key of my house."
    "Where was it? I had no idea. I searched it for hours, looked for it all around Ponyville without success. Now, I was just sitting in front of the door of house, locked outside and looking at the setting sun. The night was almost here. The real estate agency should have duplicate keys, but it was closed now."
    "I had been sitting in front of my door for ten minutes now, grumbleling at my misfortune, when a voice took me out of my thoughts."
    
    
    show twilight suspicious_right with quickdissolve
    play music twilight_theme
    $ affinities.twilight_met = True
    
    twilight "Hello, is everything alright?"
    "I froze when I raised my head. I quickly recognized Twilight Sparkle, the Princess of Friendship. Being surprised by her, I..."  
    
    menu:        
        "I immediately bowed in front of the Princess.":
            $ affinities.twilight_friendship = 2
            
            player "Your highness, it is a privilege to have an opportunity to meet you."
            
            show twilight neutral_right with quickdissolve
            
            "She laughed as I raised my head. She shook her face and smiled."
            twilight "You are a very polite %(player_gender)s. There is no need to bow!"
            player "This is the tradition when you meet a Princess, isn't it?"
            twilight "Maybe, but I am not sure this does apply to me. Anyway, what is your problem? I saw you grumbling in front of this door."
            player "Let's say I have locked myself up outside and I have lost my key..."
            
            
        "I explained her what was going on.":
            $ affinities.twilight_friendship = 1
            
            player "Good evening Princess Twilight. Long story short, I have lost the key of my home and I can't open the door..."
            
            show twilight neutral_right with quickdissolve
            
            twilight "I see... That's why you were grumbling in front of your door."
            player "And I have no idea of how I can open it or enter in the house."
            
        "As if she cared. I just didn't answer.":
            player "..."
            twilight "Uhm... Hello, it there someone at home...?"
            
            menu:
                "{i}Why won't she let me alone?{/i}":
                    player "Can you leave me alone? I don't want to talk to anyone. Princesses included."
                    
                    show twilight confused with quickdissolve
                    
                    twilight "Oh... Uhm... Well. Of course..."
                    
                    hide twilight with quickdissolve
                    
                    "I looked at the alicorn as she was walking away. I wasn't in the mood to talk to any pony."
                    
                    $ ending = True
                    $ ending_name = "ending_1_leave_me_alone"
                    return
                    
                "{i}Maybe she is genuine... I should explain her.{/i}":
                    player "Sorry, you caught me off guard, Princess Twilight. I wasn't expecting that somepony would care about my problem."
                    
                    show twilight neutral_right with quickdissolve
                    
                    twilight "It's okay, I understand. So, what is the matter?"
                    player "Long story short, I have lost the key of my home and I'm locked outside..."
                    

    show twilight thoughtful_right with quickdissolve
    
    twilight "I see... This is not fun at all... Just a question, are you new in town? I have never seen you before."
    player "Yes, I have just moved in and I was supposed to spend my first night in Ponyville in this very house. But I think it might be a little complicated."
    twilight "And there is nopony who can help you?"
    player "I don't have any friend in town actually. I am from %(player_hometown)s."
    twilight "And Ponyville is not exactly next to it..."
    player "I know there is an other key at the real agency estate but it is already closed."
    
    show twilight neutral_right with quickdissolve
    
    "The alicorn put her hoof down and smiled quickly before turning her head in my direction."
    twilight "What is your name?"
    player "Uhm... %(player_name)s, I'm %(player_name)s."
    twilight "Well %(player_name)s, nice to meet you! I can help you in a way."
    player "Can you?"
    
    show twilight happy_right with quickdissolve
    
    twilight "Yes. You told me you didn't know any pony in town and you haven't a clue of how you can enter inside your house. I am having a dinner with my friends tonight at my castle and I am already late. Would you like to come with me?"
    player "I... This is very kind of you Princess, but I don't want to disturb..."
    twilight "Would you rather spend the evening alone? Plus, you would meet my friends and get to know some of the ponies of this town. Come on, I assure you they will be very happy to meet you, especially Pinkie Pie!"
    player "In that case... I'd be happy to spend the evening with you and your friends, Princess Twilight."
    twilight "Please, call me Twilight. I don't really like when ponies call me by this title."
    
    return
    
label on_the_way_to_the_castle:
    
    scene bg outside_ponyville with Dissolve(1.5)
    
    "I followed the Princess through Ponyville, where she was waving back to some ponies, smiling at others. It was as if she knew every single person of this town. Eventually, she turned her head in my direction."
    
    show twilight neutral_right with quickdissolve
    
    twilight "So tell me %(player_name)s, maybe you want me to talk about the ponies you will meet tonight?"
    player "You mean, your friends?"
    twilight "Yes. You might have heard about them."
    player "Who don't know them? You all have made so much for Equestria!"
    twilight "Well, we just happened to be in the right place at the right moment."
    
    show twilight happy_right with quickdissolve
    
    while(mane_six_presentation and not(applejack_presentation and fluttershy_presentation and pinkie_presentation and rainbow_presentation and rarity_presentation and twilight_presentation)):
        menu:
            twilight "Who would you like to heard about?"
    
            # APPLEJACK PRESENTATION
            "Ask about Applejack" if not applejack_presentation:
                $ applejack_presentation = True
                
                player "Uhm... Talk me about Applejack please."
                
                show twilight happy_right with quickdissolve
                
                twilight "Well, Applejack is the former bearer of Honesty. She is the most reliable pony I know, always willing to lend a hoof. She is hardworking and lives at Sweet Apple Acres."
                player "I know this place! They are making the best cider of all of Equestria!"
                twilight "Yes, it's even better when you can drink it just after its fabrication."
                player "Is Applejack working alone in the farm?"
                
                show twilight neutral_right with quickdissolve
                
                twilight "No, she and her brother Big Macintosh are in charge of the harvest. Her little sister Applebloom and her grandmother Granny Smith are also working in the farm in their own way."
                player "It is a sort of family business."
                twilight "It's true. Just for the record, it is the Apple Family who founded Ponyville decaces ago."
                player "Really? They must be the most important family of the town."
                twilight "And also the most helpful one."
                
            # FLUTTERSHY PRESENTATION
            "Ask about Fluttershy" if not fluttershy_presentation:
                $ fluttershy_presentation = True
                
                player "Who is Fluttershy?"
                
                show twilight neutral_right with quickdissolve
                
                twilight "She is the former bearer of Kindness, and she is very kind as you might expect. She is also very shy, but once you get to know her, she is a very nice person. Of course, I can't talk about her without talking about her love for animals."
                player "I suppose she have a pet."
                twilight "More than one actually. Her house is a true nature sanctuary! There are all kinds of animals: mices, rabbits, bears..."
                player "Bears?!"
                twilight "She is really gifted when it comes to take care of animals. She can even talk with them."
                player "You must be kidding me... It was true..."
                
                show twilight thoughtful_right with quickdissolve
                
                twilight "I have never understand how she can do that, it must be linked with her cutie mark... It's a very rare abitily."
                
            # PINKIE PIE PRESENTATION
            "Ask about Pinkie Pie" if not pinkie_presentation:
                $ pinkie_presentation = True
                
                player "Is Pinkie Pie as energetic as she is told to be?"
                
                show twilight happy_right with quickdissolve
                
                twilight "If you needed to find an embodiment of energy, Pinkie would be the perfect pony. She is really, really full of joie de vivre and enthusiasm. She was the bearer of Laughter."
                player "Some ponies say she is weird."
                
                show twilight thoughtful_right with quickdissolve
                
                twilight "Well... I can't say she is not. There are things about her I can't explain even with magic and sciences. For example, she has a \"Pinkie sense\" that warns her about the future."
                
                show twilight neutral_right with quickdissolve
            
                twilight "But this is the funniest part about Pinkie. I have learnt with her to not question everything and accept some facts as they are."
                player "I'm really looking forward to see her. She must be very interesting!"
            
            # RAINBOW DASH PRESENTATION
            "Ask about Rainbow Dash" if not rainbow_presentation:
                $ rainbow_presentation = True
                
                player "What about Rainbow Dash?"
                
                show twilight neutral_right with quickdissolve
                
                twilight "Rainbow was the bearer of Loyalty. She is the best flyer in Ponyville and she a very athletic pony. She is always up for a challenge. Since you are a pegasus, maybe you could try to race her."
                player "I don't know if I stand a chance against her... She is not exactly known for being slow."
                
                show twilight happy_right with quickdissolve
                
                twilight "She could teach you a lot of things about flying, I often take lessons with her. But I must confess, I haven't met a lot of ponies who could beat her."
                player "Do you think I could?"
                twilight "You look in shape, maybe you are a very good racer?"
                player "Well... I'm an average pegasus..."
                twilight "Don't worry, with some training, I'm sure you could make wonders!"
                
            # RARITY PRESENTATION
            "Ask about Rarity" if not rarity_presentation: #TO DO
                $ rarity_presentation = True
                
                player "Is there anything to know about Rarity?"
                
                show twilight neutral_right with quickdissolve
                
                twilight "Well, if I had to sum up her quickly, I'd say she is a fashionista with a golden heart. She was the bearer of Generosity and she has not usurped this element of Harmony."
                player "I've read in some journals about her dresses, they are really impressive."
                
                show twilight happy_right with quickdissolve
                
                twilight "Rarity is dedicated to her work. She is always creating wonderful designs indeed."
                player "I was friend with a mare back in %(player_hometown)s who loved Rarity's work."
                twilight "Really? You should tell her about that, I'm sure she will be happy to know about that!"
                
                
            # TWILIGHT PRESENTATION
            "Ask about her" if not twilight_presentation:
                $ twilight_presentation = True
                $ affinities.twilight_friendship = 1
                $ affinities.twilight_romance = 1
                
                player "How about you, Princ... How about you, Twilight?"
                
                show twilight blushing_right with quickdissolve
                
                twilight "Me...? Uhm... What do you mean?"
                player "Well, you asked if there was somepony I'd like to heard about. I'd like to hear about you actually."
                twilight "Oh... Uhm... Okay... What can I say...?"
                player "It looks like you know every pony in town."
                
                show twilight neutral_right with quickdissolve
                
                twilight "I have been living here for two years now, and Ponyville isn't a very big city. In fact, I'm usually in charge of the planning of the big events in town, like Winter Wrap up, so I have to know every pony"
                player "Are you planning everything on your own?"
                twilight "Usually yes, and I love when everything happens according to the plan."
                player "That's quite impressive. I was sometimes helping my mom to organize the family meetings back in %(player_hometown)s. It wasn't as big as your tasks though."

                show twilight happy_right with quickdissolve
                
                twilight "Party planner, uh? I'm sure you'll get along with Pinkie. Besides, I didn't begin my plannings with the Summer Sun Celebration. Every pony has to begin somewhere."
                
            # STOP PRESENTATIONS
            "I don't have anything to ask.":
                $ mane_six_presentation = False
                
                player "I think it will be enough Princess. I really want to meet them by myself."
                
                show twilight neutral_right with quickdissolve
                
                twilight "Of course, we are almost at the castle anyway."
        
    return
    
    
label the_friendship_castle:
    
    scene bg friendship_castle_dusk with Dissolve(1.5)

    "I didn't pay attention, but we got closer to the castle as we were talking."
    "I stopped when I saw the gigantic crystal tree in the setting sun. The refraction of the sunbeams were making it looking oniric, as if it was a creation of Princess Luna herself. It was just..."
    
    show twilight suspicious_right at left_position with quickdissolve
    
    twilight "It everything alright?"
    
    menu:
        "Her castle is simply outstanding...":
            $ affinities.twilight_friendship = 1
            player "Your castle... It is... Wonderful."
            
            show twilight very_happy_right with quickdissolve #Mirror
            
            "The Princess laughed a little and looked at me with a smile."
            twilight "You know %(player_name)s, I'm glad that you find it beautiful. There're ponies who think it is ruining the landscapes around Ponyville..."
            player "They surely not have seen it at dusk. It is one of the most astonishing building I have ever seen."
            twilight "There is something special about this castle... You know, when I had to move in, I wasn't feeling very well in it..."
            
            show twilight thoughtful_right with quickdissolve #Mirror
            
            twilight "Those giant, empty and cold rooms... It was kinda sad. I was even feeling lonely, especially if Spike wasn't around."
            
            show twilight happy_right with quickdissolve
            
            twilight "But then my friends have redecorated it. It was feeling home at last..."
            player "I think I'm going to understand it, as I'm going to have my own house for the first time..."
            twilight "Don't worry, you'll get use to it. Besides, you won't be alone. I'm sure you'll meet a lot of ponies here."
            
        "Her castle is just horrible.":
            $ affinities.twilight_friendship = 1
            
            player "What is this monstruosity...? It looks like a fool's drawing..."
            
            show twilight confused with quickdissolve
            
            twilight "Uhm... This \"monstruosity\" is my castle..."
            player "Seriously? How can you live in such a place? I mean, it was as if it was put here in the sole purpose of ruining the landscapes..."
            twilight "... I like the way it is. But I suppose it is a matter of taste..."
            
            "{i}Well, in this case, she has quite stranges tastes...{i}"
            
    show twilight neutral_right with quickdissolve
        
    twilight "Anyway. We should really go inside. My friends are waiting for me." 
    
    if affinities.twilight_friendship >= 152:
        twilight "I can't wait to introduce you to my friends!"
        player "You.. You are?"
        
        show twilight happy_right with quickdissolve
        
        twilight "Yes, you seems to be really kind. I'm sure we'll get along very well!"
        
        "I couldn't help to blush a little at the compliment."
        
    "She opened the door of the castle with a smile and showed me the hallway with her forehoof, slighty bowing in my direction."
    
    twilight "Please do come in, %(player_gender)ss first!"
    
    stop music
    
    return