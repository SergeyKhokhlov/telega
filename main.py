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
    reply_keyboard = [["Готов"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text("Вас приветствует бот 'Тестирующая система', "
                              "в нем вы можете пройти "
                              "тест по знаниям соцсетей. "
                              "Если вы готовы начать нажмите на кнопку "
                              "'Готов'", reply_markup=markup)


def first_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        update.message.reply_text(questions[0])
        if update.message.text == responses[0]:
            correct_answers += 1
        return 1
    else:
        return ConversationHandler.END


def second_response(update, context):
    global questions, responses, correct_answers
    if update.message.text != "/stop":
        update.message.reply_text(questions[1])
        if update.message.text == responses[1]:
            correct_answers += 1
        return 2
    else:
        return ConversationHandler.END


def stop(update, context):
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(MessageHandler(Filters.regex("Готов"),
    #                               first_response))
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('Готов', first_response)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text, first_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(Filters.text, second_response)]
        },
        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
