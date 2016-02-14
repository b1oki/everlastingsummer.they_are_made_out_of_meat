init -1000 python:
    translation["meat"] = {}
    translation["meat"]["english"] = "They're made out of meat"
    translation["meat"][None] = u"Они сделаны из мяса"
    
init:
    $ mods["meat"] = translation["meat"][_preferences.language]
    #$ mod_tags["meat"] = ["gameplay:vn","length:day","protagonist:male","character:Unknow"]

label meat:
    $ night_time()
    $ persistent.sprite_time = "night"
    scene black with dissolve
    pause(1)
    if _preferences.language == None:
        menu:
            "Летняя версия":
                jump meat_new
            "Космическая версия":
                jump meat_old
    else:
        menu:
            "Summer version":
                jump meat_new
            "Space version":
                jump meat_old
    return

label meat_old:
    image bg cosmos_1 = "meat/cosmos_1.jpg"
    image bg cosmos_2 = "meat/cosmos_2.jpg"
    image bg cosmos_3 = "meat/cosmos_3.jpg"
    image bg cosmos_4 = "meat/cosmos_4.jpg"
    image bg cosmos_5 = "meat/cosmos_5.jpg"
    image ufo_1 = "meat/ufo_1.png"
    image ufo_2 = "meat/ufo_2.png"
    pause(1)
    if _preferences.language == None:
        jump meat_old_ru
    else:
        jump meat_old_en
    return

