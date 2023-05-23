
# с.с. при "Заниматься дома"
# label home_study:
#     $ which_random_event = renpy.random.randint(1, 10)
#     return


# учебные с.с.
# готово
# с.с. при "Пойти в универ"
label go_university:
    if studies <= 20:   
        $ which_random_event = renpy.random.randint(3, 4)
    else:
        $ which_random_event = renpy.random.randint(1, 4)

    if which_random_event == 1:
        $ studies = change_parameter(studies - 10)
        $ mental_health = change_parameter(mental_health - 5)
        "На днях была контрольная работа, а ты ее пропустил. Придется исправлять."
    elif which_random_event == 2:
        $ studies = change_parameter(studies - 5)
        $ mental_health = change_parameter(mental_health - 5)
        "Ты просрочил дедлайн по домашнему заданию. За тебя это никто не будет запоминать."
    elif which_random_event == 3:
        $ studies = change_parameter(studies + 15)
        "Вы пишите какую-то работы и тебе повезло сесть рядом с отличником. В итоге ты получил максимальный балл."
    else:
        $ studies = change_parameter(studies + 15)
        "Сегодня пара с твоим любимым преподавателем, который любит свой предмет и отлично объясняет материал, что отражается в твоем восприятие дисциплины."
    return


# готово
# с.с. при "Сходить к репетитору"
label go_tutor:
    if studies <= 20:
        $ which_random_event = renpy.random.randint(3, 4)
    else:
        $ which_random_event = renpy.random.randint(1, 4)

    if which_random_event == 1:
        $ studies = change_parameter(studies - 5)
        $ mental_health = change_parameter(mental_health - 5)
        $ finance = change_parameter(finance - 10)
        "Ты купил какой-то онлайн курс, а там оказалась обычная инфа с википедии и других открытых источников. SCUM"
    elif which_random_event == 2:
        $ mental_health = change_parameter(mental_health - 5)
        $ finance = change_parameter(finance - 10)
        "Сегодня ты занимался в группе, преподаватель уделял тебе меньше времени. У тебя остались вопросы."
    elif which_random_event == 3:
        $ studies = change_parameter(studies + 20)
        $ finance = change_parameter(finance - 10)
        "Преподаватель поделился с тобой очень полезной литературой, о которой мало кто знает."
    else:
        $ studies = change_parameter(studies + 25)
        $ finance = change_parameter(finance - 10)
        "Преподаватель разработал для тебя индивидуальную образовательную программу, что помогло тебе лучше разобрать и понять материал."

    return



# рабочие с.с.
# готово
# с.с. при "Пойти работать в цветочный магазин"
label flower_shop_work:
    if studies <= 20:
        $ which_random_event = renpy.random.randint(3, 4)
    else:
        $ which_random_event = renpy.random.randint(1, 4)

    if which_random_event == 1:
        $ physical_health = change_parameter(physical_health - 5)
        "У клиента был четкий запрос на виды цветов в букете, но ты все перепутал и набрал совсем других."
    elif which_random_event == 2:
        $ finance = change_parameter(finance + 5)
        $ physical_health = change_parameter(physical_health - 5)
        $ mental_health = change_parameter(mental_health - 5)
        "Ты случайно собрал клиенту букет с четным количеством цветов, владельцу это не понравиться, будь внимательней!"
    elif which_random_event == 3:
        $ finance = change_parameter(finance + 15)
        $ physical_health = change_parameter(physical_health - 5)
        "В магазин забегал парень, который явно куда-то спешил, за приличный букет кинул крупную купюру, и без сдачи поспешил дальше."
    else:
        $ finance = change_parameter(finance + 10)
        $ physical_health = change_parameter(physical_health - 5)
        $ mental_health = change_parameter(mental_health + 7)
        "Сегодня в магазин завезли особо вкусно пахнущие цветы, нюхать их целый день довольно приятно."

    return


