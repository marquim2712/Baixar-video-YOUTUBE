import os
import yt_dlp as youtube_dl
from datetime import datetime
from utils import create_download_folder

# Função para obter os formatos (resoluções) disponíveis
def get_video_formats(video_url):
    ydl_opts = {
        'listformats': True,  # Lista os formatos sem baixar
    }

    formats = []
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            formats = [f"{f['format_id']} - {f['format_note']}" for f in info['formats'] if 'format_note' in f]
    except Exception as e:
        print(f"Erro ao obter resoluções: {str(e)}")
    
    return formats

# Função principal para baixar vídeo com a resolução selecionada
def download_video(video_url, resolution):
    folder = create_download_folder()  # Cria a pasta com a data

    # Baixa na resolução escolhida
    ydl_opts = {
        'format': resolution.split(' ')[0],  # Seleciona a resolução
        'outtmpl': f'{folder}/%(title)s.%(ext)s',  # Salva na pasta criada
        'noplaylist': True,  # Apenas um vídeo
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download finalizado com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {str(e)}")
