# готово
label mini_game_medicine_1:
    p "Всем здравствуйте, сегодня у нас новая тема - латинский язык и вот вам сразу вопрос. {w}Какое примерное количество латинских медицинских терминов существует в настоящее время?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Какое примерное количество латинских медицинских терминов существует в настоящее время?"         
        "50 тыс":
            $ correct_answer = False

        "100 тыс":
            $ correct_answer = False

        "500 тыс":
            $ correct_answer = True

        "1 миллион":
            $ correct_answer = False

    call check_answer
        
    p '''
    Латинский язык в биологии можно рассматривать как самостоятельный научный язык, произошедший от латинского языка эпохи Возрождения, но обогащённый множеством слов, заимствованных из древнегреческого и других языков.
    
    Кроме того, многие слова латинского языка употребляются в биологических текстах в новом, специальном смысле. Грамматика в латинском биологическом языке заметно упрощена. Алфавит дополнен: в отличие от классической латыни, используются буквы J, U, W.
    
    Современные Кодексы биологической номенклатуры требуют, чтобы научные названия живых организмов были по форме латинскими, то есть были написаны буквами латинского алфавита и подчинялись правилам латинской грамматики, вне зависимости от того, из какого языка они заимствованы.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово
label mini_game_medicine_2:
    p "Всем здравствуйте, сегодня у нас новая тема - состав атомного ядра и вот вам сразу вопрос. {w}Количество нейтронов в атоме равно?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Количество нейтронов в атоме равно?"         
        "Атомному номеру":
            $ correct_answer = False

        "Количеству электронов":
            $ correct_answer = False

        "Нулю":
            $ correct_answer = False

        "Вычесть атомный номер из атомной массы ":
            $ correct_answer = True

    call check_answer
        
    p '''
    Мы знаем, что масса атома определяется массой ядра. Ядро состоит из протонов и нейтронов, относительные массы которых равны 1. Масса ядра равна сумме масс протонов и нейтронов.

    Число протонов определяем по порядковому номеру элемента. Значит, число нейтронов в ядре можно найти, если от относительной атомной массы отнять порядковый номер.

    Пример: фтор — элемент № 9. Его относительная атомная масса равна 19. В ядре атома фтора — 9 протонов и 19 — 9 = 10 нейтронов.
    '''
    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово
label mini_game_medicine_3:
    p "Всем здравствуйте, сегодня у нас новая тема - изотопы и вот вам сразу вопрос. {w}Чем отличаются изотопы одного элемента?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Чем отличаются изотопы одного элемента?"         
        "Количеством нейтронов":
            $ correct_answer = True

        "Количеством протонов":
            $ correct_answer = False

        "Количеством протонов и нейтронов":
            $ correct_answer = False

        "Зарядом ядра":
            $ correct_answer = False

    call check_answer
        
    show изотопы at truecenter
    p '''
    Атомы с одинаковым количеством протонов, но разным количеством нейтронов называются изотопами. Они обладают практически одинаковыми химическими свойствами, но отличаются по массе и, следовательно, по физическим свойствам.
    
    Существуют стабильные изотопы, которые не излучают радиацию, и нестабильные изотопы, которые излучают радиацию. Последние называются радиоизотопами.
    '''
    hide изотопы

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово
label mini_game_medicine_4:
    p "Всем здравствуйте, сегодня у нас новая тема - химическая связь и вот вам сразу вопрос. {w}Какая химическая связь наименее прочная?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Какая химическая связь наименее прочная?"         
        "Ионная":
            $ correct_answer = False

        "Ковалентная":
            $ correct_answer = False

        "Водородная":
            $ correct_answer = True

        "Металлическая":
            $ correct_answer = False

    call check_answer
        
    p '''
    Химическая связь — взаимодействие атомов, обусловливающее устойчивость молекулы или кристалла как целого. Химическая связь определяется взаимодействием между заряженными частицами.

    Наименее прочная химическая связь является водородная. Но она очень важна и распространена в органических соединениях. Ученые считают, именно водородные связи удерживают вместе две спирали ДНК. 

    Первое издание в котором было упомянуто о водородной связи написано еще в 1939 году Лайнусом Полингом. В 1920 году Латимер и Родебуш дали описание водородной связи в воде.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово
