# маршуритазор по сессионным вопросам 
label exam:
    if session_counter == 0:
        $ session_counter_limit = 2 
        $ before_exam = "Всем здравствуйте, сегодня ваш первый день сессии. Желаю удачи, хотя она вам не должна понадобиться, если вы учили материал."
        $ after_exam = "Фух, первый день есть, осталось 2. Вроде все написал, но все же не уверен в правильности до конца."
    elif session_counter == 3:
        $ session_counter_limit = 6
        $ before_exam = "Всем здравствуйте, второй день и мы начинаем!"
        $ after_exam = "Справился, большая часть сделана, выходим на финишную прямую!"
    else:
        $ session_counter_limit = 9
        $ before_exam = "Всем здравствуйте, это последний день. Еще есть возможность исправить свои оценки, но учтите она последняя. Так что отнеситесь к этому серьезно! Начинаем."
        $ after_exam = "Ура, я справился, надеюсь. По крайне мере, отмучился на ближайшее время."
    call exam_questions
    
    return

# правильность ответа
label check_session_answer:
    if correct_answer:
        $ mark += 10

    return


# первый день сессии
label exam_questions:
    # "N день экзаменов."
    p "[before_exam]"

    while session_counter <= session_counter_limit:

        $ session_question = player_choice_list[session_counter]
        $ answer_1 = player_choice_dict[player_choice_list[session_counter]][0][0]
        $ answer_2 = player_choice_dict[player_choice_list[session_counter]][1][0]
        $ answer_3 = player_choice_dict[player_choice_list[session_counter]][2][0]
        $ answer_4 = player_choice_dict[player_choice_list[session_counter]][3][0]

        menu:
            "[session_question]" 
            "[answer_1]":
                $ correct_answer = player_choice_dict[player_choice_list[session_counter]][0][1]

            "[answer_2]":
                $ correct_answer = player_choice_dict[player_choice_list[session_counter]][1][1]

            "[answer_3]":
                $ correct_answer = player_choice_dict[player_choice_list[session_counter]][2][1]

            "[answer_4]":
                $ correct_answer = player_choice_dict[player_choice_list[session_counter]][3][1]

        call check_session_answer

        $ session_counter += 1

    # "Конец дня"
    "[after_exam]"

    return