label meat_old_ru:
    $ uf = Character(u'Незнакомец', color="#6a5acd")
    $ ub = Character(u'Незнакомец', color="#f4a460")
    scene bg cosmos_1 with fade
    play music "meat/Aural_Night_Magellan.mp3"
    uf "Они мясные."
    uf "Они сделаны из мяса."
    show ufo_1 at left with moveinleft
    with dspr
    ub "Из мяса?"
    uf "Из мяса. Они сделаны из мяса."
    ub "Мяса?"
    show ufo_2 at right with moveinright
    with dspr
    uf "В этом не может быть сомнений. Мы отобрали нескольких представителей из разных мест планеты, доставили их на борт нашей лаборатории и исследовали их до мельчайших подробностей."
    uf "Они полностью мясные."
    ub "Это невозможно! А как же радиосигналы? Послания к звёздам?"
    uf "Они используют радиоволны для общения, но сигналы исходят не от них, а от машин."
    ub "Так кто сделал машины? Вот с кем нам надо найти контакт!"
    uf "{b}ОНИ{/b} сделали машины. Об этом я тебе и пытаюсь сказать. Мясо сделало машины."
    scene bg cosmos_2 with dissolve
    ub "Это смешно! Как может мясо сделать машину? Ты просишь меня поверить в разумное мясо?"
    uf "Я не прошу, я говорю. Эти создания – единственная разумная раса в этом секторе, и они сделаны из мяса."
    ub "Может они как орфоли? Ну тот углеводный интеллект, который проходит через стадию мяса?"
    uf "Вовсе нет. Они как рождаются мясом, так мясом и умирают."
    uf "Мы изучили их в нескольких поколениях, которые очень недолговечны. Как ты думаешь, сколько живёт мясо?"
    hide ufo_2
    show ufo_1 at right with moveinright
    with dissolve
    ub "Не до того! Хорошо, может они только частично мясные. Знаешь, как веддили."
    ub "Мясная голова, а внутри мозг из электронной плазмы."
    uf "И снова мимо. Мы подумали об этом сразу как увидели эти мясные головы, похожие на веддилические."
    uf "Но я же сказал, что мы проверили их. Они мясные целиком, сплошь."
    ub "Ну то есть мозга нет?"
    uf "О, у них нормальный мозг. Просто этот мозг…"
    scene bg cosmos_3 with hpunch
    uf "{b}СДЕЛАН ИЗ МЯСА!{/b} Я давно уже пытаюсь тебе это сказать!"
    ub "Так… а что же думает?"
    uf "Ты что, не понимаешь? Ты не слышишь, что я говорю? Мозг думает! Мясо."
    ub "Думающее мясо! Ты просишь меня поверить в думающее мясо!"
    uf "Да, думающее мясо! Сознательное мясо! Любящее мясо. Мечтающее мясо. Всё в мясе."
    uf "Ты начинаешь понимать или мне начать всё с начала?"
    ub "С ума сойти! Значит, ты серьёзно. Они сделаны из мяса."
    show ufo_2 at left with moveinleft
    uf "Спасибо! Наконец! Да. Они действительно сделаны из мяса."
    uf "И они пытаются вступить с нами в контакт почти сто их лет."
    ub "С ума сойти! Так какое же намерение у мяса?"
    uf "Сперва оно хочет поговорить с нами. Потом, я полагаю, оно захочет исследовать Вселенную, пообщаться с другими разумными, обменяться идеями и информацией – всё, как обычно."
    ub "Предположим, мы заговорим с мясом."
    scene bg cosmos_4 with dissolve
    uf "Что ж, это мысль. Вот сообщение, которое они посылают по радио:"
    u"Человек" "Привет! Есть кто там? Кто-нибудь дома?"
    uf "Как-то так."
    show ufo_1 at left with moveinleft
    ub "Значит, они действительно могут общаться. Они употребляют слова, мысли, понятия?"
    uf "Да да! Если не считать, что они делают это мясом."
    ub "Ты же только что сказал, что они используют для  этого радио."
    uf "Они используют радио, но как ты думаешь, что там, на радио? Звуки мяса!"
    uf "Представь, что ты хлопаешь или машешь мясом, оно будет издавать шум?"
    uf "Они разговаривают, шлёпая одной частью мяса по другой."
    uf "Они могут даже петь, пропуская воздух через собственное мясо!"
    ub "С ума сойти! Поющее мясо! Это уже слишком! Что ты посоветуешь?"
    uf "Официально или неофициально?"
    ub "И так и так."
    scene bg cosmos_5 with dissolve
    uf "Официально требуется, чтобы мы вступали в контакт, приглашали и регистрировали любые и все разумные расы и группы в этом квадрате Вселенной без предубеждений, страха и предпочтений."
    uf "А если строго между нами, то {i}я советую стереть все записи и забыть.{/i}"
    ub "Я надеялся, что ты так скажешь."
    show ufo_2 at right with moveinright
    uf "Может это и слишком радикально, но всему есть предел. Действительно ли мы хотим контакта с мясом?"
    ub "Согласен на 100 процентов. Что нам сказать?"
    u"Они" "Привет, мясо. Как ты там?"
    ub "Сработает ли это? Вообще, о каком количестве планет идёт речь?"
    uf "Всего об одной. Они могут путешествовать к другим планетам в специальном мясном контейнере, но жить на них не могут."
    uf "Будучи мясом, они способны к перемещению только в пространстве С, что ограничивает их скорости скоростью света и делает возможность вступить когда либо в контакт довольно слабой. Бесконечно малой."
    hide ufo_2
    ub "То есть нам нужно только притвориться, что дома никого и Вселенная пуста?"
    uf "Точно."
    scene bg cosmos_1 with dissolve
    ub "Жестоко."
    ub "Но ты и сам сказал, кто захочет встречаться с мясом."
    ub "А как же те, что побывали на нашем корабле, кого вы исследовали? Они не вспомнят?"
    uf "Если и вспомнят, их посчитают сумасшедшими. Но мы проникли к ним в головы и разгладили их мясо, так что встреча с нами стала снами."
    ub "Снами для мяса! Как-то странно представлять, что мы можем быть мясными снами!"
    uf "И мы отмечаем этот сектор как {b}НЕОБИТАЕМЫЙ{/b}."
    ub "Хорошо. Согласен, и официально и неофициально. Дело закрыто."
    scene bg cosmos_2 with dissolve
    ub "Что ещё? Есть кто заслуживающий внимания на этой стороне галактики?"
    uf "Да, довольно робкий, но приятный разум группы водородных ядер в звезде девятого класса зоны Г445"
    uf "Он выходил на контакт за два оборота галактики до этого и снова дружественно настроен."
    ub "Они всегда возвращаются…"
    uf "А почему бы нет? Представь, как невыносимо,.."
    scene black with dissolve2
    pause(1)
    stop music fadeout 2.0
    uf "Как невыразимо холодна была бы Вселенная, если бы мы все были…"
    uf "{i}одиноки…{/i}"
    scene black with dissolve
    hide ufo_1
    hide ufo_2
    with dspr
    pause(1)
    u"Терри Биссон" "Конец."
    u"Терри Биссон" "ОНИ СДЕЛАНЫ ИЗ МЯСА, 1990"
    u"Терри Биссон" "Перевод на русский язык: Анатолий Бойгок, 2012"
    u"Терри Биссон" "Музыка: композиция Magellan, авторство Aural Night"
    scene black with fade3
    return
