from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_audio(video_url, output_path):
    # Baixar o vídeo do YouTube
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download(output_path=output_path)
    
    # Converter o áudio para MP3
    base, ext = os.path.splitext(audio_file)
    mp3_file = base + '.mp3'
    audio = AudioSegment.from_file(audio_file)
    audio.export(mp3_file, format='mp3')
    
    # Remover o arquivo original
    os.remove(audio_file)
    
    return mp3_file

# Exemplo de uso
video_url = input("Informe a URL do vídeo: ")
output_path = './audios'
mp3_file = download_youtube_audio(video_url, output_path)
print(f'Áudio salvo em: {mp3_file}')
