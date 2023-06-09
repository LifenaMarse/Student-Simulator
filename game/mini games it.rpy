# готово 
label mini_game_IT_1:
    p "Всем здравствуйте, сегодня у нас новая тема и вот вам сразу вопрос. {w}Что такое операционная система?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Что такое операционная система?"         
        "Это просто программа на компьютере, как и другие - Word или Chrome.":
            $ correct_answer = False

        "Это показатель того, какой процессор используется на компьютере. Например, 32-битный или 64-битный.":
            $ correct_answer = False

        "Это набор взаимосвязанных программ, осуществляющих управление компьютером и взаимодействие с пользователем.":
            $ correct_answer = True

        "Нет такого понятия, есть понятие \"файловая система\".":
            $ correct_answer = False

    call check_answer from _call_check_answer_10
        
    p '''
    Операционная система — это специальный набор программ, благодаря которому все системы компьютера взаимодействуют как между собой, так и с пользователем.

    Простыми словами, операционная система – это основа, без которой невозможно работать ни с одной программой на компьютере.

    Приложения и сервисы, например, текстовые редакторы, таблицы, интернет-браузеры, базы данных просто не запустятся, если на компьютере не будет ОС.'''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."

    return


# готово 
label mini_game_IT_2:
    p "Всем здравствуйте, сегодня у нас новая тема - комплектующие компьютера и вот вам сразу вопрос. {w}Что такое процессор компьютера?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Что такое процессор компьютера?"         
        "Это блок, внутри которого находится дисковод и много разъемов для монитора, клавиатуры и компьютерной мышки.":
            $ correct_answer = False

        "Это общее название всех комплектующих компьютера.":
            $ correct_answer = False

        "Это суммарный показатель вычислительной мощности компьютера, например 2,7 ГГц.":
            $ correct_answer = False

        "Это элемент компьютера, с помощью которого обрабатывается информация, находящаяся как в собственной памяти, так и в памяти других устройств.":
            $ correct_answer = True

    call check_answer from _call_check_answer_11
        
    p '''
    Процессор – это устройство, отвечающее за обработку информации. Его называют по-разному: центральный процессор, 
    сокращенно ЦП или центральное процессорное устройство, сокращенно ЦПУ или central processing unit, сокращенно CPU. 
    
    Но все эти термины обозначают элемент, который является “мозгом” вычислительного устройства: смартфона, телевизора, компьютера, планшета, фотоаппарата, сервера.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."
    return


# готово 
label mini_game_IT_3:
    p "Всем здравствуйте, сегодня у нас новая тема - компьютерные сети и вот вам сразу вопрос. {w}Что такое IP адрес?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Что такое IP адрес?"         
        "Чем выше IP адрес, тем мощнее компьютер.":
            $ correct_answer = False

        "Это адрес нашего компьютера в интернете.":
            $ correct_answer = True

        "Это наши данные в интернете - имя, адрес, номер телефона.":
            $ correct_answer = False

        "Это мессенджер, как ICQ.":
            $ correct_answer = False

    call check_answer from _call_check_answer_12
        
    p '''
    IP-адрес — уникальный числовой идентификатор устройства в компьютерной сети, работающей по протоколу IP.

    В сети Интернет требуется глобальная уникальность адреса; в случае работы в локальной сети требуется уникальность адреса в пределах сети. 
    
    В версии протокола IPv4 IP-адрес имеет длину 4 байта, а в версии протокола IPv6 — 16 байт.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."
    return


# готово 
label mini_game_IT_4:
    p "Всем здравствуйте, сегодня у нас новая тема - введение в программирование и вот вам сразу вопрос. {w}Чем отличается IDE и простой текстовый редактор?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Чем отличается IDE и простой текстовый редактор?"   
        "IDE - это программа, включающая в себя не только текстовый редактор, но и другие необходимые для разработки программы.":
            $ correct_answer = True      
        "IDE - это подвид текстовых редакторов, способных еще и работать с графикой.":
            $ correct_answer = False

        "IDE - это один из видов текстовых редакторов, как Блокнот или Word.":
            $ correct_answer = False

        "IDE - это графический редактор, а не текстовый.":
            $ correct_answer = False

    call check_answer from _call_check_answer_13
        
    p '''
    Интегрированная среда разработки или IDE — комплекс программных средств, используемый программистами для разработки программного обеспечения.

    Среда разработки включает в себя: текстовый редактор, компилятор и/или интерпретатор, средства автоматизации сборки.
    
    Иногда содержит также средства для интеграции с системами управления версиями и разнообразные инструменты для упрощения конструирования графического интерфейса пользователя.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."
    return


# готово 
label mini_game_IT_5:
    p "Всем здравствуйте, сегодня у нас новая тема - языки программирования и вот вам сразу вопрос. {w}Один из самых популярных и прогрессирующих языков программирования последних лет?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Один из самых популярных и прогрессирующих языков программирования последних лет?"         
        "Java":
            $ correct_answer = False

        "C++":
            $ correct_answer = False

        "Python":
            $ correct_answer = True

        "Pascal":
            $ correct_answer = False

    call check_answer from _call_check_answer_14
        
    p '''
    Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью.

    Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации.
 
    Недостатками языка являются более низкая скорость работы и более высокое потребление памяти написанных на нём программ.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."
    return