# готово
# с.с. при "Пойти работать в бар"
label bar_work:
    if studies <= 20:
        $ which_random_event = renpy.random.randint(3, 4)
    else:
        $ which_random_event = renpy.random.randint(1, 4)

    if which_random_event == 1:
        $ finance = change_parameter(finance + 10)
        $ physical_health = change_parameter(physical_health - 10)
        $ mental_health = change_parameter(mental_health - 5)
        "Сегодня особенно многолюдно, ты не вывозишь большого трафика людей, посетители недовольны."
    elif which_random_event == 2:
        $ finance = change_parameter(finance + 15)
        $ physical_health = change_parameter(physical_health - 15)
        $ mental_health = change_parameter(mental_health - 5)
        "Одному синяку не понравилось то, как ты на него смотрел, теперь ты панда."
    elif which_random_event == 3:
        $ finance = change_parameter(finance + 20)
        $ physical_health = change_parameter(physical_health - 10)
        $ mental_health = change_parameter(mental_health + 5)
        "Одна мадама весь вечер строила тебе глазки, а когда ушла, оставила неплохие чаевые."
    else:
        $ finance = change_parameter(finance + 15)
        $ physical_health = change_parameter(physical_health - 5)
        $ mental_health = change_parameter(mental_health + 2)
        "На вечер бар заняли футбольные болельщики, они больше сконцентрированы на игре, чем на еде. Да и атмосфера хорошая."      
    return


# готово
# с.с. при "Пойти работать строителем"
label builder_work:
    if studies <= 20:
        $ which_random_event = renpy.random.randint(3, 4)
    else:
        $ which_random_event = renpy.random.randint(1, 4)

    if which_random_event == 1:
        $ finance = change_parameter(finance + 20)
        $ physical_health = change_parameter(physical_health - 25)
        "Упал кирпич на голову, хотя бы ты был в каске."
    elif which_random_event == 2:
        $ finance = change_parameter(finance + 15)
        $ physical_health = change_parameter(physical_health - 15)
        "Ты так и не понял как должен стоять пакалодник: вровень со стенкой или выпирать. Ну начальника!"
    elif which_random_event == 3:
        $ finance = change_parameter(finance + 27)
        $ physical_health = change_parameter(physical_health - 15)
        "Сегодня ездил в какой-то элитный коттеджный поселок, строить дом депутату."
    else:
        $ finance = change_parameter(finance + 20)
        $ physical_health = change_parameter(physical_health - 15)
        $ mental_health = change_parameter(mental_health + 10)
        "Сдружился с узбеками, накормили пловом. "

    return



# ментальные с.с.
# с.с. при "Пойти к психологу"
# label go_psychologist:
#     if studies <= 20:
#         $ which_random_event = renpy.random.randint(3, 4)
#     else:
#         $ which_random_event = renpy.random.randint(1, 4)

#     if which_random_event == 1:

#         ""
#     elif which_random_event == 2:

#         ""
#     elif which_random_event == 3:

#         ""
#     else:

#         ""

#     return


# готово
# с.с. при "Пойти гулять с друзьями"
label friends_hang_out:
    if studies <= 20:
        $ which_random_event = renpy.random.randint(3, 4)
    else:
        $ which_random_event = renpy.random.randint(1, 4)

    if which_random_event == 1:
        $ mental_health = change_parameter(mental_health + 15)
        $ finance = change_parameter(finance - 10)
        "Один другалек попросил в долг, ну как отказать. А вернет ли, это вопрос."
    elif which_random_event == 2:
        $ mental_health = change_parameter(mental_health + 15)
        $ finance = change_parameter(finance - 5)
        $ physical_health = change_parameter(physical_health - 10)
        "Кто-то предложил купить алкашки, стоит нам собраться этим все и заканчивается. Ох, печень моя, печень!"
    elif which_random_event == 3:
        $ mental_health = change_parameter(mental_health + 20)
        $ finance = change_parameter(finance - 5)
        "Встретились с лучшем другом, разговоры по душам с этим человеком могут заменить психолога."
    else:
        $ mental_health = change_parameter(mental_health + 25)
        $ finance = change_parameter(finance - 5)
        $ physical_health = change_parameter(physical_health - 7)
        "Один приятель позвал к себе на хату. На следующее утро сложно вспомнить что было вчера, но встречаешь ты его не один, рядом сопит какое-то чудо."

    return


