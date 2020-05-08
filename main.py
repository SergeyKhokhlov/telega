from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram.ext import CommandHandler, ConversationHandler
import json
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

TOKEN = "852223716:AAGdVVMYgHTro5LM7yTfmprosTgE9cBTxOA"
questions = []
responses = []
correct_answers = 0


def start(update, context):
    global questions, responses
    with open("static/json/bot.json", encoding='utf-8') as file:
        test_json = json.loads(file.readline())
        test = test_json['test']
        for i in test:
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
        return ConversationHandler.END


def second_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[0]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[1]}")
            return 2
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[1]}")
        return 2
    else:
        return ConversationHandler.END


def third_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[1]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[2]}")
            return 3
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[2]}")
        return 3
    else:
        return ConversationHandler.END


def fourth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[2]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[3]}")
            return 4
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[3]}")
        return 4
    else:
        return ConversationHandler.END


def fifth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[3]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[4]}")
            return 2
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[4]}")
        return 2
    else:
        return ConversationHandler.END


def sixth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[4]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[5]}")
            return 2
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[5]}")
        return 2
    else:
        return ConversationHandler.END


def seventh_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[5]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[6]}")
            return 2
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[6]}")
        return 2
    else:
        return ConversationHandler.END


def eighth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[6]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[7]}")
            return 2
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[7]}")
        return 2
    else:
        return ConversationHandler.END


def ninth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[7]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[8]}")
            return 2
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[8]}")
        return 2
    else:
        return ConversationHandler.END


def tenth_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        if update.message.text == responses[8]:
            correct_answers += 1
            update.message.reply_text(f"Верно. А вот и следующий вопрос.\n{questions[9]}")
            return 2
        update.message.reply_text(f"Не верно. А вот и следующий вопрос.\n{questions[9]}")
        return 2
    else:
        return ConversationHandler.END


def stop(update, context):
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
        },
        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
