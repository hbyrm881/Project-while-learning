from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Lütfen bir YouTube linki gönderin.")

async def indir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = update.message.text
    try:
        await update.message.reply_text("İndiriliyor...")

        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            dosya_adi = ydl.prepare_filename(info)

        # Dosya boyutunu kontrol et
        if os.path.getsize(dosya_adi) > 49 * 1024 * 1024:
            await update.message.reply_text("⚠️ Dosya 50MB'den büyük olduğu için Telegram'a yüklenemiyor.")
        else:
            await update.message.reply_video(video=open(dosya_adi, 'rb'))

        os.remove(dosya_adi)  # Temizlik
    except Exception as e:
        await update.message.reply_text(f"Hata oluştu: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token("7725557881:AAH1_-xKmWqdysKuNAY7Ts49ixo3JxCGHVQ").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, indir))

    app.run_polling()
