import telebot
import speech_recognition as SRG
from modules import config
from telebot import types
from pydub import AudioSegment

bot = telebot.TeleBot(config.TOKEN)

# start


@bot.message_handler(commands=["start"])
def start(message):
    if message.from_user.id == config.AdminTelegramID:
        bot.send_message(message.chat.id, f"Приветствую тебя хозяин")
        with open("stikers/KitayPartiya.webp", "rb") as sticker:
            bot.send_sticker(message.chat.id, sticker)
    else:
        if message.from_user.last_name is None:
            bot.send_message(
                message.chat.id, f"Привет {message.from_user.first_name}")

        else:
            bot.send_message(
                message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}")
        help(message)


# help
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, """
/start - Запуск/Перезапуск бота
/help - Помощь
/diary - Дневник ученика

На какие вопросы я могу ответить:
Какое расписание уроков у 11 2/11 1
Какое расписание звонков
Какое расписание элективов
Кто не учится в субботу
Как зовут директора школы
Какой адрес школы
Какой номер телефона школы
Какое расписание ЕГЭ
""")
    bot.send_message(
        message.chat.id, f"Если у тебя другой вопрос, отзыв или предложение, то напиши моему хозяину {config.owners_profile}")
    bot.send_message(
        message.chat.id, f"Автор: не забудь поблагодарить моего бота )")


# speech recognition
def recognise(filename):
    language = 'ru_RU'
    r = SRG.Recognizer()

    with SRG.AudioFile(filename) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language=language)
            return text
        except:
            return "Ошибка, попробуйте снова"


