import yt_dlp

url = input("URL do YouTube: ")

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Vídeo baixado com sucesso!")