label mini_game_medicine_5:
    p "Всем здравствуйте, сегодня у нас новая тема - ДНК и вот вам сразу вопрос. {w}Назовите функцию ДНК."
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Назовите функцию ДНК"         
        "Транспортирует аминокислоты к рибосоме":
            $ correct_answer = False

        "Хранит генетическую информацию":
            $ correct_answer = True

        "Переносит генетическую информацию к рибосоме":
            $ correct_answer = False

        "Непосредственно участвует в сборке молекул полипептидов":
            $ correct_answer = False

    call check_answer
        
    p '''
    Дезоксирибонуклеиновая кислота — макромолекула, обеспечивающая хранение, передачу из поколения в поколение и реализацию генетической программы развития и функционирования живых организмов.

    Молекула ДНК хранит биологическую информацию в виде генетического кода, состоящего из последовательности нуклеотидов. ДНК содержит информацию о структуре различных видов РНК и белков.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово
label mini_game_medicine_6:
    p "Всем здравствуйте, сегодня у нас новая тема - группы крови и вот вам сразу вопрос. {w}У отца — I группа крови, у матери — IV. Определите группы крови их детей? "
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "У отца — I группа крови, у матери — IV. Определите группы крови их детей? "         
        "только IV":
            $ correct_answer = False

        "I, I, III, IV":
            $ correct_answer = False

        "I или IV":
            $ correct_answer = False

        "II или III":
            $ correct_answer = True

    call check_answer

    show цой at truecenter
    p '''
    Группа крови — генетический обусловленный иммунологический признак крови, который исходя из его сходств и различий у разных индивидов, позволяет подразделять людей на разные группы.

    Группу крови и резус принадлежность наследуется от родителей. Существует 4 группы крови: О, А, В или АВ. Они остаются неизменными в течении всей жизни.
    '''
    hide цой

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово
label mini_game_medicine_7:
    p "Всем здравствуйте, сегодня у нас новая тема - гистогенез и вот вам сразу вопрос. {w}Развитие крови как ткани происходит в..."
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Развитие крови как ткани происходит в..."         
        "Почках":
            $ correct_answer = False

        "Желточном мешке":
            $ correct_answer = True

        "Щитовидной железе":
            $ correct_answer = False

        "Сердце":
            $ correct_answer = False

    call check_answer
        
    p '''
    Гистогенез — совокупность процессов, приводящих к образованию и восстановлению тканей в ходе индивидуального развития. В образовании определенного вида тканей участвует тот или иной зародышевый листок. 
    
    Например, мышечная ткань развивается из мезодермы, нервная — из эктодермы, и т. д. В ряде случаев ткани одного типа могут иметь различное происхождение, например, эпителий кожи имеет эктодермальное, а всасывающий кишечный эпителий — энтодермальное происхождение.

    Гистогенез крови принято называть гемопоэзом. Все клетки крови происходят от единой популяции стволовых кроветворных клеток, которая находится в красном костном мозгу.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово
label mini_game_medicine_8:
    p "Всем здравствуйте, сегодня у нас новая тема - сердечно-cосудистая система и вот вам сразу вопрос. {w}Сердечно-сосудистая система состоит из..."
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Сердечно-сосудистая система состоит из..."         
        "Сердца, артерий, вен, капилляров, венул, артериоло-венулярных анастомозов, лимфатических капилляров, сосудов, протоков":
            $ correct_answer = True

        "Артерии, вен, венул, капилляров, лимфатических капилляров":
            $ correct_answer = False

        "Сердца, лимфатических узлов, вен, капилляров, венул, лимфатических капилляров":
            $ correct_answer = False    

        "Сердца, артерий, вен, лимфатических капилляров, лимфатических сосудов и протоков":
            $ correct_answer = False

    call check_answer
        
    p '''
    Сердечно-cосудистая система — система органов, обеспечивающих циркуляцию крови в организме человека и животных.

    Благодаря её деятельности кислород и питательные вещества доставляются к органам и тканям тела, а углекислый газ, другие продукты метаболизма и отходы жизнедеятельности отводятся от органов и тканей и затем выводятся из организма.

    Сердечно-сосудистая система бывает замкнутая и незамкнутая. У человека, как и у всех позвоночных, она замкнутая.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово
label mini_game_medicine_9:
    p "Всем здравствуйте, сегодня у нас новая тема - скелет и вот вам сразу вопрос. {w}Что не является биологическиой функцией кости как органа?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Что не является биологическиой функцией кости как органа?"         
        "Функция роста":
            $ correct_answer = False

        "Функция Кроветворения":
            $ correct_answer = False

        "Восстановительная функция":
            $ correct_answer = True

        "Защитная функция":
            $ correct_answer = False

    call check_answer
        
    p '''
    Скелет человека — совокупность костей человеческого организма, пассивная часть опорно-двигательного аппарата. Служит опорой мягким тканям, точкой приложения мышц, вместилищем и защитой внутренних органов. Костная ткань скелета развивается из мезенхимы.

    Скелет взрослого человека состоит примерно из 206 костей. Почти все они объединяются в единое целое с помощью суставов, связок и других соединений. 
    
    При рождении человеческий скелет состоит более чем из 300 костей; число костей в зрелом возрасте снижается до 205—208, так как некоторые кости срастаются вместе, преимущественно кости черепа, таза и позвоночника.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово
label mini_game_medicine_10:
    p "Всем здравствуйте, сегодня у нас новая тема - анестезия и вот вам сразу вопрос. {w}Какой врач впервые использовал наркоз?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Какой врач впервые использовал наркоз?"         
        "Склифосовский":
            $ correct_answer = False

        "Мухин":
            $ correct_answer = False

        "Пирогов":
            $ correct_answer = False

        "Мортон":
            $ correct_answer = True

    call check_answer
        
    p '''
    Анестезиология — раздел клинической медицины, занимающийся изучением методов защиты организма от операционной травмы и её последствий, а также от патологических нарушений, 
    
    вызванных непосредственно хирургическим заболеванием, путем управления жизненно важными функциями организма во время операции и в послеоперационном периоде.
    
    16 октября 1846 года был проведен первый в мире наркоз эфиром при операции по удалению поднижнечелюстной опухоли у пациента Гилберта Эббота. В ней приняли участие анестезиолог Уильям Мортон и хирург Джон Уоррен.

    В России эфирный наркоз был впервые применён 7 февраля 1847 года Ф. И. Иноземцевым, а 14 февраля русский учёный и врач Николай Иванович Пирогов впервые применил его для обезболивания при операции.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