# diary func
# view grades of chosen subject
def view_grade(call, subject):
    if subject == "informatics":
        inf_menu = types.InlineKeyboardMarkup(row_width=1)
        inf_menu_button1 = types.InlineKeyboardButton(
            "Посмотреть оценки", callback_data="view_grade_of_informatics")
        inf_menu_button2 = types.InlineKeyboardButton(
            "Изменить оценки", callback_data="change_grade_of_informatics")
        inf_menu_button3 = types.InlineKeyboardButton(
            "Назад", callback_data="main_menu")
        inf_menu.add(inf_menu_button1, inf_menu_button2, inf_menu_button3)

        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="informatics")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_inf.txt", 'r') as inf_file:
            user_inf_grades = inf_file.read().split("\n")

        answer = ''
        for i in user_inf_grades:
            if i == "5" or i == "4" or i == "3" or i == "2" or i == "1":
                answer = answer + i + "\n"

        if answer.count("5") > 0 or answer.count("4") > 0 or answer.count("3") > 0 or answer.count("2") > 0 or answer.count("1") > 0:

            sum_of_average = (answer.count("5") * 5 + answer.count("4") * 4 + answer.count("3") * 3 + answer.count(
                "2") * 2 + answer.count("1") * 1)
            len_of_average = (
                answer.count("5") + answer.count("4") + answer.count("3") + answer.count("2") + answer.count("1"))
            if len_of_average == 0:
                len_of_average = 1
            average = sum_of_average / len_of_average

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Ваши оценки по информатике:\n{answer}Средне арихметическая оценка: {str(average)[:4]}",
                                  reply_markup=back_menu)

        elif answer.count("5") == 0 and answer.count("4") == 0 and answer.count("3") == 0 and answer.count("2") == 0 and answer.count("1") == 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Информатика: Ваш список оценок пуст", reply_markup=back_menu)

    elif subject == "mathematics":
        mat_menu = types.InlineKeyboardMarkup(row_width=1)
        mat_menu_button1 = types.InlineKeyboardButton(
            "Посмотреть оценки", callback_data="view_grade_of_mathematics")
        mat_menu_button2 = types.InlineKeyboardButton(
            "Изменить оценки", callback_data="change_grade_of_mathematics")
        mat_menu_button3 = types.InlineKeyboardButton(
            "Назад", callback_data="main_menu")
        mat_menu.add(mat_menu_button1, mat_menu_button2, mat_menu_button3)

        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="mathematics")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_mat.txt", 'r') as mat_file:
            user_mat_grades = mat_file.read().split("\n")

        answer = ''
        for i in user_mat_grades:
            if i == "5" or i == "4" or i == "3" or i == "2" or i == "1":
                answer = answer + i + "\n"

        if answer.count("5") > 0 or answer.count("4") > 0 or answer.count("3") > 0 or answer.count("2") > 0 or answer.count("1") > 0:

            sum_of_average = (answer.count("5") * 5 + answer.count("4") * 4 + answer.count("3") * 3 + answer.count(
                "2") * 2 + answer.count("1") * 1)
            len_of_average = (
                answer.count("5") + answer.count("4") + answer.count("3") + answer.count("2") + answer.count("1"))
            if len_of_average == 0:
                len_of_average = 1
            average = sum_of_average / len_of_average

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Ваши оценки по математике:\n{answer}Средне арихметическая оценка: {str(average)[:4]}",
                                  reply_markup=back_menu)

        elif answer.count("5") == 0 and answer.count("4") == 0 and answer.count("3") == 0 and answer.count("2") == 0 and answer.count("1") == 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Математика: Ваш список оценок пуст", reply_markup=back_menu)

    elif subject == "english":
        eng_menu = types.InlineKeyboardMarkup(row_width=1)
        eng_menu_button1 = types.InlineKeyboardButton(
            "Посмотреть оценки", callback_data="view_grade_of_english")
        eng_menu_button2 = types.InlineKeyboardButton(
            "Изменить оценки", callback_data="change_grade_of_english")
        eng_menu_button3 = types.InlineKeyboardButton(
            "Назад", callback_data="main_menu")
        eng_menu.add(eng_menu_button1, eng_menu_button2, eng_menu_button3)

        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="english")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_eng.txt", 'r') as eng_file:
            eng_grades = eng_file.read().split("\n")

        answer = ''
        for i in eng_grades:
            if i == "5" or i == "4" or i == "3" or i == "2" or i == "1":
                answer = answer + i + "\n"

        if answer.count("5") > 0 or answer.count("4") > 0 or answer.count("3") > 0 or answer.count("2") > 0 or answer.count("1") > 0:

            sum_of_average = (answer.count("5") * 5 + answer.count("4") * 4 + answer.count("3") * 3 + answer.count(
                "2") * 2 + answer.count("1") * 1)
            len_of_average = (
                answer.count("5") + answer.count("4") + answer.count("3") + answer.count("2") + answer.count("1"))
            if len_of_average == 0:
                len_of_average = 1
            average = sum_of_average / len_of_average

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Ваши оценки по английскому языку:\n{answer}Средне арихметическая оценка: {str(average)[:4]}",
                                  reply_markup=back_menu)

        elif answer.count("5") == 0 and answer.count("4") == 0 and answer.count("3") == 0 and answer.count("2") == 0 and answer.count("1") == 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Английский язык: Ваш список оценок пуст", reply_markup=back_menu)

    elif subject == "russian":
        rus_menu = types.InlineKeyboardMarkup(row_width=1)
        rus_menu_button1 = types.InlineKeyboardButton(
            "Посмотреть оценки", callback_data="view_grade_of_english")
        rus_menu_button2 = types.InlineKeyboardButton(
            "Изменить оценки", callback_data="change_grade_of_english")
        rus_menu_button3 = types.InlineKeyboardButton(
            "Назад", callback_data="main_menu")
        rus_menu.add(rus_menu_button1, rus_menu_button2, rus_menu_button3)

        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="russian")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_rus.txt", 'r') as rus_file:
            user_rus_grades = rus_file.read().split("\n")

        answer = ''
        for i in user_rus_grades:
            if i == "5" or i == "4" or i == "3" or i == "2" or i == "1":
                answer = answer + i + "\n"

        if answer.count("5") > 0 or answer.count("4") > 0 or answer.count("3") > 0 or answer.count("2") > 0 or answer.count("1") > 0:

            sum_of_average = (answer.count("5") * 5 + answer.count("4") * 4 + answer.count("3") * 3 + answer.count(
                "2") * 2 + answer.count("1") * 1)
            len_of_average = (
                answer.count("5") + answer.count("4") + answer.count("3") + answer.count("2") + answer.count("1"))
            if len_of_average == 0:
                len_of_average = 1
            average = sum_of_average / len_of_average

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Ваши оценки по русскому языку:\n{answer}Средне арихметическая оценка: {str(average)[:4]}",
                                  reply_markup=back_menu)

        elif answer.count("5") == 0 and answer.count("4") == 0 and answer.count("3") == 0 and answer.count("2") == 0 and answer.count("1") == 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Русский язык: Ваш список оценок пуст", reply_markup=back_menu)