label meat_old_en:
    $ uf = Character(u'Unknow', color="#6a5acd")
    $ ub = Character(u'Unknow', color="#f4a460")
    scene bg cosmos_1 with fade
    play music "meat/Aural_Night_Magellan.mp3"
    uf "They're made out of meat."
    show ufo_1 at left with moveinleft
    with dspr
    ub "Meat?"
    uf "Meat. They're made out of meat."
    ub "Meat?"
    show ufo_2 at right with moveinright
    with dspr
    uf "There's no doubt about it. We picked up several from different parts of the planet, took them aboard our recon vessels, and probed them all the way through."
    uf "They're completely meat."
    ub "That's impossible. What about the radio signals? The messages to the stars?"
    uf "They use the radio waves to talk, but the signals don't come from them. The signals come from machines."
    ub "So who made the machines? That's who we want to contact."
    uf "They made the machines. That's what I'm trying to tell you. Meat made the machines."
    scene bg cosmos_2 with dissolve
    ub "That's ridiculous. How can meat make a machine? You're asking me to believe in sentient meat."
    uf "I'm not asking you, I'm telling you. These creatures are the only sentient race in that sector and they're made out of meat."
    ub "Maybe they're like the orfolei. You know, a carbon-based intelligence that goes through a meat stage."
    uf "Nope. They're born meat and they die meat."
    uf "We studied them for several of their life spans, which didn't take long. Do you have any idea what's the life span of meat?"
    hide ufo_2
    show ufo_1 at right with moveinright
    with dissolve
    ub "Spare me. Okay, maybe they're only part meat. You know, like the weddilei."
    ub "A meat head with an electron plasma brain inside."
    uf "Nope. We thought of that, since they do have meat heads, like the weddilei."
    uf "But I told you, we probed them. They're meat all the way through."
    ub "No brain?"
    uf "Oh, there's a brain all right. It's just that the brain…"
    scene bg cosmos_3 with hpunch
    uf "{b}is made out of meat!{/b} That's what I've been trying to tell you."
    ub "So… what does the thinking?"
    uf "You're not understanding, are you? You're refusing to deal with what I'm telling you. The brain does the thinking. The meat."
    ub "Thinking meat! You're asking me to believe in thinking meat!"
    uf "Yes, thinking meat! Conscious meat! Loving meat. Dreaming meat. The meat is the whole deal!"
    uf "Are you beginning to get the picture or do I have to start all over?"
    ub "Omigod. You're serious then. They're made out of meat."
    show ufo_2 at left with moveinleft
    uf "Thank you. Finally. Yes. They are indeed made out of meat."
    uf "And they've been trying to get in touch with us for almost a hundred of their years."
    ub "Omigod. So what does this meat have in mind?"
    uf "First it wants to talk to us. Then I imagine it wants to explore the Universe, contact other sentiences, swap ideas and information. The usual."
    ub "We're supposed to talk to meat."
    scene bg cosmos_4 with dissolve
    uf "That's the idea. That's the message they're sending out by radio:"
    "Human" "Hello. Anyone out there. Anybody home."
    uf "That sort of thing."
    show ufo_1 at left with moveinleft
    ub "They actually do talk, then. They use words, ideas, concepts?"
    uf "Oh, yes. Except they do it with meat."
    ub "I thought you just told me they used radio."
    uf "They do, but what do you think is on the radio? Meat sounds."
    uf "You know how when you slap or flap meat, it makes a noise?"
    uf "They talk by flapping their meat at each other."
    uf "They can even sing by squirting air through their meat."
    ub "Omigod. Singing meat. This is altogether too much. So what do you advise?"
    uf "Officially or unofficially?"
    ub "Both."
    scene bg cosmos_5 with dissolve
    uf "Officially, we are required to contact, welcome and log in any and all sentient races or multibeings in this quadrant of the Universe, without prejudice, fear or favor."
    uf "Unofficially, {i}I advise that we erase the records and forget the whole thing.{/i}"
    ub "I was hoping you would say that."
    show ufo_2 at right with moveinright
    uf "It seems harsh, but there is a limit. Do we really want to make contact with meat?"
    ub "I agree one hundred percent. What's there to say?"
    "They" "Hello, meat. How's it going?"
    ub "But will this work? How many planets are we dealing with here?"
    uf "Just one. They can travel to other planets in special meat containers, but they can't live on them."
    uf "And being meat, they can only travel through C space. Which limits them to the speed of light and makes the possibility of their ever making contact pretty slim. Infinitesimal, in fact."
    hide ufo_2
    ub "So we just pretend there's no one home in the Universe."
    uf "That's it."
    scene bg cosmos_1 with dissolve
    ub "Cruel."
    ub "But you said it yourself, who wants to meet meat?"
    ub "And the ones who have been aboard our vessels, the ones you probed? You're sure they won't remember?"
    uf "They'll be considered crackpots if they do. We went into their heads and smoothed out their meat so that we're just a dream to them."
    ub "A dream to meat! How strangely appropriate, that we should be meat's dream."
    uf "And we marked the entire sector {b}unoccupied.{/b}"
    ub "Good. Agreed, officially and unofficially. Case closed."
    scene bg cosmos_2 with dissolve
    ub "Any others? Anyone interesting on that side of the galaxy?"
    uf "Yes, a rather shy but sweet hydrogen core cluster intelligence in a class nine star in G445 zone."
    uf "Was in contact two galactic rotations ago, wants to be friendly again."
    ub "They always come around."
    uf "And why not? Imagine how unbearably,.."
    scene black with dissolve2
    pause(1)
    stop music fadeout 2.0
    uf "How unutterably cold the Universe would be if one were all…"
    uf "{i}alone…{/i}"
    scene black with dissolve
    hide ufo_1
    hide ufo_2
    with dspr
    pause(1)
    "Terry Bisson" "The End."
    "Terry Bisson" "THEY'RE MADE OUT OF MEAT, 1990"
    "Terry Bisson" "Music: Magellan by Aural Night"
    scene black with fade3
    return

