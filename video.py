import yt_dlp

output_dir = 'vídeos'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

url = input("URL do YouTube: ")

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s')
}

try:
    # Baixa o vídeo do YouTube
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Vídeo baixado com sucesso na pasta 'vídeos'!")
except yt_dlp.utils.DownloadError as e:
    print(f"Erro ao baixar o vídeo: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")