import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot token'ını burada girin
TOKEN = '7725557881:AAH1_-xKmWqdysKuNAY7Ts49ixo3JxCGHVQ'

# Logları etkinleştir
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /start komutu
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Merhaba! Zayıflama hedeflerinizi takip etmenize yardımcı olacağım.")

# Günlük yemek kaydı yapma
def record_food(update: Update, context: CallbackContext) -> None:
    food = " ".join(context.args)  # Kullanıcının yazdığı yiyecekleri al
    # Burada yiyecekleri kaydedebiliriz (örneğin JSON dosyasına)
    update.message.reply_text(f"Yediğiniz yemek: {food} kaydedildi.")

# Hata mesajları
def error(update: Update, context: CallbackContext) -> None:
    print(f"Update {update} caused error {context.error}")

# Ana fonksiyon
def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    # Komutları işlemek
    dp.add_handler(CommandHandler("start", start))  # /start komutu
    dp.add_handler(CommandHandler("food", record_food))  # /food komutu

    # Hata işleme
    dp.add_error_handler(error)

    # Botu başlat
    updater.start_polling()

    # Botun kapanmasını bekle
    updater.idle()

if __name__ == '__main__':
    main()
