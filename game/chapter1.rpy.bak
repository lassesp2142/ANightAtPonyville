# A Night At Ponyville - chapter1.rpy
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

label meeting_the_mane_six:
    
    scene bg friendship_castle_main_hallway with Dissolve(1.5)
    
    "As huge as the castle is looking from the outside, it was nothing compared to the inside. The crystal walls were echoing as I walked in, followed by Twilight. The Princess showed up next to me."
    
    show twilight neutral_right at left_position with moveinleft
    
    twilight "Follow me, I think Spike and the others are in the dinning room."
    player "How many rooms is there in this castle?"
    twilight "Enough to lose yourself inside. When I told you it was really huge, I wasn't lying."
    
    hide twilight with quickdissolve
    
    "The alicorn continues in the corridors as I was walking behind her."
    
    # Inside the dinning room
    scene bg friendship_castle_dining_room with Dissolve(1.5)
    
    "Twilight entered inside a large room, which seems to be the dining room. When we got inside, six heads turned around to look at us. I quickly recognized those legendaries faces: Applejack, Pinkie Pie, Rainbow Dash, Rarity, Fluttershy and Spike. I felt a little bit overwhelmed by this extraordinary crowd. The orange earth pony walked in our direction."
    
    show twilight neutral_right at left_position with quickdissolve
    
    twilight "Good evening every pony! Sorry for being late, the meeting at the city hall lasted longer than expected."
    
    show applejack smiling_left at right_position with moveinright
    play music applejack_theme
    $ affinities.applejack_met = True
    
    applejack "Howdy Twilight! How are ya? And who is this %(player_gender)s? Ah don't think Ah know %(player_reflective)s."
    
    twilight "This is %(player_name)s, %(player_pronom)s will be with us tonight. You see, %(player_name)s has just arrived in town and knows nopony. I figured we could have an extra guest tonight."

    show applejack happy with quickdissolve
    
    applejack "Well, welcome in Ponyville sugarcube. Ah'm Applejack, nice to meet ya!"
    player "Nice to meet you too, Applejack."
    applejack "It's not every day that new ponies move in Ponyville, ya know? What is bringin' ya in our little town?"
    player "Actually, nothing in particular. I've just moved here because it's a small and quiet place. I'm from %(player_hometown)s, but I've always wanted to live in a more peaceful place."
    
    show applejack neutral_right with quickdissolve
    
    if player_hometown == "Manehattan":
        applejack "Manehattan? Ah lived a few weeks there when Ah was a filly. Ah can' say Ah miss this big town. Sweet Apple Acres is everythin' an Apple like me needs. Livin' with your friends and your family is the most important for me."
        
    else:
        applejack "Ah can't say I'd like to live in a big city either. Ponyville may not be the best city in Equestria, but it has everythin' I can ask for. Livin' with your friends and your family is the most important for me."
    
    player "I am sure that you ..."
    
    # Pinkie appears
    show twilight surprised_left
    show applejack surprised_right
    
    pinkie "THERE IS A NEW PONY IN TOWN AND NOPONY WARNED ME ?!"
    
    hide twilight with moveoutleft
    hide applejack with moveoutright
    show pinkie intrusive with quickdissolve 
    with vpunch
    play music pinkie_theme
    $ affinities.pinkie_met = True

    "A pink ouragan stormed through the room and crashed on me."
    
    pinkie "Hello there! I'm Pinkie Pie! What's your name? Oh oh oh! Don't tell me! Is it Starry Sky? Or Sunny Cloud? Aqua Balloon? Maybe Sky Walker? Or Atmosphere? Oh! Do you like parties? I'm sure you do! Every pony likes parties! I know, I do love parties and..."
    "I looked at the pony without understanding what was going on. As far as I could say, it was Pinkie and she was as energetic as she was told to be. She was talkative... Very talkative, my brain had difficulties to process everything she was saying."
    
    show pinkie neutral with quickdissolve

    pinkie "... And that is how I called it Cherry Chonga! I'll cook some of them soon, and you'll take one! I'm sure you'll love it because..."
    
    show pinkie smiling_left with vqdissolve
    show pinkie:
            linear .5 xalign .9 
    show twilight angry at left_position with moveinleft
    
    twilight "Pinkie! Stop! Let %(player_reflective)s breath!"
    
    show twilight suspicious_right with quickdissolve
    
    twilight "Are you alright %(player_name)s?"
    
    menu:
        "{i}I... I guess.{/i}":
            player "I guess... I wasn't expecting that..."
            twilight "Please excuse Pinkie, she is often excited when she meets a new pony. This time, she has been easy on you."
            pinkie "Excuse me, I might have been a tiny little bit carried away. Sorry!"
            
        "{i}What are you, crazy ?!":
            $ affinities.pinkie_friendship = 1
            player "Are completely crazy Pinkie Pie? You could have broken my neck!"
            
            show pinkie concerned_left with quickdissolve
            
            pinkie "I'm sorry, I didn't want to..."
            player "Next time, try to not jump on me!"
            twilight "Calm down, it's nothing... "
            player "It was nothing? Have you seen how she... You know what? Forget it."
            
        "Burst in laught":
            $ affinities.pinkie_friendship = 2
            "{i}I burst in laugh as I got up, Pinkie imitated me under the curious eye of Twilight{/i}"
            player "Now that's what I call a welcome! Nice to meet you Pinkie Pie!"
            
            show twilight happy_right with quickdissolve
            
            twilight "Well, I suppose you are alright."
            player "Of course I am!"
            pinkie "Oh! I almost forgot! Your welcome song! Ahem... No wait... I can't sing, there is only writing text in a visual novel!"
            
            show twilight suspicious_right with quickdissolve
            
            twilight "Visual Novel? What are you talking about?"
            pinkie "Well! I guess I'll find an other way to sing!"
            player "Uhm... I don't get what she is saying either..."
    
    twilight "I don't when to overwhelm you, %(player_name)s. Maybe you should meet my friends one by one. You should have the time to meet three of them before dinner."
    player "It is maybe a better idea..."
    
    show pinkie neutral with quickdissolve
    
    pinkie "I can't wait to talk with you! Come and talk to me when you want!"
    
    hide pinkie with moveoutright
    
    twilight "Sorry about that..."
    player "Don't worry, it could have been worse. Besides, Pinkie is the element of Laughter, that's not surprising... I suppose."
    
    show twilight neutral_right with vqdissolve

    menu:
        twilight "Who would you like to see first?"
        
        # Applejack's Path
        "{i}Applejack seems really sympathic.{/i}":
            player "Applejack seems really sympathic, plus we have been cut in our discussion by Pinkie. I think I should talk to her first."
            twilight "Of course. She is right over here, I think she'll be happy to talk with you."
            $ dinner_meet_applejack = True
            call applejack_first_talk from _call_applejack_first_talk
            
        # Fluttershy's Path TODO
        "{i}I'm going to take a break after Pinkie... Let's talk with Fluttershy.{/i}":
            player "After this pink storm, I think I'm going to take a calmer one. Fluttershy is known for the kindness, isn't she? I think I'm going to talk to her."
            show twilight suspicious_right with quickdissolve
            twilight "Sounds good to me. Just, be sure to not be too... sharp with her. She can feel unseasy very quickly..."
            $ dinner_meet_fluttershy = True
            
        # Pinkie's Path TODO
        "{i}Well... Maybe I'm crazy, but I can't make Pinkie Pie wait.{/i}":
            player "Well... Maybe I'm crazy, but I can't make Pinkie Pie wait. She seems to be very excited to meet me."
            show twilight happy_right with quickdissolve
            twilight "You are a though %(player_gender)s to return inside the Pinkie's Storm so quickly! Good luck then. Don't hesitate to cut her if she doesn't stop talking. She is very talkative when she meets somepony for the first time."
            $ dinner_meet_pinkie = True
        
        # Rainbow's Path TODO
        "{i}I'd really like to meet Rainbow Dash.{/i}":
            player "I'd really like to meet Rainbow Dash. I'm sure she is as awesome as she is said to be!"
            twilight "She sure has a very good reputation! She is overthere, I'm sure you'll get along just fine!"
            $ dinner_meet_rainbow = True

        # Rarity's Path TODO
        "{i}Maybe I should introduce myself to Rarity.{/i}":
            player "Maybe I should introduce myself to Rarity, I've read some magazines about her and I'd like to talk with her."
            twilight "Rarity is really sweet and kind, I'm pretty sure she will like you. She is right there."
            $ dinner_meet_rarity = True
            
        # Twilight's Path TODO
        "{i}What about you, Twilight?{/i}":
            $ affinities.twilight_romance = 2
            $ affinities.twilight_friendship = 2
            player "What about you, Twilight? Coud we talk a little bit more?"
            show twilight blushing_right with quickdissolve
            twilight "Me...? Well, if you want, but... You don't want to meet the others?"
            player "We have the whole evening, so a few more minutes with you won't hurt anypony."
            twilight "Of course... Come with me, we should take a chair."
            player "Princesses first."
            "{i}The alicorn blushed a little before making her way to the table."
            $ dinner_meet_twilight = True
            $ dinner_meet_twilight_first = True
            call twilight_first_talk
            
        # Spike's Path TODO
        "{i}What about Spike? I've always wanted to meet a dragon!{/i}":
            player "What about Spike? I've always wanted to meet a dragon!"
            show twilight happy_right with quickdissolve
            twilight "Well, this is your lucky day. Spike is one of the only dragon that lives amongst ponies. Besides, I'm sure we will be that somepony take interest in him. He is just there."
            $ dinner_meet_spike = True
    
    $ dinner_ponies_met = 1
    
    while dinner_ponies_met < 3:
        stop music
        scene bg friendship_castle_dining_room with fade
        
        menu:
            player "{i}I wonder who I should talk with now...{/i}"
            
            "{i}Let's talk with Applejack{/i}" if not dinner_meet_applejack:
                $ dinner_meet_applejack = True
                call applejack_first_talk
            
            "{i}Let's talk with Fluttershy.{/i}" if not dinner_meet_fluttershy:
                $ dinner_meet_fluttershy = True
                pass
                
            "{i}Let's talk with Pinkie Pie.{/i}" if not dinner_meet_pinkie:
                $ dinner_meet_pinkie = True
                pass
                
            "{i}Let's talk with Rainbow Dash.{/i}" if not dinner_meet_rainbow:
                $ dinner_meet_rainbow = True
                pass 
                
            "{i}Let's talk with Rarity.{/i}" if not dinner_meet_rarity:
                $ dinner_meet_rarity = True
                pass
                
            "{i}Let's talk with Twilight.{/i}" if not dinner_meet_twilight:
                $ dinner_meet_twilight = True
                call twilight_first_talk
                pass
            
            "{i}Let's talk with Spike.{/i}" if not dinner_meet_spike:
                $ dinner_meet_spike = True
                pass
                
        $ dinner_ponies_met += 1
    return
    
    
