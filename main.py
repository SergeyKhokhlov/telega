from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

TOKEN = "852223716:AAGdVVMYgHTro5LM7yTfmprosTgE9cBTxOA"


def start(update, context):
    reply_keyboard = [["Готов"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text("Вас приветствует бот 'Тестирующая система', в нем вы можете пройти "
                              "тест по знаниям соцсетей. Если вы готовы начать нажмите на кнопку "
                              "'Готов'", reply_markup=markup)


def test(update, context):
    pass


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex("Готов"),
                                  test))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