label meat_new:
    scene black
    with dissolve
    pause(1)
    if _preferences.language == None:
        jump meat_new_ru
    else:
        jump meat_new_en
    return

label meat_new_en:
    play music "meat/Aural_Night_Magellan.mp3"
    scene black
    sh "They're made out of meat."
    scene bg ext_dining_hall_near_night
    show el surprise pioneer far at cleft
    show sh serious pioneer far at cright
    with dissolve
    el "Meat?"
    sh "Meat. They're made out of meat."
    el "Meat?"
    sh "There's no doubt about it. We picked up several from different parts of the planet, took them aboard our recon vessels, and probed them all the way through."
    sh "They're completely meat."
    show el shocked pioneer far at cleft with dspr
    el "That's impossible. What about the radio signals? The messages to the stars?"
    sh "They use the radio waves to talk, but the signals don't come from them. The signals come from machines."
    show sh normal pioneer far at cright with dspr
    el "So who made the machines? That's who we want to contact."
    sh "{b}They{/b} made the machines. That's what I'm trying to tell you. Meat made the machines."
    show el smile pioneer far at cleft with dspr
    el "That's ridiculous. How can meat make a machine? You're asking me to believe in sentient meat."
    sh "I'm not asking you, I'm telling you. These creatures are the only sentient race in that sector and they're made out of meat."
    show el normal pioneer far at cleft with dspr
    el "Maybe they're like the orfolei. You know, a carbon-based intelligence that goes through a meat stage."
    sh "Nope. They're born meat and they die meat."
    sh "We studied them for several of their life spans, which didn't take long. Do you have any idea what's the life span of meat?"
    el "Spare me. Okay, maybe they're only part meat. You know, like the weddilei."
    el "A meat head with an electron plasma brain inside."
    sh "Nope. We thought of that, since they do have meat heads, like the weddilei."
    sh "But I told you, we probed them. They're meat all the way through."
    el "No brain?"
    sh "Oh, there's a brain all right. It's just that the brain…"
    show sh rage pioneer far at cright with dspr
    sh "{b}is made out of meat!{/b} That's what I've been trying to tell you."
    show sh normal pioneer far at cright with dspr
    el "So… what does the thinking?"
    sh "You're not understanding, are you? You're refusing to deal with what I'm telling you. The brain does the thinking. The meat."
    scene bg ext_dining_hall_away_night
    show el shocked pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "Thinking meat! You're asking me to believe in thinking meat!"
    sh "Yes, thinking meat! Conscious meat! Loving meat. Dreaming meat. The meat is the whole deal!"
    sh "Are you beginning to get the picture or do I have to start all over?"
    el "Omigod. You're serious then. They're made out of meat."
    sh "Thank you. Finally. Yes. They are indeed made out of meat."
    show el normal pioneer far at cleft with dspr
    sh "And they've been trying to get in touch with us for almost a hundred of their years."
    el "Omigod. So what does this meat have in mind?"
    scene bg ext_clubs_night
    show el normal pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    sh "First it wants to talk to us. Then I imagine it wants to explore the Universe, contact other sentiences, swap ideas and information. The usual."
    el "We're supposed to talk to meat."
    sh "That's the idea. That's the message they're sending out by radio:"
    pi "Hello. Anyone out there. Anybody home."
    sh "That sort of thing."
    scene bg ext_path_night
    show el normal pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "They actually do talk, then. They use words, ideas, concepts?"
    sh "Oh, yes. Except they do it with meat."
    el "I thought you just told me they used radio."
    sh "They do, but what do you think is on the radio? Meat sounds."
    sh "You know how when you slap or flap meat, it makes a noise?"
    sh "They talk by flapping their meat at each other."
    sh "They can even sing by squirting air through their meat."
    scene bg ext_aidpost_night
    show el surprise pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "Omigod. Singing meat. This is altogether too much. So what do you advise?"
    sh "Officially or unofficially?"
    show el normal pioneer far at cleft with dspr
    el "Both."
    scene bg ext_path2_night
    show el normal pioneer far at cleft
    show sh serious pioneer far at cright
    with dissolve
    sh "Officially, we are required to contact, welcome and log in any and all sentient races or multibeings in this quadrant of the Universe, without prejudice, fear or favor."
    sh "Unofficially, {i}I advise that we erase the records and forget the whole thing.{/i}"
    el "I was hoping you would say that."
    sh "It seems harsh, but there is a limit. Do we really want to make contact with meat?"
    el "I agree one hundred percent. What's there to say?"
    me "Hello, meat. How's it going?"
    scene bg ext_square_night
    show el normal pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "But will this work? How many planets are we dealing with here?"
    sh "Just one. They can travel to other planets in special meat containers, but they can't live on them."
    sh "And being meat, they can only travel through C space. Which limits them to the speed of light and makes the possibility of their ever making contact pretty slim. Infinitesimal, in fact."
    el "So we just pretend there's no one home in the Universe."
    show sh serious pioneer far at cright with dspr
    sh "That's it."
    el "Cruel."
    el "But you said it yourself, who wants to meet meat?"
    scene bg ext_bus_night
    show el normal pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "And the ones who have been aboard our vessels, the ones you probed? You're sure they won't remember?"
    sh "They'll be considered crackpots if they do. We went into their heads and smoothed out their meat so that we're just a dream to them."
    el "A dream to meat! How strangely appropriate, that we should be meat's dream."
    sh "And we marked the entire sector {b}unoccupied.{/b}"
    el "Good. Agreed, officially and unofficially. Case closed."
    scene bg int_bus_night
    show el normal pioneer close at cleft
    show sh normal pioneer close at cright
    with dissolve
    el "Any others? Anyone interesting on that side of the galaxy?"
    sh "Yes, a rather shy but sweet hydrogen core cluster intelligence in a class nine star in G445 zone."
    sh "Was in contact two galactic rotations ago, wants to be friendly again."
    el "They always come around."
    sh "And why not? Imagine how unbearably,.."
    scene black with dissolve2
    pause(1)
    stop music fadeout 2.0
    sh "How unutterably cold the Universe would be if one were all…"
    sh "{i}alone…{/i}"
    scene black with dissolve
    with dspr
    pause(1)
    "Terry Bisson" "The End."
    "Terry Bisson" "THEY'RE MADE OUT OF MEAT, 1990"
    "Terry Bisson" "Music: Magellan by Aural Night"
    scene black with fade3
    return