# готово 
label mini_game_IT_6:
    p "Всем здравствуйте, сегодня у нас новая тема - парадигмы программирования и вот вам сразу вопрос. {w}Как расшифровывается ООП?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Как расшифровывается ООП?"         
        "Основы объектного программирования":
            $ correct_answer = False

        "Отладка опенсорс проектов":
            $ correct_answer = False

        "Основные опорные программы":
            $ correct_answer = False

        "Объектно-ориентированное программирование":
            $ correct_answer = True

    call check_answer from _call_check_answer_15
        
    p '''
    Объектно-ориентированное программирование — методология программирования, основанная на представлении программы в виде совокупности взаимодействующих объектов, 

    каждый из которых является экземпляром определённого класса, а классы образуют иерархию наследования.

    Идеологически, ООП — подход к программированию как к моделированию информационных объектов, решающий на новом уровне основную задачу структурного программирования:

    структурирование информации с точки зрения управляемости, что существенно улучшает управляемость самим процессом моделирования, что, в свою очередь, особенно важно при реализации крупных проектов.
    '''
    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."
    return


# готово 
label mini_game_IT_7:
    p "Всем здравствуйте, сегодня у нас новая тема - сложность алгоритмов и вот вам сразу вопрос. {w}что означает выражение f(n)=x(g(n)), если вместо x подставить О-символику: o, O, Θ?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "что означает выражение f(n)=x(g(n)), если вместо x подставить О-символику: o, O, Θ?"         
        "f(n)<g(n) при O, f(n)<=g(n) при o, f(n)≈g(n) при Θ":
            $ correct_answer = False

        "f(n)<g(n) при o, f(n)<=g(n) при O, f(n)≈g(n) при Θ":
            $ correct_answer = True

        "f(n)<g(n) при Θ, f(n)<=g(n) при O, f(n)≈g(n) при o":
            $ correct_answer = False

        "o, O, Θ означают одно и то же, это просто разные варианты написания":
            $ correct_answer = False

    call check_answer from _call_check_answer_16
        
    p '''
    Сложность алгоритмов обычно оценивают по времени выполнения или по используемой памяти. В обоих случаях сложность зависит от размеров входных данных: массив из 100 элементов будет обработан быстрее, чем аналогичный из 1000.
    
    При этом точное время мало кого интересует: оно зависит от процессора, типа данных, языка программирования и множества других параметров. 
    
    Важна лишь асимптотическая сложность, т. е. сложность при стремлении размера входных данных к бесконечности.
    '''
    show буквенные обозначения at truecenter
    p '''
    Вот небольшая грамотка по буквенной символики.

    Рекомендую вам запомнить эту информацию!
    '''
    hide буквенные обозначения

    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."
    return


# готово 
label mini_game_IT_8:
    p "Всем здравствуйте, сегодня у нас новая тема - системы счисления и вот вам сразу вопрос. {w}Что получится при переводе 11010101 из двоичной в десятичную систему счисления?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Число 11010101 из двоичной в десятичную систему счисления?"         
        "5":
            $ correct_answer = False

        "14":
            $ correct_answer = False

        "213":
            $ correct_answer = True

        "53":
            $ correct_answer = False

    call check_answer from _call_check_answer_17
        
    p '''
    Система счисления — символический метод записи чисел, представление чисел с помощью письменных знаков.

    Система счисления: даёт представления множества чисел; даёт каждому числу уникальное представление; отражает алгебраическую и арифметическую структуру чисел.
    
    Преобразовать число из двоичной системы счисления в десятичную можно следующим образом: каждый разряд числа необходимо умножить на 2^n, где n - номер разряда, начиная с 0. Затем суммировать полученные значения.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."
    return


# готово 
label mini_game_IT_9:
    show таблица истинности at truecenter
    p "Всем здравствуйте, сегодня у нас новая тема - алгебра логики и вот вам сразу вопрос. {w}Какому логическому выражению соответствует указанная таблица истинности?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Какому логическому выражению соответствует указанная таблица истинности?"     
        "НЕ (А & B)":
            $ correct_answer = True

        "A v B":
            $ correct_answer = False

        "НЕ (А) & НЕ (B)":
            $ correct_answer = False

        "А & B":
            $ correct_answer = False

    call check_answer from _call_check_answer_18
    hide таблица истинности
        
    p '''
    Алгебра логики — раздел математической логики, в котором изучаются логические операции над высказываниями. Чаще всего предполагается, что высказывания могут быть только истинными или ложными, используется бинарная или двоичная логика.

    Основные операции: ¬ - отрицание, ∧ - конъюнкция, ∨ - дизъюнкция.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."
    return


# готово 
label mini_game_IT_10:
    p "Всем здравствуйте, сегодня у нас новая тема - комплексные числа и вот вам сразу вопрос. {w}Чему равен квадрат мнимой единице комплексного числа i^2?"
    "У тебя в голове всплывает несколько вариантов ответов и ты решаешь ответить на вопрос."
    menu:
        "Чему равен квадрат мнимой единице комплексного числа i^2?"         
        "1":
            $ correct_answer = False

        "-1":
            $ correct_answer = True

        "0":
            $ correct_answer = False

        "i нельзя возвести в квадрат":
            $ correct_answer = False

    call check_answer from _call_check_answer_19
        
    p '''
    Комплексные числа — числа вида a + bi, где a, b — вещественные числа, i — мнимая единица, то есть число, для которого выполняется равенство: i^2 = -1.

    Множество комплексных чисел обычно обозначается символом C. Вещественные числа можно рассматривать как частный случай комплексных, они имеют вид a + 0i. 
    
    Главное свойство C — в нём выполняется основная теорема алгебры, то есть любой многочлен n-й степени при n>=1 имеет n корней.
    '''

    p "Рекомендую вам запомнить эту информацию!"
    "Хорошо, что я сходил на пары, вероятно полученные знания могут мне пригодиться в будущем! {w}Ну ладно, пора домой."
    return

