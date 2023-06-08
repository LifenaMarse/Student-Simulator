# паттерн учебы
label get_studies:
    menu:
        "Пойти учиться"
        "Заниматься дома":
            if renpy.random.randint(1, 2) == 1:
                $ studies = change_parameter(studies + 5)
                "У тебя получилось довольно продуктивно позаниматься!"
            else:
                $ studies = change_parameter(studies + 1)
                "Непонятно, что ты делал больше: занимался или отвлекался на посторонние вещи."
            $ mental_health = change_parameter(mental_health - 1)
            $ physical_health = change_parameter(physical_health - 1) 

        "Пойти в универ" if workday and month != 'Январь':
            if calendar[calendar_counter][4]:
                if faculty_IT:
                    call mini_games_IT from _call_mini_games_IT
                elif faculty_medicine:
                    call mini_games_medicine from _call_mini_games_medicine
                else:
                    call mini_games_humanitarian from _call_mini_games_humanitarian

            elif random_event:
                call go_university from _call_go_university
            else:
                $ studies = change_parameter(studies + 10)
                $ mental_health = change_parameter(mental_health - 5)
                $ physical_health = change_parameter(physical_health - 3)        
                "Сегодня ты сходил на пары, молодец!"      

        "Сходить к репетитору":
            if random_event:
                call go_tutor from _call_go_tutor
            else:
                $ studies = change_parameter(studies + 15)
                $ finance = change_parameter(finance - 10)
                $ mental_health = change_parameter(mental_health - 5)
                "Ты чувствуешь, как прибавилось в голове и убавилось в кармане."
    return


# паттерн финансов
label get_finance:
    menu:
        "Пойти работать"
        "Пойти работать в цветочный магазин":
            if random_event:
                call flower_shop_work from _call_flower_shop_work
            else:
                $ finance = change_parameter(finance + 10)
                $ physical_health = change_parameter(physical_health - 5) 
                "Платят не шибко, но зато красиво."

        "Пойти работать в бар":
            if random_event:
                call bar_work from _call_bar_work
            else:
                $ finance = change_parameter(finance + 15)
                $ physical_health = change_parameter(physical_health - 10) 
                "Бутылочка бесплатного холодненького темного, самое то под вечер!"

        "Пойти работать строителем":
            if random_event:
                call builder_work from _call_builder_work
            elif good_weather:
                $ finance = change_parameter(finance + 20)
                $ physical_health = change_parameter(physical_health - 15) 
                "Тяжко, зато прибыльно."  
            else:
                $ finance = change_parameter(finance + 20)
                $ physical_health = change_parameter(physical_health - 20)
                $ mental_health = change_parameter(mental_health - 10)
                "Работать в непогоду под открытым небом - такое себе."

    if workday and month != 'Январь':
        $ studies = change_parameter(studies - 5)

    return


# паттерн ментального здоровья
label get_mental_health:
    menu:
        "Решать беды с башкой"
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
                call friends_hang_out from _call_friends_hang_out
            else:
                $ mental_health = change_parameter(mental_health + 15)
                $ finance = change_parameter(finance - 5)
                "Брат может не быть другом, но друг - всегда брат."

        "Провести день с самим собой - поиграть в игры / посмотреть сериал":
            if random_event:
                call day_with_yourself from _call_day_with_yourself
            else:
                $ mental_health = change_parameter(mental_health + 5)
                "Откис, но дела сами собой не сделаются."
            $ physical_health = change_parameter(physical_health - 2)
    if workday and month != 'Январь':
        $ studies = change_parameter(studies - 5)
    return


# паттерн физического здоровья
label get_physical_health:
    menu:
        "Заняться спортом"
        "Пойти в качалку":
            if random_event:
                call gym from _call_gym
            else:
                $ physical_health = change_parameter(physical_health + 25)
                $ mental_health = change_parameter(mental_health + 3)
                $ finance = change_parameter(finance - 15)
                "Чувствуешь себя like Boss of the gym!"

        "Пойти на спортплощадку" if month != 'Декабрь' and month != 'Январь':
            if good_weather == False:
                $ physical_health = change_parameter(physical_health + 5)
                $ mental_health = change_parameter(mental_health - 3)
                "Ты толком не позанимался, зря только выходил на улицу."
            elif random_event:
                call sports_ground from _call_sports_ground
            else:
                $ physical_health = change_parameter(physical_health + 15)
                $ mental_health = change_parameter(mental_health + 3)
                "С буквой \"о\" сила, с буквой \"и\" могила!"

        "Покататься на коньках" if month == 'Декабрь' or month == 'Январь':
            if random_event:
                call skating from _call_skating
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
    if workday and month != 'Январь':
        $ studies = change_parameter(studies - 5)

    return


    