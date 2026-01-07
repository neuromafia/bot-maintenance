import telebot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    print("Error: BOT_TOKEN environment variable not set.")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: message.chat.type == 'private')
def echo_all(message):
    bot.reply_to(message, "🕯 Город засыпает...\nNeuroMafia временно ушла в тень.\nМы проводим технические работы. Совсем скоро город снова проснётся — следите за новостями.\nЧтобы пообщаться с другими участниками и узнать новости клуба, заходи в наш чат [t.me/neuro_mafia_spb](t.me/neuro_mafia_spb) 💬")

bot.infinity_polling()