label applejack_first_talk:
    #APPLEJACK'S PATH
    
    scene bg friendship_castle_dining_room with fade
    play music applejack_theme
    
    "I saw Applejack leaning against a wall, looking at me with a wide smile. I smiled in return and came next to her."

    show applejack confident_right with quickdissolve
    
    applejack "So, what do ya think of Pinkie?"
    player "... Energetic, I guess?"
    applejack "Pinkie's really somethin'. Don't worry, ya'll get use to it. She is really kind when ya know her."
    player "I'm sure she is."
    
    show applejack neutral_right with quickdissolve
    
    applejack "Come on sugarcube, ya can't blame Pinkie for been friendly. She is just, ya know, very expressive."
    player "She caught me off guard, but I guess she was genuine. I don't hold it against her."
    applejack "That's the spirit! So tell me %(player_name)s, ya told me about you; maybe ya want to ask me questions?"

    menu:
        "Ask about the life in the farm.":
            player "How is the life in a farm?"
            
            show applejack smiling_right with quickdissolve
            
            applejack "Well, the life is quite calm at Sweet Apple Acres. Besides the apple buckin' and runnin' the sales, there's not an awful lot of thinfs to do."
            player "You are only growing apples?"
            applejack "Not exactly, but mainly. We've got loads of crops, like carrots or Zapp'Apples."
            player "Zapp'Apples?"
            
            show applejack neutral_right with quickdissolve
            
            applejack "Ya don't know what Zapp'Apples are? This is a very special kind of apple that could only be in the Everfree Forest. Granny Smith had found some seeds years ago, and since then we are cultivatin' Zapp'Apples at the farm."
            applejack "And ya're in luck, sugarcube, it is almost the season. I'll be sure to keep some of them for ya."
            
            menu:
                "{i}That's very nice from you.{/i}":
                    $ affinities.applejack_friendship = 1
                    player "That's very kind of you, Applejack. I'm sure I'll love it!"
                    
                    show applejack smiling_right with quickdissolve
                    
                    applejack "Ah bet ya will! Ah'll eat mah hat if ya don't!"
                    player "Just to be sure, you should save some jam to eat you hat with. I'm not sure it tastes very good."
                    applejack "Ah'll keep that in mind. But it won't happen, sugarcube."
                    

                "{i}Maybe I could help you harvesting the Zapp'Apples.{/i}":
                    $ affinities.applejack_friendship = 2
                    player "Maybe I could lend a hoof to help you bucking those apples."
                    
                    show applejack smiling_right with quickdissolve
            
                    applejack "We don't usually ned help, but thanks you kindly %(player_name)s. Ah'll ask you if we need ya."
                    player "I'll be my pleasure."
                    
                
                "{i}From the Everfree Forest? Are you crazy?{/i}":
                    $ affinities.applejack_friendship = 1
                    player "From the Everfree Forest? Is your family crazy or what? Who is stupid enough to harvest something from the Everfree?"
                    
                    show applejack angry_right with quickdissolve

                    applejack "Ah don't like the tone with which ya are talking about mah family. Without the Zapp'Apples, Ponyville wouldn't be here today."
                    
                    menu:
                        "{i}Likely story.{/i}":
                            $ affinities.applejack_friendship = 2
                            player "Likely story. You're not a very good liar, Element of Honesty."
                            applejack "Well, Ah think ya should leave before Ah say something Ah could regret."
                            player "See you later, farm girl."
                            
                            "I left Applejack with a small smirk. I didn't think she liked me, but neither did I."
                            return
                        "Apologize.":
                            player "That's not what I meant, sorry. This is just that the Everfree is really dangerous."
                            applejack "Yes, it is. But Granny Smith did the right thing. Our family was starvin', she sought for a solution."
                            player "I reckon I may have been a little harsh..."
                            
                            show applejack neutral_right with quickdissolve
                            
                            applejack "Well, no hard feelin' sugarcube. Next time you should just watch your tong. Ah've to talk with Twilight, I'll see you later."
                            player "See you later Applejack."
                            "The orange pony smiled quickly before walking towards Twilight."
                            
                            return
                            
            show applejack neutral_right with quickdissolve
            
            applejack "Even if the Zapp'Apples season begins in only three weeks, ya could come to the farm when ya want."
            player "Why?"
            applejack "It's always nice to have friends around, don't ya think?"
            player "You consider me as a friend?"
            
            show applejack confident_right with quickdissolve
            
            applejack "Why wouldn't Ah? Twilight's friends are mah friends. And Ah like ya. In general, city ponies don't like ponies from the countryside."
            player "I doubt I could not like you. I mean, Twilight don't even know me and she is offering me to have a dinner tonight with all of you."
            applejack "I would have do the same. Say, ya haven't told me how ya meet Twilight."
            player "Long story short, I lost my key and my house was locked."

            show applejack smiling_right with quickdissolve
            
            menu:
                "{i}Applejack laughed slighty when I explained her."
        
                "{i}What is so funny?{/i}":
                    player "What is so funny?"
                    applejack "Sorry sugarcube, but that's really bad luck. I mean, ya just move and ya lost your key. I hope you'll find it."
                    player "Yes... Very funny."
                    
                    show applejack neutral_right with quickdissolve
                    
                    applejack "Oh come on. I didn't meant to hurt you sugarcube."
                    player "None taken."
                    applejack "Perfect. Ah have to leave you. Twilight and Ah need to talk about the dinner. See ya later."
                    
                    "Applejack quickly tipped her hat and left."

                "She has a lovely laught...":
                    $ affinities.applejack_romance = 2
                    player "You are cute when you laughed."
                    
                    show applejack puzzled_right with vqdissolve
                    
                    applejack "What... What was that?"
                    player "I just say you are cute when you laught."
                    
                    show applejack blushing_right with quickdissolve
                    
                    applejack "Uhm... Ahw shucks... Thank you..."
                    "She quickly cleared her throat and looked away."
                    applejack "Ah... Ah have to talk with Twilight. Sorry, Ah'll see ya later."
                    player "I hope."
                    
                    "She hid her blush a little under her hat before leaving me alone."
                
                "Laught with her.":
                    $ affinities.applejack_friendship = 1
                    player "That's sure, I'm not very lucky this time."
                    applejack "Well, next time something good will happen to ya! Luck and missfortune balance each other over time."
                    player "An old yet true proverb."
                    applejack "Exactly! Well, Ah have to talk with Twilight sugarcube. I'll see ya later."
                    "The farm pony quickly winked at me with a smile and left."
                    
                
        "Ask about her.":
            player "Well, talk me about you. For example, where do you live?"
            applejack "Ah live at Sweet Apple Acres, the farm on the outskirts of Ponyville. Ah am with mah little sister Applebloom, mah big brother Big Macintosh and mah grandma Granny Smith."
            player "So the farm is a family business?"
            applejack "It has always been, sugarcube. That's how the Apple Family works, always in family."
            player "And what about you? What is your role in this?"
            
            show applejack happy with quickdissolve
            
            applejack "Well, Ah am usually buckin' the apples and takin' care of all the chores."
            
            menu:
                "{i}All by yourself? That's impressive...{/i}":
                    $ affinities.applejack_friendship = 1
                    player "Wow Applejack, that's really impressive. I don't think I could run a farm on my own."
                    applejack "Ah am not alone sugarcube, but thanks. Without Big Mac, it won't be that easy. He's a pony of few words, but he's a really hardwork pony."
                    player "It must run in the family."
                    
                    show applejack confident_right with quickdissolve
                    
                    applejack "Granny Smith always says hard work is the best policy of life."
                    player "A wise pony."
                    applejack "Exactly. Ah'm doin' mah best to live with her values and pass them to anypony who would want to."
                    "She softly laughed"
                    
                    menu:
                        "{i}You are really something, Applejack.{/i}":
                            $ affinities.applejack_friendship = 2
                            player "You are really something Applejack. Truly, I admire you."
                            applejack "Thanks you kindly %(player_name)s, but ya should give Granny Smith all the credits. She is the one who raised me."
                            player "I hope I'll meet her someday. She has made a wonderful work."
                            
                            show applejack happy with quickdissolve
                            
                            player "She sure has. Well, sugarcube, Ah'm sorry but Ah have to talk with Twilight. I'll see you later."
                            "The farm pony quickly winked at me with a smile and left."
                        "She has a lovely laught...":
                            $ affinities.applejack_romance = 2
                            player "You are cute when you laughed."
                            
                            show applejack puzzled_right with vqdissolve
                            
                            applejack "What... What was that?"
                            player "I just say you are cute when you laught."
                            
                            show applejack blushing_right with quickdissolve
                            
                            applejack "Uhm... Ahw shucks... Thank you..."
                            "She quickly cleared her throat and looked away."
                            applejack "Ah... Ah have to talk with Twilight. Sorry, Ah'll see ya later."
                            player "I hope."
                            
                            "She hid her blush a little under her hat before leaving me alone."
                            
                    
                "{i}That's not bad for an earth pony.{/i}":
                    $ affinities.applejack_friendship = 2
                    player "That's not bad for an earth pony."
                    
                    show applejack angry_right with quickdissolve
                    
                    applejack "What do ya mean by \"That's not bad for an earth pony\"?"
                    player "Well, I meant what I meant. Earth ponies are hardworkers and all, but come on."
                    applejack "Ya think ya're do better then me?"
                    player "Without a doubt."
                    applejack "Ah don't like braggin', but Ah am surely stronger than ya. Even Rainbow has difficulties to compete with me."
                    player "But I'm not Rainbow Dash, farm girl."
                    applejack "Y'all urban ponies think ya are better because ya live in fancy places. Ya should leave me, Ah don't like where our conversation is goin'. Wouldn't want to hurt ya, pegasus."
                    "Applejack left me alone with a angry glance."
                    
            
        "Ask about her family and the foundation of Ponyville." if applejack_presentation:
            player"Twilight told me it was your family that founded Ponyville decades ago. How has it happened?"
            
            show applejack happy with quickdissolve
            
            applejack "Have ya talk with Twilight about me? There's not a lot a ponies who want to know about Ponyville's foundation. Well, Ah can tell you the story, Ah'll tell you the short version."
            player "Take your time, I'm listening."
            
            show applejack smiling_right with quickdissolve
            
            applejack "When Granny Smith was just a filly, she and her family were pilgrims who collected seeds and sold them to live. Princess Celestia herself gave them some lands near the Everfree Forest."
            
            show applejack neutral_right with quickdissolve
            
            applejack "They planted their first orchad, but it wasn't growing at all. Granny Smith ventured inside the Everfree to find food. She found some stranges seeds and collected them."
            applejack "It was Zapp'Apples seeds. Soon, they begun to make Zapp'Apple jam, and it was so delicious that some ponies begun to come around."
            applejack "Soon, a nice little town appeared, and Ponyville was born. And ever since then, we are makin' Zapp'Apple jam every year."
            player "What a wonderful story..."
            applejack "Ah know, right? What da ya think about that?"
            
            menu:
                "{i}I think I have lost five minutes of my life listening to it.{/i}":
                    $ affinities.applejack_friendship = 2
                    player "I think I have lost five minutes of my life listening to your story. I should not have ask for it, that was a waste of time."
                    
                    show applejack angry_right with quickdissolve
                    
                    applejack "Well, next time Ah won't tell ya the story ya are askin' for either."
                    player "Good to know, farm girl."
                    applejack "Ah have to talk with Twilight. See ya."
                    "Applejack groaned loudly before leaving. What a rude pony."
        
                "{i}I really loved it.{/i}":
                    $ affinities.applejack_friendship = 4
                    player "I loved it, it reminds me the epic stories of the past. Cities have often great stories behind their foundation."
                    
                    show applejack confident_right with quickdissolve
                    
                    applejack "Exactly, and Ah'm really happy to continu the Zapp'Apple jam tradition. Ya will come to the farm to taste it, will ya?"
                    player "I'd love to. This story has made me quite curious about a jam which can gather so much ponies!"
                    applejack "Well, be sure Ah'll keep the first jar for ya this year."
                    player "Wow Applejack, thank you!"
                    
                    show applejack happy with quickdissolve
                    
                    applejack "That will be mah welcome gift %(player_name)s, Ah'm happy to give it to you!"
                    player "We'll eat it together!"
                    applejack "Of course sugarcube. Ah'm sorry, but Ah have to leave you. Ah have to talk with Twilight. See ya later."
                    "The farm pony quickly winked at me with a smile and left."
    return
    
    
