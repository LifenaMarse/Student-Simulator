# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

# define e = Character('Эйлин', color="#c8ffc8")



# настройка верхней панели
screen info_panel:
    frame:
        padding(80,15)
        xsize 1920
        # ysize 50

        vbox:
            # xsize 1920
            hbox:
                xsize 1920
                text "Учеба: [studies]"      
                text "Финансы: [finance]"     
                text "Ментальное здоровье: [mental_health]"    
                text "Физическое здоровье: [physical_health]"  
                
            hbox:
                text "[week_day]  /  [day]  /  [month]  /  [day_type]  /  погода:  [weather]"



# Игра начинается здесь:
# вступление
label start:
    n'''
    Приветствуем тебя в игре Student Simulator!!! 

    Здесь тебе предстоит прожить семестр жизнью студента. Возможно, ты будешь разочарован, но даже в виртуальном мире тебя ждет учеба, а вместе с ней такая радость жизни любого учащегося высших учебных заведений и не только, как {i}сессия{/i} . 
    {w}Что опять?! {w}Да, но не переживай, все проще, чем кажется, однако слишком не расслабляйся. {w}Но жизнь студентов состоит далеко не только из учебы. {w}Следи также за своим материальным состоянием и не забывай про ментальное и физическое здоровье. 
    {w}И помни, что все связано и переплетено между собой, если где-то убыло, возможно где-то прибыло. {w}И самое главное, все это жизнь, а жизнь как известно не предсказуема, возможно сегодня тебе улыбнется удача, а возможно тебе дорогу перейдет черный кот, ты рассыпишь соль или раздавишь паука и произойдет что-то плохое. {w}Все возможно, поэтому не придавай этому большого значения. 
    
    Ну что, в путь дорогу и удачи на даче!!!
    '''
    nvl hide
    nvl clear


    # первый день
    scene mesi
    with fade

    n'''
    Сегодня первое сентября и твой первый день в университете! 
    
    Ты хорошо сдал все экзамены и смог поступить куда хотел. {w}Сам ты из провинции, но смог поступить в престижный вуз в большом городе, родители определенно тобой гордятся. 
    {w}Правда ты понимаешь, что теперь по большому счету, можешь рассчитывать только на себя. Можно сказать начинается взрослая жизнь.

    И в идеале, чтобы хорошо в ней себя чувствовать, нужно быть образованным. {w}Поэтому ты поступил на факультет...
    '''
    nvl hide
    nvl clear

    menu:       
        "Твой факультет?"         
        "Факультет информационных технологий":
            $ faculty_IT = True
            "Ну а как иначе? Шаришь за hello world, да и считать ты всегда умел, определенно тебе сюда."
        "Факультет медицинских наук":
            $ faculty_medicine = True
            "Как говорится, быть врачом – это призвание!"
        "Факультет гуманитарных наук":
            $ faculty_humanitarian = True
            "Ну а как иначе? Язык хорошо подвешен, любишь читать, знаешь когда крестили Русь, определенно тебе сюда."
    
    "Глобально, чего-то важного или интересного в институте сегодня не было, ты познакомился со своей группой, вас ввели в курс дела по учебе и отпустили на все четыре стороны. Что же, завтра твой первый учебный день, не терпится начать новую жизнь, да?"


    # второй день
    show screen info_panel

    $ week_day = calendar[calendar_counter][0]
    $ day = calendar[calendar_counter][1]
    $ month = calendar[calendar_counter][2]
    $ day_type = calendar[calendar_counter][3]

    '''
    Прямо сейчас в верхней части экрана ты можешь наблюдать окно с наиболее важной и нужной информацией, которая понадобиться тебе для прохождения игры. 
    
    Здесь ты можешь наблюдать 4 параметра: “учеба”, “финансы” “ментальное здоровье” и “физическое здоровье”. {w}Это ключевые параметры, за которыми нужно следить больше всего, если хотя бы один из них опустится до 0, ты проиграешь. 
    
    Далее идет сводка о дне: день недели, число, месяц и погода, это тоже важно и в некоторых ситуациях может сыграть свою роль. 

    Что же, сегодня будний день, а это значит нужно провести его продуктивною, предлагаю пойти в университет. 
    '''
    menu:       
        "Планы на сегодня"         
        "Пойти учиться":
            menu:
                "Пойти учиться"
                "Пойти в универ":
                    $ studies = change_parameter(studies + 10)
                    $ mental_health = change_parameter(mental_health - 5)
                    $ physical_health = change_parameter(physical_health - 3)          
                    "Сегодня ты сходил на пары, молодец!" 

    '''
    Как ты видишь твои действия могут влиять на показатели как положительно, так и отрицательно. 
    
    Также учти, если ты будешь заниматься вне учебной деятельностью в будние дни, это будет отрицательно влиять на твои успехи в учебе, но всегда приходится чем-то жертвовать.
    
    Ты хорошо потрудился сегодня.
    '''
    $ calendar_counter += 1
    "Что ждет тебя завтра?"


    # день три
    $ week_day = calendar[calendar_counter][0]
    $ day = calendar[calendar_counter][1]
    $ month = calendar[calendar_counter][2]
    $ day_type = calendar[calendar_counter][3]
    "Сегодня выходной, предлагаю потратить его с пользой для себя, с показателями ментального и физического здоровья не все в порядке. Оставляю это на твое усмотрение."

    menu:       
        "Планы на сегодня?"         
        "Решать беды с башкой":
            menu:
                "Решать беды с башкой"
                "Пойти к психологу":
                    $ mental_health = change_parameter(mental_health + 30)
                    $ finance = change_parameter(finance - 20)
                    "Так и разориться недолго, но тараканы потихоньку уползают."

                "Пойти гулять с друзьями":
                    $ mental_health = change_parameter(mental_health + 15)
                    $ finance = change_parameter(finance - 5)
                    "Брат может не быть другом, но друг - всегда брат."

                "Провести день с самим собой - поиграть в игры / посмотреть сериал":
                    $ mental_health = change_parameter(mental_health + 5)
                    "Откис, но дела сами собой не сделаются."

        "Заняться спортом":
            menu:
                "Заняться спортом"
                "Пойти в качалку":
                    $ physical_health = change_parameter(physical_health + 25)
                    $ mental_health = change_parameter(mental_health + 3)
                    $ finance = change_parameter(finance - 15)
                    "Чувствуешь себя like Boss of the gym!"

                "Пойти на спортплощадку":
                    $ physical_health = change_parameter(physical_health + 15)
                    $ mental_health = change_parameter(mental_health + 3)
                    "С буквой \"о\" сила, с буквой \"и\" могила!"

                "Позаниматься дома":
                    $ physical_health = change_parameter(physical_health + 5)
                    $ mental_health = change_parameter(mental_health + 1)
                    "Ну ка, где мои гантельки?"

    $ calendar_counter += 1
    "Это было продуктивно. Что подарит новый день?"


    # дегь четыре
    $ week_day = calendar[calendar_counter][0]
    $ day = calendar[calendar_counter][1]
    $ month = calendar[calendar_counter][2]
    $ day_type = calendar[calendar_counter][3]    

    $ good_weather = False 
    $ weather = "плохая"

    "Предлагаю сегодня поднять деньжат, кушать же тоже хочется. {w}Но как ты видишь погода бывает и плохой, это также влияет на некоторые события. Будь осторожен и думай о последствиях."

    menu:       
        "Планы на сегодня"         
        "Пойти работать":
            menu:
                "Пойти работать"
                "Пойти работать в цветочный магазин":
                    $ finance = change_parameter(finance + 10)
                    $ physical_health = change_parameter(physical_health - 5) 
                    "Платят не шибко, но зато красиво."

                "Пойти работать в бар":
                    $ finance = change_parameter(finance + 15)
                    $ physical_health = change_parameter(physical_health - 10) 
                    "Бутылочка бесплатного холодненького темного, самое то под вечер!"

                "Пойти работать строителем":
                    if good_weather:
                        $ finance = change_parameter(finance + 20)
                        $ physical_health = change_parameter(physical_health - 15) 
                        "Тяжко, зато прибыльно."  
                    else:
                        $ finance = change_parameter(finance + 20)
                        $ physical_health = change_parameter(physical_health - 20)
                        $ mental_health = change_parameter(mental_health - 10)
                        "Работать в непогоду под открытым небом - такое себе."

    "Что же, я рассказал тебе все, что ты должен знать и отпускаю тебя в сольное плавание. Вперед к приключениям!"

    $ calendar_counter += 1
    "Что подарит новый день?"

    jump main_game

    return