# add grades of chosen subject
def add_grade(call, subject, grade):
    if subject == "inf":
        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="informatics")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_inf.txt", "a") as inf_file:
            inf_file.write(grade+"\n")

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Информатика: оценка успешно добавлена", reply_markup=back_menu)
        bot.answer_callback_query(call.id, text='')

    elif subject == "mat":
        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="mathematics")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_mat.txt", "a") as mat_file:
            mat_file.write(grade+"\n")

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Математика: оценка успешно добавлена", reply_markup=back_menu)
        bot.answer_callback_query(call.id, text='')

    elif subject == "eng":
        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="english")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_eng.txt", "a") as eng_file:
            eng_file.write(grade+"\n")

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Английский язык: оценка успешно добавлена", reply_markup=back_menu)
        bot.answer_callback_query(call.id, text='')

    elif subject == "rus":
        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="russian")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_rus.txt", "a") as rus_file:
            rus_file.write(grade+"\n")

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Русский язык: оценка успешно добавлена", reply_markup=back_menu)
        bot.answer_callback_query(call.id, text='')


# remove grades of chosen subject
def remove_grade(call, subject):
    if subject == "inf":
        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="informatics")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_inf.txt", "r") as inf_file:
            inf_file_to_remove_last = inf_file.read().split("\n",)

        if inf_file_to_remove_last[-1] == "5" \
                or inf_file_to_remove_last[-1] == "4" \
                or inf_file_to_remove_last[-1] == "3" \
                or inf_file_to_remove_last[-1] == "2" \
                or inf_file_to_remove_last[-1] == "1":
            del inf_file_to_remove_last[-1]  # Удаление последнего элемента
        else:
            # Удаление последнего элемента (пустой строки или лишнего символа)
            del inf_file_to_remove_last[-1]
            del inf_file_to_remove_last[-1]  # Удаление "последнего" элемента

        with open(f"users_list/{call.from_user.id}_inf.txt", "w") as inf_file:
            for i in inf_file_to_remove_last:
                inf_file.writelines(i + "\n")

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Информатика: последняя оценка успешно удалена", reply_markup=back_menu)
        bot.answer_callback_query(call.id, text='')

    elif subject == "mat":
        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="mathematics")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_mat.txt", "r") as mat_file:
            mat_file_to_remove_last = mat_file.read().split("\n",)

        if mat_file_to_remove_last[-1] != "":
            del mat_file_to_remove_last[-1]  # Удаление последнего элемента
        else:
            # Удаление последнего элемента (пустой строки)
            del mat_file_to_remove_last[-1]
            del mat_file_to_remove_last[-1]  # Удаление "последнего" элемента

        with open(f"users_list/{call.from_user.id}_mat.txt", "w") as mat_file:
            for i in mat_file_to_remove_last:
                mat_file.writelines(i + "\n")

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Информатика: последняя оценка успешно удалена", reply_markup=back_menu)
        bot.answer_callback_query(call.id, text='')

    elif subject == "eng":
        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="english")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_eng.txt", "r") as eng_file:
            eng_file_to_remove_last = eng_file.read().split("\n",)

        if eng_file_to_remove_last[-1] != "":
            del eng_file_to_remove_last[-1]  # Удаление последнего элемента
        else:
            # Удаление последнего элемента (пустой строки)
            del eng_file_to_remove_last[-1]
            del eng_file_to_remove_last[-1]  # Удаление "последнего" элемента

        with open(f"users_list/{call.from_user.id}_eng.txt", "w") as eng_file:
            for i in eng_file_to_remove_last:
                eng_file.writelines(i + "\n")

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Информатика: последняя оценка успешно удалена", reply_markup=back_menu)
        bot.answer_callback_query(call.id, text='')

    elif subject == "rus":
        back_menu = types.InlineKeyboardMarkup(row_width=1)
        back_menu_button1 = types.InlineKeyboardButton(
            "Назад", callback_data="russian")
        back_menu.add(back_menu_button1)

        with open(f"users_list/{call.from_user.id}_rus.txt", "r") as rus_file:
            rus_file_to_remove_last = rus_file.read().split("\n",)

        if rus_file_to_remove_last[-1] != "":
            del rus_file_to_remove_last[-1]  # Удаление последнего элемента
        else:
            # Удаление последнего элемента (пустой строки)
            del rus_file_to_remove_last[-1]
            del rus_file_to_remove_last[-1]  # Удаление "последнего" элемента

        with open(f"users_list/{call.from_user.id}_rus.txt", "w") as rus_file:
            for i in rus_file_to_remove_last:
                rus_file.writelines(i + "\n")

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Информатика: последняя оценка успешно удалена", reply_markup=back_menu)
        bot.answer_callback_query(call.id, text='')


