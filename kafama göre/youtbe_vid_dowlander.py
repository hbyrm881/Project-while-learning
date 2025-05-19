import yt_dlp

def video_indir(link):
    ydl_opts = {
        'format': 'best',  # En iyi kaliteyi indir
        'outtmpl': '%(title)s.%(ext)s'  # Dosya adını video başlığı yap
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    url = input("YouTube video linkini girin: ")
    video_indir(url)
