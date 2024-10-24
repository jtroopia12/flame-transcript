import os
import re
import requests
from tkinter import Tk, filedialog
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript

# Função para extrair o ID do vídeo a partir da URL
def get_video_id(url):
    if 'v=' in url:
        return url.split('v=')[1]
    elif 'youtu.be/' in url:
        return url.split('youtu.be/')[1]
    else:
        return None

# Função para baixar a transcrição de um vídeo
def download_transcription(video_id, output_dir):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['pt'])
        transcript_text = transcript.fetch()

        transcript_content = "\n".join([text['text'] for text in transcript_text])
        video_title = get_video_title(video_id)

        # Se o título não estiver disponível, use o ID do vídeo como fallback
        if video_title == 'Título não disponível':
            video_file = f"{video_id}.txt"
        else:
            video_file = f"{video_title}_{video_id}.txt"

        with open(os.path.join(output_dir, video_file), 'w', encoding='utf-8') as file:
            file.write(f"Transcrição para o vídeo {video_id}:\n\n")
            file.write(transcript_content)

        print(f"Transcrição baixada para: {video_title}")

    except (TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript):
        print(f"Transcrição não disponível para o vídeo {video_id}.")
    except Exception as e:
        print(f"Erro ao baixar a transcrição do vídeo {video_id}: {e}")

# Função para obter o título do vídeo
def get_video_title(video_id):
    try:
        response = requests.get(f'https://www.youtube.com/watch?v={video_id}')
        title_match = re.search(r'<title>(.*?)</title>', response.text)
        if title_match:
            title = title_match.group(1).replace(' - YouTube', '').replace(' ', '_').strip()
            return re.sub(r'[\/:*?"<>|]', '', title)  # Remove caracteres inválidos para nomes de arquivos
        return 'Título não disponível'
    except Exception as e:
        print(f"Erro ao obter título do vídeo {video_id}: {e}")
        return 'Título não disponível'

# Função principal para processar as URLs do arquivo de entrada
def process_video_urls(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as file:
        urls = file.readlines()

    for index, url in enumerate(urls, start=1):
        url = url.strip()
        if url:
            video_id = get_video_id(url)
            if video_id:
                print(f"Baixando transcrição do vídeo {index}: {url}")
                download_transcription(video_id, output_dir)
            else:
                print(f"URL inválida: {url}")
        else:
            print(f"Linha {index} está vazia.")

# Função para abrir janela de seleção de arquivo
def select_input_file():
    root = Tk()
    root.withdraw()  # Esconde a janela principal
    input_file_path = filedialog.askopenfilename(
        title="Selecione o arquivo de URLs",
        filetypes=[("Arquivos de texto", "*.txt")]
    )
    return input_file_path

# Função para solicitar nome da pasta de saída
def get_output_dir():
    return input("Digite o nome da pasta para salvar as transcrições: ")

# Programa principal
def main():
    # Abrir janela para selecionar o arquivo de URLs
    input_file = select_input_file()

    if not input_file:
        print("Nenhum arquivo selecionado. Saindo.")
        return

    # Solicitar nome da pasta para salvar as transcrições
    output_dir = get_output_dir()

    # Processar as URLs
    process_video_urls(input_file, output_dir)

if __name__ == "__main__":
    main()