# diary main command
@bot.message_handler(commands=["diary"])
def diary(message):
    main_menu = types.InlineKeyboardMarkup(row_width=1)
    main_menu_button1 = types.InlineKeyboardButton(
        'Информатика', callback_data='informatics')
    main_menu_button2 = types.InlineKeyboardButton(
        'Математика', callback_data='mathematics')
    main_menu_button3 = types.InlineKeyboardButton(
        'Английский язык', callback_data='english')
    main_menu_button4 = types.InlineKeyboardButton(
        'Русский язык', callback_data='russian')
    main_menu.add(main_menu_button1, main_menu_button2,
                  main_menu_button3, main_menu_button4)

    bot.send_message(
        message.chat.id, f"Дневник {message.from_user.first_name}")
    bot.send_message(message.chat.id, "Выберите предмет",
                     reply_markup=main_menu)

    with open(f"users_list/{message.from_user.id}_inf.txt", 'w') as inf_file:
        inf_file.write("")
    with open(f"users_list/{message.from_user.id}_mat.txt", 'w') as mat_file:
        mat_file.write("")
    with open(f"users_list/{message.from_user.id}_eng.txt", 'w') as eng_file:
        eng_file.write("")
    with open(f"users_list/{message.from_user.id}_rus.txt", 'w') as rus_file:
        rus_file.write("")


# Text tracking
@bot.message_handler(content_types=["text"])
def text_tracking(message):
    if message.text.lower() in config.helloWords:
        bot.send_message(message.chat.id, f"""
И тебе привет 😉
Что хочешь узнать?""")
        help(message)
    if message.text.lower() in config.helpWords:
        help(message)

    if message.text.lower() in config.whoIsYourOwner:
        bot.send_message(
            message.chat.id, "Самсонов Евгений (@SamsonovEugene) мой хозяин ")

    if message.text.lower() in config.TimelineWords:
        bot.send_message(message.chat.id, config.TimelineForLessons)

    if message.text.lower() in config.lessonScheduleWordsFor11_2:
        bot.send_message(message.chat.id, config.lessonScheduleFor11_2)

    if message.text.lower() in config.lessonScheduleWordsFor11_1:
        bot.send_message(message.chat.id, config.lessonScheduleFor11_1)

    if message.text.lower() in config.whoDoesntStudyOnSaturday:
        bot.send_message(message.chat.id, """
В субботу не учаться ученики начальных классов (1-4),
Все остальные (5-11) классы в субботу учаться (""")

    if message.text.lower() in config.whatDirectorNameWords:
        bot.send_message(
            message.chat.id, f"Директора школы зовут {config.director_name}")

    if message.text.lower() in config.whatAddressOfSchoolWords:
        bot.send_message(message.chat.id, "Ирчи Казака 126 г")

    if message.text.lower() in config.thanksWords:
        bot.send_message(message.chat.id, "Всегда пожалуйста ;)")

    if message.text.lower() in config.electivesScheduleWords:
        bot.send_message(message.chat.id, config.electivesSchedule)

    if message.text.lower() in config.listOfEGEWords:
        bot.send_message(message.chat.id, config.listOfEGE)

    if message.text.lower() in config.whatPhoneNuberOfSchoolWords:
        bot.send_message(
            message.chat.id, "Номер телефона школы: +7 (8722) 62-63-93")


