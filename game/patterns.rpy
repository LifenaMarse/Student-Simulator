# паттерн учебы
label get_studies:
    menu:
        "ГДЗ физкультура 5 класс"
        "Заниматься дома":
            if renpy.random.randint(1, 2) == 1:
                $ studies = change_parameter(studies + 5)
                "У тебя получилось довольно продуктивно позаниматься!"
            else:
                $ studies = change_parameter(studies + 1)
                "Непонятно, что ты делал больше: занимался или отвлекался на посторонние вещи."

        "Пойти в универ" if workday:
            if calendar[calendar_counter][4]:
                call mini_games
            elif random_event:
                call go_university
            else:
                $ studies = change_parameter(studies + 10)
                $ mental_health = change_parameter(mental_health - 5)
                $ physical_health = change_parameter(physical_health - 3)          
                "Сегодня ты сходил на пары, молодец!"      

        "Сходить к репетитору":
            if random_event:
                call go_tutor
            else:
                $ studies = change_parameter(studies + 15)
                $ finance = change_parameter(finance - 10)
                $ mental_health = change_parameter(mental_health - 5)
                "Ты чувствуешь, как прибавилось в голове и убавилось в кармане."
    return


# паттерн финансов
label get_finance:
    menu:
        "Где деньги взять?"
        "Пойти работать в цветочный магазин":
            if random_event:
                call flower_shop_work
            else:
                $ finance = change_parameter(finance + 10)
                $ physical_health = change_parameter(physical_health - 5) 
                "Платят не шибко, но зато красиво."

        "Пойти работать в бар":
            if random_event:
                call bar_work
            else:
                $ finance = change_parameter(finance + 15)
                $ physical_health = change_parameter(physical_health - 10) 
                "Пивас за счет заведения"

        "Пойти работать строителем":
            if random_event:
                call builder_work
            elif good_weather:
                $ finance = change_parameter(finance + 20)
                $ physical_health = change_parameter(physical_health - 15) 
                "Тяжко, зато прибыльно."  
            else:
                $ finance = change_parameter(finance + 20)
                $ physical_health = change_parameter(physical_health - 20)
                $ mental_health = change_parameter(mental_health - 10)
                "Работать в непогоду под открытым небом - такое себе."

    if workday:
        $ studies = change_parameter(studies - 5)

    return


# паттерн ментального здоровья
label get_mental_health:
    menu:
        "Беды с башкой"
        "Пойти к психологу":
            $ mental_health = change_parameter(mental_health + 30)
            $ finance = change_parameter(finance - 20)
            "Так и разориться недолго, но тараканы потихоньку уползают."

            # if random_event:
            #     call go_psychologist
            # else:
            #     $ mental_health = change_parameter(mental_health + 30)
            #     $ finance = change_parameter(finance - 20)
            #     "Так и разориться недолго, но тараканы потихоньку уползают."

        # "Встретиться с друзьями":
        "Пойти гулять с друзьями":
            if good_weather == False:
                $ mental_health = change_parameter(mental_health + 10)
                $ physical_health = change_parameter(physical_health - 5)
                $ finance = change_parameter(finance - 5)
                "Возможно стоило выбрать другой день для встречи."
            elif random_event:
                call friends_hang_out
            else:
                $ mental_health = change_parameter(mental_health + 15)
                $ finance = change_parameter(finance - 5)
                "Люблю этих оболтусов"

        "Провести день с самим собой - поиграть в игры / посмотреть сериал":
            if random_event:
                call day_with_yourself
            else:
                $ mental_health = change_parameter(mental_health + 5)
                "Откис, но дела сами собой не сделаются."
    if workday:
        $ studies = change_parameter(studies - 5)
    return


# паттерн физического здоровья
label get_physical_health:
    menu:
        "Банки 5 литров"
        "Пойти в качалку":
            if random_event:
                call gym
            else:
                $ physical_health = change_parameter(physical_health + 25)
                $ mental_health = change_parameter(mental_health + 3)
                $ finance = change_parameter(finance - 15)
                "Чувствуешь себя like Boss of the gym!"

        "Пойти на спортплощадку" if month != 'Декабрь' or month != 'Январь':
            if good_weather == False:
                $ physical_health = change_parameter(physical_health + 5)
                $ mental_health = change_parameter(mental_health - 3)
                "Ты толком не позанимался, зря только выходил на улицу."
            elif random_event:
                call sports_ground
            else:
                $ physical_health = change_parameter(physical_health + 15)
                $ mental_health = change_parameter(mental_health + 3)
                "С буквой \"о\" сила, с буквой \"и\" могила!"

        "Покататься на коньках" if month == 'Декабрь' or month == 'Январь':
            if random_event:
                call skating
            else:
                $ physical_health = change_parameter(physical_health + 10)
                $ mental_health = change_parameter(mental_health + 5)
                $ finance = change_parameter(finance - 5)
                "Если ни разу не упал, считай победил."

        "Позаниматься дома":
            $ physical_health = change_parameter(physical_health + 5)
            $ mental_health = change_parameter(mental_health + 1)
            "Ну ка, где мои гантельки?"
            
            # if random_event:
            #     call home_sport
            # else:
            #     $ physical_health = change_parameter(physical_health + 5)
            #     $ mental_health = change_parameter(mental_health + 1)
            #     "Ну ка, где мои гантельки?"
    if workday:
        $ studies = change_parameter(studies - 5)

    return


    