label twilight_first_talk:
    # TWILIGHT'S PATH
    
    scene bg friendship_castle_dining_room with fade
    play music twilight_theme
    
    if dinner_meet_twilight_first:  # Only activated if Twilight is the first pony the player talk to.
        "The princess drew two chairs and offered one to me. I took it and sat down next to her. She cleared her throat and her blush had disappeared."
        
        show twilight suspicious_left at right_position with moveinright

        twilight "So... Uhm... %(player_name)s, why do you want to talk with me first? I mean, there's a lot of interesting ponies with us tonight..."
        
        menu:
            "{i}That's not your business.{/i}":
                $ affinities.twilight_friendship = -3
                $ affinities.twilight_romance = -3
                player "I don't have to justificate myself. That is not your business."
                
                show twilight confused with quickdissolve
                
                twilight "Okay... That's a way to begin a conversation..."
                
            "{i}I'm too shy to talk with the others...{/i}":
                player "I guess I'm too shy to talk with the others..."
                
                show twilight happy_left with quickdissolve
                
                twilight "Is that all? You shouldn't be afraid, they are all very sympathic. No one is going to bite you."
                player "I know but... The first impression is often the most important and... I don't want to mess up already."
                twilight "Don't worry, we can spend some time together if you don't feel to talk with the girls now."
                
            "{i}Because I just want to spend time with you, Twilight.{/i}":
                player "I guess I just want to spend some time with you so we can get to know each other."
                
                show twilight embarrassed_left with quickdissolve
                
                twilight "I see... I usually don't draw the intention on me..."
                player "Really? I would have thought the contrary. You seem very interesting actually."
                
                show twilight blushing_embarrassed_left with quickdissolve
                
                "Twilight blushed and looked at the ground as she cleared her throat. {i}Maybe I should talk about something else... {/i}"
                
    else:
        "Twilight was near the table, putting some cakes on it. She saw me coming and smiled genuinely."
        
        show twilight neutral_left at right_position with quickdissolve
        
        twilight "So, how is it going so far?"
        player "Well I guess. Your friends are very sympathic."
        twilight "I told you so! Come on, take a chair, we can a little if you want to."
        "She drew a chair for me and invited me to sit down with a quick smile."
        
    menu:
        "Leave her alone.":
            pass
        "Ask about her friends.":
            pass
        "Ask about the time she organized Winter Wrap Up" if twilight_presentation:
            pass
    
    return
    