# готово
# с.с. при "Провести день с самим собой"
label day_with_yourself:
    if studies <= 20:
        $ which_random_event = renpy.random.randint(3, 4)
    else:
        $ which_random_event = renpy.random.randint(1, 4)

    if which_random_event == 1:
        $ mental_health = change_parameter(mental_health - 7)
        "Пошел играть в любимую онлайн игру, но то тима - раки, то у тебя аим - мимо. В общем, нужен новый стул."
    elif which_random_event == 2:
        $ mental_health = change_parameter(mental_health + 5)
        $ physical_health = change_parameter(physical_health - 5)
        "Пока пытался осилить новый сезон сериала, не заметил как заточил пару пачек чипсов, пару банок газировки и несколько бутеров."
    elif which_random_event == 3:
        $ mental_health = change_parameter(mental_health + 10)
        "Десятки, а то и сотни часов потрачены не впустую, + платина еще в одном тайтле."
    else:
        $ mental_health = change_parameter(mental_health + 5)
        $ studies = change_parameter(studies + 5)
        "После просмотра очередного кино произведения, решил ознакомиться с книжным оригиналом, читать же вроде как полезно."

    return



# готово
# физкультурные с.с.
# с.с. при "Пойти в качалку"
label gym:
    if studies <= 20:
        $ which_random_event = renpy.random.randint(3, 4)
    else:
        $ which_random_event = renpy.random.randint(1, 4)

    if which_random_event == 1:
        $ physical_health = change_parameter(physical_health + 25)
        $ mental_health = change_parameter(mental_health - 10)
        $ finance = change_parameter(finance - 15)
        "Во время работы с весами ты перенапрягся и это слышала большая часть зала."
    elif which_random_event == 2:
        $ physical_health = change_parameter(physical_health + 20)
        $ mental_health = change_parameter(mental_health - 5)
        $ finance = change_parameter(finance - 15)
        "Пошел на беговую дорожку, а прямо перед тобой занималась девушка, чьи родители походу пекари. Оказалось, потерять равновесие и улететь можно за считанные секунды."
    elif which_random_event == 3:
        $ physical_health = change_parameter(physical_health + 30)
        $ finance = change_parameter(finance - 15)
        "Видя как ты мучаешься с тренажером, какой-то тренер решил помочь тебе. Ааа, так вот как им пользоваться."
    else:
        $ physical_health = change_parameter(physical_health + 35)
        $ mental_health = change_parameter(mental_health + 3)
        $ finance = change_parameter(finance - 20)
        "В раздевалке шнырял какой-то подозрительный тип и предлагал протеин, недорого. Ну ты не дурак, купил себе, мышцы растут как на дрожжах."

    return


# готово
# с.с. при "Пойти на спортплощадку"
label sports_ground:
    if studies <= 20:
        # $ which_random_event = renpy.random.randint(3, 4)
        $ which_random_event = 2
    else:
        $ which_random_event = renpy.random.randint(1, 2)

    if which_random_event == 1:
        $ physical_health = change_parameter(physical_health - 5)
        $ mental_health = change_parameter(mental_health - 5)
        "Ты плохо размялся и сразу полез на перекладину, как итог потянул мышцу."
    else:
        $ physical_health = change_parameter(physical_health + 17)
        $ mental_health = change_parameter(mental_health + 10)
        "После большого количества попыток и повторений у тебя все таки получилось выполнить новый элемент на турнике."


    # elif which_random_event == 2:

    #     ""
    # elif which_random_event == 3:

    #     ""
    # else:

    #     ""

    return


# готово
# с.с. при "Покататься на коньках"
label skating:
    if studies <= 20:
        # $ which_random_event = renpy.random.randint(3, 4)
        $ which_random_event = 2
    else:
        $ which_random_event = renpy.random.randint(1, 2)

    if which_random_event == 1:
        $ physical_health = change_parameter(physical_health + 5)
        $ finance = change_parameter(finance - 5)
        "Носясь по катку, у тебя сбивается дыхание и тебе приходится дышать ртом. Как оказывается холодный воздух негативно сказывается на здоровье."
    else:
        $ physical_health = change_parameter(physical_health + 10)
        $ mental_health = change_parameter(mental_health + 10)
        $ finance = change_parameter(finance - 5)
        "На катке пацаны играли в хоккей, ты напросился к ним и по итогу хорошо провел время."    

    return


# с.с. при "Позаниматься дома"
# label home_sport:
#     if studies <= 20:
#         $ which_random_event = renpy.random.randint(3, 4)
#     else:
#         $ which_random_event = renpy.random.randint(1, 4)

#     if which_random_event == 1:

#         ""
#     elif which_random_event == 2:

#         ""
#     elif which_random_event == 3:

#         ""
#     else:

#         ""

#     return

