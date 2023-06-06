# маршрутизатор по IT вопросам
label mini_games_IT:
    if mini_games_counter == 1:
        call mini_game_IT_1
    elif mini_games_counter == 2:
        call mini_game_IT_2
    elif mini_games_counter == 3:
        call mini_game_IT_3
    elif mini_games_counter == 4:
        call mini_game_IT_4
    elif mini_games_counter == 5:
        call mini_game_IT_5
    elif mini_games_counter == 6:
        call mini_game_IT_6
    elif mini_games_counter == 7:
        call mini_game_IT_7
    elif mini_games_counter == 8:
        call mini_game_IT_8
    elif mini_games_counter == 9:
        call mini_game_IT_9
    else:
        call mini_game_IT_10
    return


# маршрутизатор по химбио вопросам
label mini_games_medicine:
    if mini_games_counter == 1:
        call mini_game_medicine_1
    elif mini_games_counter == 2:
        call mini_game_medicine_2
    elif mini_games_counter == 3:
        call mini_game_medicine_3
    elif mini_games_counter == 4:
        call mini_game_medicine_4
    elif mini_games_counter == 5:
        call mini_game_medicine_5
    elif mini_games_counter == 6:
        call mini_game_medicine_6
    elif mini_games_counter == 7:
        call mini_game_medicine_7
    elif mini_games_counter == 8:
        call mini_game_medicine_8
    elif mini_games_counter == 9:
        call mini_game_medicine_9
    else:
        call mini_game_medicine_10
    return


# маршрутизатор по гуманитарным вопросам
label mini_games_humanitarian:
    if mini_games_counter == 1:
        call mini_game_humanitarian_1
    elif mini_games_counter == 2:
        call mini_game_humanitarian_2
    elif mini_games_counter == 3:
        call mini_game_humanitarian_3
    elif mini_games_counter == 4:
        call mini_game_humanitarian_4
    elif mini_games_counter == 5:
        call mini_game_humanitarian_5
    elif mini_games_counter == 6:
        call mini_game_humanitarian_6
    elif mini_games_counter == 7:
        call mini_game_humanitarian_7
    elif mini_games_counter == 8:
        call mini_game_humanitarian_8
    elif mini_games_counter == 9:
        call mini_game_humanitarian_9
    else:
        call mini_game_humanitarian_10
    return


# проверка правильности ответа
label check_answer:
    if correct_answer:
        $ studies = change_parameter(studies + 5)
        p "Да, абсолютно правильно!"
    else:
        $ mental_health = change_parameter(mental_health - 5)
        p "Нет, это неверно!"
    return