# основная игра
# label start:
label main_game:
    scene mesi
    with fade # плавный переход
    show screen info_panel

    while calendar_counter <= 122:
        $ week_day = calendar[calendar_counter][0]
        $ day = calendar[calendar_counter][1]
        $ month = calendar[calendar_counter][2]
        $ day_type = calendar[calendar_counter][3]

        if renpy.random.randint(1, 10) <= 6:
            $ good_weather = True
            $ weather = "хорошая"
        else:
            $ good_weather = False
            $ weather = "плохая"
        
        if day_type == 'выходной':
            $ workday = False
            "Сегодня выходной, возможно стоит отдохнуть?"
        else:
            $ workday = True
            "Сегодня будний, пора за работу!"   

        if renpy.random.randint(1, 10) <= 5:
            $ random_event = True
        else:
            $ random_event = False
        
        if calendar[calendar_counter][4]:
            "Вроде говорили, что сегодня на парах должно быть что-то важное. {w}Стоит сходить в универ!"
            $ mini_games_counter += 1



        menu:       
            "Планы на сегодня?"         
            "Пойти учиться":
                call get_studies from _call_get_studies

            "Пойти работать":
                call get_finance from _call_get_finance

            "Решать беды с башкой":
                call get_mental_health from _call_get_mental_health

            "Заняться спортом":
                call get_physical_health from _call_get_physical_health


        if studies == 0 or finance == 0 or mental_health == 0 or physical_health == 0:
            jump bad_end
            # call bad_end

        $ calendar_counter += 1
        "Что подарит новый день?"
        



    if max(studies, finance, mental_health, physical_health) >= 80:
        $ max_parameter = max(studies, finance, mental_health, physical_health)
        jump good_end

    # studies >= 80 or finance >= 80 or mental_health >= 80 or physical_health >= 80:
        


    """
    sas! {w} SoS
    """
    "sbls"



    # scene gorizont
    # with fade



    # $ studies = change_parameter(studies - 20)

    # $ week_day = "Пятница"
    # $ date += 1

    return




# изменетие значений параметров
init python:
    def change_parameter(change):
        if change <= 0:
            return 0
        elif change >= 100:
            return 100
        else:
            return change



# плохие концовки
label bad_end:
    if studies == 0:
        "Кто учиться будет? Ну что, здравствуй небо в облаках, здравствуй юность в сапогах"
    elif finance == 0:
        "Ты нищий, пиздуй на улицу"
    elif mental_health == 0:
        "Депрессия в 0 лет" 
    else:
        "Когда-то и меня вела дорога приключений, а потом мне прострелили колено"

    return





# хорошие концовки
label good_end:
    if studies == max_parameter:
        ""
    elif finance == max_parameter:
        ""
    elif mental_health == max_parameter:
        "" 
    else:
        ""

    return