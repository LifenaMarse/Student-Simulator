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
label start:
    show screen info_panel

    # scene bg room
    scene mesi
    with fade # плавный переход

    menu:       
        "Выбор факультета"         
        "IT":
            $ faculty_IT = True
        "Химбио":
            $ faculty_medicine = True
        "Гуманитарий":
            $ faculty_humanitarian = True


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
            "Планы на сегодня"         
            "ГДЗ физкультура 5 класс":
                call get_studies

            "Где деньги взять?":
                call get_finance

            "Беды с башкой":
                call get_mental_health

            "Банки 5 литров":
                call get_physical_health


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