# callback
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'main_menu':
        main_menu = types.InlineKeyboardMarkup(row_width=1)
        main_menu_button1 = types.InlineKeyboardButton(
            'Информатика', callback_data='informatics')
        main_menu_button2 = types.InlineKeyboardButton(
            'Математика', callback_data='mathematics')
        main_menu_button3 = types.InlineKeyboardButton(
            'Английский язык', callback_data='english')
        main_menu_button4 = types.InlineKeyboardButton(
            'Русский язык', callback_data='russian')
        main_menu.add(main_menu_button1, main_menu_button2,
                      main_menu_button3, main_menu_button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите предмет",
                              reply_markup=main_menu)

    elif call.data == 'informatics':
        inf_menu = types.InlineKeyboardMarkup(row_width=1)
        inf_menu_button1 = types.InlineKeyboardButton(
            "Посмотреть оценки", callback_data="view_grade_of_informatics")
        inf_menu_button2 = types.InlineKeyboardButton(
            "Изменить оценки", callback_data="change_grade_of_informatics")
        inf_menu_button3 = types.InlineKeyboardButton(
            "Назад", callback_data="main_menu")
        inf_menu.add(inf_menu_button1, inf_menu_button2, inf_menu_button3)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Информатика: Выберите действие", reply_markup=inf_menu)

    elif call.data == 'mathematics':
        mat_menu = types.InlineKeyboardMarkup(row_width=1)
        mat_menu_button1 = types.InlineKeyboardButton(
            "Посмотреть оценки", callback_data="view_grade_of_mathematics")
        mat_menu_button2 = types.InlineKeyboardButton(
            "Изменить оценки", callback_data="change_grade_of_mathematics")
        mat_menu_button3 = types.InlineKeyboardButton(
            "Назад", callback_data="main_menu")
        mat_menu.add(mat_menu_button1, mat_menu_button2, mat_menu_button3)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Математика: Выберите действие",
                              reply_markup=mat_menu)

    elif call.data == 'english':
        eng_menu = types.InlineKeyboardMarkup(row_width=1)
        eng_menu_button1 = types.InlineKeyboardButton(
            "Посмотреть оценки", callback_data="view_grade_of_english")
        eng_menu_button2 = types.InlineKeyboardButton(
            "Изменить оценки", callback_data="change_grade_of_english")
        eng_menu_button3 = types.InlineKeyboardButton(
            "Назад", callback_data="main_menu")
        eng_menu.add(eng_menu_button1, eng_menu_button2, eng_menu_button3)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Английский язык: Выберите действие",
                              reply_markup=eng_menu)

    elif call.data == 'russian':
        rus_menu = types.InlineKeyboardMarkup(row_width=1)
        rus_menu_button1 = types.InlineKeyboardButton(
            "Посмотреть оценки", callback_data="view_grade_of_russian")
        rus_menu_button2 = types.InlineKeyboardButton(
            "Изменить оценки", callback_data="change_grade_of_russian")
        rus_menu_button3 = types.InlineKeyboardButton(
            "Назад", callback_data="main_menu")
        rus_menu.add(rus_menu_button1, rus_menu_button2, rus_menu_button3)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Русский язык: Выберите действие",
                              reply_markup=rus_menu)

    elif call.data == 'view_grade_of_informatics' \
            or call.data == 'view_grade_of_mathematics' \
            or call.data == 'view_grade_of_english' \
            or call.data == 'view_grade_of_russian':
        if call.data == 'view_grade_of_informatics':
            view_grade(call, "informatics")

        elif call.data == 'view_grade_of_mathematics':
            view_grade(call, "mathematics")

        elif call.data == 'view_grade_of_english':
            view_grade(call, "english")

        elif call.data == 'view_grade_of_russian':
            view_grade(call, "russian")

    elif call.data == "change_grade_of_informatics" \
            or call.data == "change_grade_of_mathematics" \
            or call.data == "change_grade_of_english" \
            or call.data == "change_grade_of_russian":
        if call.data == "change_grade_of_informatics":
            inf_cg_menu = types.InlineKeyboardMarkup(row_width=2)
            inf_cg_button1 = types.InlineKeyboardButton(
                "Добавить оценку", callback_data="add_grade_for_informatics")
            inf_cg_button2 = types.InlineKeyboardButton(
                "Удалить оценку", callback_data="remove_grade_for_informatics")
            inf_cg_button3 = types.InlineKeyboardButton(
                "Назад", callback_data="informatics")
            inf_cg_menu.add(inf_cg_button1, inf_cg_button2, inf_cg_button3)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Информатика: выберите действие:",
                                  reply_markup=inf_cg_menu)

        elif call.data == "change_grade_of_mathematics":
            mat_cg_menu = types.InlineKeyboardMarkup(row_width=2)
            mat_cg_button1 = types.InlineKeyboardButton(
                "Добавить оценку", callback_data="add_grade_for_mathematics")
            mat_cg_button2 = types.InlineKeyboardButton(
                "Удалить оценку", callback_data="remove_grade_for_mathematics")
            mat_cg_button3 = types.InlineKeyboardButton(
                "Назад", callback_data="mathematics")
            mat_cg_menu.add(mat_cg_button1, mat_cg_button2, mat_cg_button3)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Математика: выберите действие:",
                                  reply_markup=mat_cg_menu)

        elif call.data == "change_grade_of_english":
            eng_cg_menu = types.InlineKeyboardMarkup(row_width=2)
            eng_cg_button1 = types.InlineKeyboardButton(
                "Добавить оценку", callback_data="add_grade_for_english")
            eng_cg_button2 = types.InlineKeyboardButton(
                "Удалить оценку", callback_data="remove_grade_for_english")
            eng_cg_button3 = types.InlineKeyboardButton(
                "Назад", callback_data="english")
            eng_cg_menu.add(eng_cg_button1, eng_cg_button2, eng_cg_button3)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Английский язык: выберите действие:",
                                  reply_markup=eng_cg_menu)

        elif call.data == "change_grade_of_russian":
            rus_cg_menu = types.InlineKeyboardMarkup(row_width=2)
            rus_cg_button1 = types.InlineKeyboardButton(
                "Добавить оценку", callback_data="add_grade_for_russian")
            rus_cg_button2 = types.InlineKeyboardButton(
                "Удалить оценку", callback_data="remove_grade_for_russian")
            rus_cg_button3 = types.InlineKeyboardButton(
                "Назад", callback_data="russian")
            rus_cg_menu.add(rus_cg_button1, rus_cg_button2, rus_cg_button3)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Русский язык: выберите действие:",
                                  reply_markup=rus_cg_menu)

    elif call.data == "add_grade_for_informatics" \
            or call.data == "add_grade_for_mathematics" \
            or call.data == "add_grade_for_english" \
            or call.data == "add_grade_for_russian":
        if call.data == "add_grade_for_informatics":
            list_of_grades_menu = types.InlineKeyboardMarkup(row_width=5)
            list_of_grades_button1 = types.InlineKeyboardButton(
                "1", callback_data="grade_1_inf")
            list_of_grades_button2 = types.InlineKeyboardButton(
                "2", callback_data="grade_2_inf")
            list_of_grades_button3 = types.InlineKeyboardButton(
                "3", callback_data="grade_3_inf")
            list_of_grades_button4 = types.InlineKeyboardButton(
                "4", callback_data="grade_4_inf")
            list_of_grades_button5 = types.InlineKeyboardButton(
                "5", callback_data="grade_5_inf")
            list_of_grades_button6 = types.InlineKeyboardButton(
                "Назад", callback_data="informatics")
            list_of_grades_menu.add(list_of_grades_button1, list_of_grades_button2, list_of_grades_button3,
                                    list_of_grades_button4, list_of_grades_button5, list_of_grades_button6)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Информатика: какую оценку добавить?", reply_markup=list_of_grades_menu)

        elif call.data == "add_grade_for_mathematics":
            list_of_grades_menu = types.InlineKeyboardMarkup(row_width=5)
            list_of_grades_button1 = types.InlineKeyboardButton(
                "1", callback_data="grade_1_mat")
            list_of_grades_button2 = types.InlineKeyboardButton(
                "2", callback_data="grade_2_mat")
            list_of_grades_button3 = types.InlineKeyboardButton(
                "3", callback_data="grade_3_mat")
            list_of_grades_button4 = types.InlineKeyboardButton(
                "4", callback_data="grade_4_mat")
            list_of_grades_button5 = types.InlineKeyboardButton(
                "5", callback_data="grade_5_mat")
            list_of_grades_button6 = types.InlineKeyboardButton(
                "Назад", callback_data="mathematics")
            list_of_grades_menu.add(list_of_grades_button1, list_of_grades_button2, list_of_grades_button3,
                                    list_of_grades_button4, list_of_grades_button5, list_of_grades_button6)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Математика: какую оценку добавить?", reply_markup=list_of_grades_menu)

        elif call.data == "add_grade_for_english":
            list_of_grades_menu = types.InlineKeyboardMarkup(row_width=5)
            list_of_grades_button1 = types.InlineKeyboardButton(
                "1", callback_data="grade_1_eng")
            list_of_grades_button2 = types.InlineKeyboardButton(
                "2", callback_data="grade_2_eng")
            list_of_grades_button3 = types.InlineKeyboardButton(
                "3", callback_data="grade_3_eng")
            list_of_grades_button4 = types.InlineKeyboardButton(
                "4", callback_data="grade_4_eng")
            list_of_grades_button5 = types.InlineKeyboardButton(
                "5", callback_data="grade_5_eng")
            list_of_grades_button6 = types.InlineKeyboardButton(
                "Назад", callback_data="english")
            list_of_grades_menu.add(list_of_grades_button1, list_of_grades_button2, list_of_grades_button3,
                                    list_of_grades_button4, list_of_grades_button5, list_of_grades_button6)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Английский язык: какую оценку добавить?", reply_markup=list_of_grades_menu)

        elif call.data == "add_grade_for_russian":
            list_of_grades_menu = types.InlineKeyboardMarkup(row_width=5)
            list_of_grades_button1 = types.InlineKeyboardButton(
                "1", callback_data="grade_1_rus")
            list_of_grades_button2 = types.InlineKeyboardButton(
                "2", callback_data="grade_2_rus")
            list_of_grades_button3 = types.InlineKeyboardButton(
                "3", callback_data="grade_3_rus")
            list_of_grades_button4 = types.InlineKeyboardButton(
                "4", callback_data="grade_4_rus")
            list_of_grades_button5 = types.InlineKeyboardButton(
                "5", callback_data="grade_5_rus")
            list_of_grades_button6 = types.InlineKeyboardButton(
                "Назад", callback_data="russian")
            list_of_grades_menu.add(list_of_grades_button1, list_of_grades_button2, list_of_grades_button3,
                                    list_of_grades_button4, list_of_grades_button5, list_of_grades_button6)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Русский язык: какую оценку добавить?", reply_markup=list_of_grades_menu)

    elif call.data == "remove_grade_for_informatics" \
            or call.data == "remove_grade_for_mathematics" \
            or call.data == "remove_grade_for_english" \
            or call.data == "remove_grade_for_russian":
        if call.data == "remove_grade_for_informatics":
            remove_grade(call, "inf")

        elif call.data == "remove_grade_for_mathematics":
            remove_grade(call, "mat")

        elif call.data == "remove_grade_for_english":
            remove_grade(call, "eng")

        elif call.data == "remove_grade_for_russian":
            remove_grade(call, "rus")

    elif call.data == "grade_1_inf" \
            or call.data == "grade_2_inf" \
            or call.data == "grade_3_inf" \
            or call.data == "grade_4_inf" \
            or call.data == "grade_5_inf":
        if call.data == "grade_1_inf":
            add_grade(call, "inf", "1")

        elif call.data == "grade_2_inf":
            add_grade(call, "inf", "2")

        elif call.data == "grade_3_inf":
            add_grade(call, "inf", "3")

        elif call.data == "grade_4_inf":
            add_grade(call, "inf", "4")

        elif call.data == "grade_5_inf":
            add_grade(call, "inf", "5")

    elif call.data == "grade_1_mat" \
            or call.data == "grade_2_mat" \
            or call.data == "grade_3_mat" \
            or call.data == "grade_4_mat" \
            or call.data == "grade_5_mat":
        if call.data == "grade_1_mat":
            add_grade(call, "mat", "1")

        elif call.data == "grade_2_mat":
            add_grade(call, "mat", "2")

        elif call.data == "grade_3_mat":
            add_grade(call, "mat", "3")

        elif call.data == "grade_4_mat":
            add_grade(call, "mat", "4")

        elif call.data == "grade_5_mat":
            add_grade(call, "mat", "5")

    elif call.data == "grade_1_eng" \
            or call.data == "grade_2_eng" \
            or call.data == "grade_3_eng" \
            or call.data == "grade_4_eng" \
            or call.data == "grade_5_eng":
        if call.data == "grade_1_eng":
            add_grade(call, "eng", "1")

        elif call.data == "grade_2_eng":
            add_grade(call, "eng", "2")

        elif call.data == "grade_3_eng":
            add_grade(call, "eng", "3")

        elif call.data == "grade_4_eng":
            add_grade(call, "eng", "4")

        elif call.data == "grade_5_eng":
            add_grade(call, "eng", "5")

    elif call.data == "grade_1_rus" \
            or call.data == "grade_2_rus" \
            or call.data == "grade_3_rus" \
            or call.data == "grade_4_rus" \
            or call.data == "grade_5_rus":
        if call.data == "grade_1_rus":
            add_grade(call, "rus", "1")

        elif call.data == "grade_2_rus":
            add_grade(call, "rus", "2")

        elif call.data == "grade_3_rus":
            add_grade(call, "rus", "3")

        elif call.data == "grade_4_rus":
            add_grade(call, "rus", "4")

        elif call.data == "grade_5_rus":
            add_grade(call, "rus", "5")