label meat_new_ru:
    play music "meat/Aural_Night_Magellan.mp3"
    scene black
    sh "Они мясные."
    sh "Они сделаны из мяса."
    scene bg ext_dining_hall_near_night
    show el surprise pioneer far at cleft
    show sh serious pioneer far at cright
    with dissolve
    el "Из мяса?"
    sh "Из мяса. Они сделаны из мяса."
    el "Мяса?"
    sh "В этом не может быть сомнений. Мы отобрали нескольких представителей из разных мест планеты, доставили их на борт нашей лаборатории и исследовали их до мельчайших подробностей."
    sh "Они полностью мясные."
    show el shocked pioneer far at cleft with dspr
    el "Это невозможно! А как же радиосигналы? Послания к звёздам?"
    sh "Они используют радиоволны для общения, но сигналы исходят не от них, а от машин."
    show sh normal pioneer far at cright with dspr
    el "Так кто сделал машины? Вот с кем нам надо найти контакт!"
    sh "{b}ОНИ{/b} сделали машины. Об этом я тебе и пытаюсь сказать. Мясо сделало машины."
    show el smile pioneer far at cleft with dspr
    el "Это смешно! Как может мясо сделать машину? Ты просишь меня поверить в разумное мясо?"
    sh "Я не прошу, я говорю. Эти создания – единственная разумная раса в этом секторе, и они сделаны из мяса."
    show el normal pioneer far at cleft with dspr
    el "Может они как орфоли? Ну тот углеводный интеллект, который проходит через стадию мяса?"
    sh "Вовсе нет. Они как рождаются мясом, так мясом и умирают."
    sh "Мы изучили их в нескольких поколениях, которые очень недолговечны. Как ты думаешь, сколько живёт мясо?"
    el "Не до того! Хорошо, может они только частично мясные. Знаешь, как веддили."
    el "Мясная голова, а внутри мозг из электронной плазмы."
    sh "И снова мимо. Мы подумали об этом сразу как увидели эти мясные головы, похожие на веддилические."
    sh "Но я же сказал, что мы проверили их. Они мясные целиком, сплошь."
    el "Ну то есть мозга нет?"
    sh "О, у них нормальный мозг. Просто этот мозг…"
    show sh rage pioneer far at cright with dspr
    sh "{b}СДЕЛАН ИЗ МЯСА!{/b} Я давно уже пытаюсь тебе это сказать!"
    show sh normal pioneer far at cright with dspr
    el "Так… а что же думает?"
    sh "Ты что, не понимаешь? Ты не слышишь, что я говорю? Мозг думает! Мясо."
    scene bg ext_dining_hall_away_night
    show el shocked pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "Думающее мясо! Ты просишь меня поверить в думающее мясо!"
    sh "Да, думающее мясо! Сознательное мясо! Любящее мясо. Мечтающее мясо. Всё в мясе."
    sh "Ты начинаешь понимать или мне начать всё с начала?"
    el "С ума сойти! Значит, ты серьёзно. Они сделаны из мяса."
    sh "Спасибо! Наконец! Да. Они действительно сделаны из мяса."
    show el normal pioneer far at cleft with dspr
    sh "И они пытаются вступить с нами в контакт почти сто их лет."
    el "С ума сойти! Так какое же намерение у мяса?"
    scene bg ext_clubs_night
    show el normal pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    sh "Сперва оно хочет поговорить с нами. Потом, я полагаю, оно захочет исследовать Вселенную, пообщаться с другими разумными, обменяться идеями и информацией – всё, как обычно."
    el "Предположим, мы заговорим с мясом."
    sh "Что ж, это мысль. Вот сообщение, которое они посылают по радио:"
    pi "Привет! Есть кто там? Кто-нибудь дома?"
    sh "Как-то так."
    scene bg ext_path_night
    show el normal pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "Значит, они действительно могут общаться. Они употребляют слова, мысли, понятия?"
    sh "Да да! Если не считать, что они делают это мясом."
    el "Ты же только что сказал, что они используют для  этого радио."
    sh "Они используют радио, но как ты думаешь, что там, на радио? Звуки мяса!"
    sh "Представь, что ты хлопаешь или машешь мясом, оно будет издавать шум?"
    sh "Они разговаривают, шлёпая одной частью мяса по другой."
    sh "Они могут даже петь, пропуская воздух через собственное мясо!"
    scene bg ext_aidpost_night
    show el surprise pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "С ума сойти! Поющее мясо! Это уже слишком! Что ты посоветуешь?"
    sh "Официально или неофициально?"
    show el normal pioneer far at cleft with dspr
    el "И так и так."
    scene bg ext_path2_night
    show el normal pioneer far at cleft
    show sh serious pioneer far at cright
    with dissolve
    sh "Официально требуется, чтобы мы вступали в контакт, приглашали и регистрировали любые и все разумные расы и группы в этом квадрате Вселенной без предубеждений, страха и предпочтений."
    sh "А если строго между нами, то {i}я советую стереть все записи и забыть.{/i}"
    el "Я надеялся, что ты так скажешь."
    sh "Может это и слишком радикально, но всему есть предел. Действительно ли мы хотим контакта с мясом?"
    el "Согласен на 100 процентов. Что нам сказать?"
    me "Привет, мясо. Как ты там?"
    scene bg ext_square_night
    show el normal pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "Сработает ли это? Вообще, о каком количестве планет идёт речь?"
    sh "Всего об одной. Они могут путешествовать к другим планетам в специальном мясном контейнере, но жить на них не могут."
    sh "Будучи мясом, они способны к перемещению только в пространстве С, что ограничивает их скорости скоростью света и делает возможность вступить когда либо в контакт довольно слабой. Бесконечно малой."
    el "То есть нам нужно только притвориться, что дома никого и Вселенная пуста?"
    show sh serious pioneer far at cright with dspr
    sh "Точно."
    el "Жестоко."
    el "Но ты и сам сказал, кто захочет встречаться с мясом."
    scene bg ext_bus_night
    show el normal pioneer far at cleft
    show sh normal pioneer far at cright
    with dissolve
    el "А как же те, что побывали на нашем корабле, кого вы исследовали? Они не вспомнят?"
    sh "Если и вспомнят, их посчитают сумасшедшими. Но мы проникли к ним в головы и разгладили их мясо, так что встреча с нами стала снами."
    el "Снами для мяса! Как-то странно представлять, что мы можем быть мясными снами!"
    sh "И мы отмечаем этот сектор как {b}НЕОБИТАЕМЫЙ{/b}."
    el "Хорошо. Согласен, и официально и неофициально. Дело закрыто."
    scene bg int_bus_night
    show el normal pioneer close at cleft
    show sh normal pioneer close at cright
    with dissolve
    el "Что ещё? Есть кто заслуживающий внимания на этой стороне галактики?"
    sh "Да, довольно робкий, но приятный разум группы водородных ядер в звезде девятого класса зоны Г445"
    sh "Он выходил на контакт за два оборота галактики до этого и снова дружественно настроен."
    el "Они всегда возвращаются…"
    sh "А почему бы нет? Представь, как невыносимо,.."
    scene black with dissolve2
    pause(1)
    stop music fadeout 2.0
    sh "Как невыразимо холодна была бы Вселенная, если бы мы все были…"
    sh "{i}одиноки…{/i}"
    scene black with dissolve
    with dspr
    pause(1)
    u"Терри Биссон" "Конец."
    u"Терри Биссон" "ОНИ СДЕЛАНЫ ИЗ МЯСА, 1990"
    u"Терри Биссон" "Перевод на русский язык: Анатолий Бойгок, 2012"
    u"Терри Биссон" "Музыка: композиция Magellan, авторство Aural Night"
    scene black with fade3
    return