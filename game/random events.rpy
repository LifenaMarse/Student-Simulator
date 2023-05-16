# учебные с.с.
# с.с. при "Заниматься дома"
# label home_study:
#     $ which_random_event = renpy.random.randint(1, 10)

#     return



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
# с.с. при "Пойти работать в цветочный магазин"
label flower_shop_work:
    $ which_random_event = renpy.random.randint(1, 10)

    return


# с.с. при "Пойти работать в бар"
label bar_work:
    $ which_random_event = renpy.random.randint(1, 10)

    return


# с.с. при "Пойти работать строителем"
label builder_work:
    $ which_random_event = renpy.random.randint(1, 10)

    return





# ментальные с.с.
# с.с. при "Пойти к психологу"
label go_psychologist:
    $ which_random_event = renpy.random.randint(1, 10)

    return


# с.с. при "Пойти гулять с друзьями"
label friends_hang_out:
    $ which_random_event = renpy.random.randint(1, 10)

    return


# с.с. при "Провести день с самим собой"
label day_with_yourself:
    $ which_random_event = renpy.random.randint(1, 10)

    return




# физкультурные с.с.
# с.с. при "Пойти в качалку"
label gym:
    $ which_random_event = renpy.random.randint(1, 10)

    return


# с.с. при "Пойти на спортплощадку"
label sports_ground:
    $ which_random_event = renpy.random.randint(1, 10)

    return


# с.с. при "Покататься на коньках"
label skating:
    $ which_random_event = renpy.random.randint(1, 10)

    return


# с.с. при "Позаниматься дома"
label home_sport:
    $ which_random_event = renpy.random.randint(1, 10)

    return