# voice tracking
@bot.message_handler(content_types=["voice"])
def voice_tracking(message):
    src = f"voice/{message.from_user.id}.ogg"
    dst = f"voice/{message.from_user.id}.wav"

    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    sound = AudioSegment.from_ogg(src)
    sound.export(dst, format="wav")

    recognised_text = recognise(dst)
    print(recognised_text)

    if recognised_text.lower() == "старт":
        start(message)

    elif recognised_text.lower() in config.helpWords:
        help(message)

    elif recognised_text.lower() in config.diary_words:
        diary(message)

    elif recognised_text.lower() in config.helloWords:
        bot.send_message(message.chat.id, f"""
И тебе привет 😉
Что хочешь узнать?""")
        help(message)

    elif recognised_text.lower() in config.whoIsYourOwner:
        bot.send_message(
            message.chat.id, "Самсонов Евгений (@SamsonovEugene) мой хозяин ")

    elif recognised_text.lower() in config.TimelineWords:
        bot.send_message(message.chat.id, config.TimelineForLessons)

    elif recognised_text.lower() in config.lessonScheduleWordsFor11_2:
        bot.send_message(message.chat.id, config.lessonScheduleFor11_2)

    elif recognised_text.lower() in config.lessonScheduleWordsFor11_1:
        bot.send_message(message.chat.id, config.lessonScheduleFor11_1)

    elif recognised_text.lower() in config.whoDoesntStudyOnSaturday:
        bot.send_message(message.chat.id, """
    В субботу не учаться ученики начальных классов (1-4),
    Все остальные (5-11) классы в субботу учаться (""")

    elif recognised_text.lower() in config.whatDirectorNameWords:
        bot.send_message(
            message.chat.id, f"Директора школы зовут {config.director_name}")

    elif recognised_text.lower() in config.whatAddressOfSchoolWords:
        bot.send_message(message.chat.id, "Ирчи Казака 126 г")

    elif recognised_text.lower() in config.thanksWords:
        bot.send_message(message.chat.id, "Всегда пожалуйста ;)")

    elif recognised_text.lower() in config.electivesScheduleWords:
        bot.send_message(message.chat.id, config.electivesSchedule)

    elif recognised_text.lower() in config.listOfEGEWords:
        bot.send_message(message.chat.id, config.listOfEGE)

    elif recognised_text.lower() in config.whatPhoneNuberOfSchoolWords:
        bot.send_message(
            message.chat.id, "Номер телефона школы: +7 (8722) 62-63-93")

    else:
        bot.send_message(
            message.chat.id, "Я не расслышал :(, пожалуйста повторите")


# Bot none-stop
bot.polling(none_stop=True)
