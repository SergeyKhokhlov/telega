# Нужно написать чтобы все вопросы были в разнобой!

from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler, ConversationHandler
import json
import random
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

TOKEN = "852223716:AAGdVVMYgHTro5LM7yTfmprosTgE9cBTxOA"
questions = []
responses = []
temp = []
correct_answers = 0


def start(update, context):
    global questions, responses
    with open("static/json/bot.json", encoding='utf-8') as file:
        test_json = json.loads(file.readline())
        test = test_json['test']
        for i in test:
            temp.append(i)
        for i in range(len(temp) - 1, 0, -1):
            j = random.randint(0, i + 1)
            temp[i], temp[j] = temp[j], temp[i]
        for i in temp:
            questions.append(i['question'])
            responses.append(i['response'])
    reply_keyboard = [["/stop"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text("Вас приветствует бот 'Тестирующая система', "
                              "в нем вы можете пройти "
                              "тест по знаниям соцсетей. "
                              "Если вы готовы начать, напишите что угодно. Но если вам надоело и "
                              "вы хотите прекратить игру, то нажмите "
                              "/stop.", reply_markup=markup)
    return 1


def first_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        update.message.reply_text(questions[0])
        return 2
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def second_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[0]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[1]}")
            return 3
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[1]}")
        return 3
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def third_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[1]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[2]}")
            return 4
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[2]}")
        return 4
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def fourth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[2]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[3]}")
            return 5
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[3]}")
        return 5
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def fifth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[3]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[4]}")
            return 6
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[4]}")
        return 6
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def sixth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[4]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[5]}")
            return 7
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[5]}")
        return 7
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def seventh_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[5]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[6]}")
            return 8
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[6]}")
        return 8
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def eighth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[6]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[7]}")
            return 9
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[7]}")
        return 9
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def ninth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[7]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[8]}")
            return 10
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[8]}")
        return 10
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def tenth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[8]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[9]}")
            return 11
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[9]}")
        return 11
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def end(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[9]:
            correct_answers += 1
            update.message.reply_text(f"Верно. Вы ответили правильно на:{correct_answers} вопросов")
            return ConversationHandler.END
        update.message.reply_text(f"Не верно. Вы ответили правильно на:{correct_answers} вопросов")
        return ConversationHandler.END
    else:
        questions = []
        responses = []
        update.message.reply_text("Диалог окончен.")
        return ConversationHandler.END


def stop(update, context):
    global questions, responses
    questions = []
    responses = []
    update.message.reply_text("Диалог окончен.")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start', start)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text, first_response)],
            2: [MessageHandler(Filters.text, second_response)],
            3: [MessageHandler(Filters.text, third_response)],
            4: [MessageHandler(Filters.text, fourth_response)],
            5: [MessageHandler(Filters.text, fifth_response)],
            6: [MessageHandler(Filters.text, sixth_response)],
            7: [MessageHandler(Filters.text, seventh_response)],
            8: [MessageHandler(Filters.text, eighth_response)],
            9: [MessageHandler(Filters.text, ninth_response)],
            10: [MessageHandler(Filters.text, tenth_response)],
            11: [MessageHandler(Filters.text, end)],
        },
        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
