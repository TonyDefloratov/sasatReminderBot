import time
from telegram import Bot
from telegram import Update
from telegram.ext import MessageHandler, Filters, CallbackContext
from telegram.ext import Updater


with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Этот бот поможет тебе не забыть снять сасалку с зарядки. Напиши сообщение, в котором присудствует слово "сасалку".')


def remind_to_turn_off_kettle(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text

    if "сасалку" in message_text:
        update.message.reply_text('Понял тебя, еба! Как настанет время, я тебя пну.')
        time.sleep(900)
        update.message.reply_text('Сыми бля сасалку с зарядки, даун!')

    if "сасалку" not in message_text:
        update.message.reply_text('Да мне похуй, что ты там сделал. Я тут, чтобы напомнеть тебе про сасалку. Либо пишешь мне про "сасалку", либо идешь нахуй!')


def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, remind_to_turn_off_kettle))
    dp.add_handler(MessageHandler(Filters.command & Filters.regex(r'^/start$'), start))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
