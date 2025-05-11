from telegram.ext import ApplicationBuilder, CommandHandler

async def mesaj_gonder(update, context):
    await update.message.reply_text("Mesajınız alındı! Yardımcı olabilir miyim?")

def main():
    app = ApplicationBuilder().token("7725557881:AAH1_-xKmWqdysKuNAY7Ts49ixo3JxCGHVQ").build()
    app.add_handler(CommandHandler("mesaj", mesaj_gonder))  # /mesaj komutunu yakala
    app.run_polling()

if __name__ == '__main__':
    main()
