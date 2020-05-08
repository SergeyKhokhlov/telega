from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

TOKEN = "852223716:AAGdVVMYgHTro5LM7yTfmprosTgE9cBTxOA"
questions = []
responses = []


def start(update, context):
    global questions, responses
    with open("static/json/bot.json", encoding='utf-8') as file:
        reply_keyboard = [["Готов"]]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(f"{file.readlines()} Вас приветствует бот "
                                  f"'Тестирующая система', в нем вы можете пройти "
                                  "тест по знаниям соцсетей. Если вы готовы начать нажмите на кнопку "
                                  "'Готов'", reply_markup=markup)


def test(update, context):
    pass


def stop(update, context):
    pass


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex("Готов"),
                                  test))
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start', start)],

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
