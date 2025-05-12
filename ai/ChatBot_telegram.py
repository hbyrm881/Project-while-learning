import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Botu kontrol etmek için loglama ayarı yapalım
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Start komutu için bir fonksiyon
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Merhaba! Benimle konuşmak için yazabilirsiniz.')

# Hata yönetimi
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Botun tokenını buraya ekle
    token = '7643401707:AAEdal7-3xG_RKPIhfpDr2XAfLIx8Kaz8c4'

    # Application nesnesi ile botu başlat
    application = Application.builder().token(token).build()

    # Dispatcher'a handler ekle
    application.add_handler(CommandHandler("start", start))

    # Hata işleyici
    application.add_error_handler(error)

    # Botu çalıştır
    application.run_polling()

if __name__ == '__main__':
    main()
