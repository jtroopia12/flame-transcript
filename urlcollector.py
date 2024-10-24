import subprocess
import re
import os

# Função para capturar URLs dos vídeos e lives
def capture_video_urls(channel_url, output_file):
    try:
        # Executa o yt-dlp para listar todos os vídeos e salvar a saída em um arquivo
        result = subprocess.run(['yt-dlp', '--flat-playlist', '-J', channel_url], stdout=subprocess.PIPE, text=True)
        
        # Verifica se o yt-dlp retornou uma saída
        if result.stdout:
            output = result.stdout
        else:
            print("Nenhuma saída recebida do yt-dlp.")
            return

        # Extrair todas as URLs de vídeos do JSON
        video_urls = re.findall(r'https://www.youtube.com/watch\?v=[\w-]+', output)
        
        if video_urls:
            # Remover duplicados
            video_urls = list(set(video_urls))
            
            with open(output_file, 'w') as f:
                for url in video_urls:
                    f.write(f"{url}\n")
            print(f"URLs dos vídeos salvas em {output_file}")
        else:
            print("Nenhuma URL de vídeo foi encontrada.")
        
    except Exception as e:
        print(f"Erro ao capturar URLs: {e}")

# Solicitar a URL do canal e o nome do arquivo de saída ao usuário
channel_url = input("Cole a URL do canal do YouTube: ")
output_file = input("Digite o nome do arquivo de texto (ex: walacepop.txt): ")

# Verificar se o arquivo já existe
if os.path.exists(output_file):
    os.remove(output_file)
    print(f"Arquivo existente {output_file} removido.")

# Capturar URLs de vídeos e lives
capture_video_urls(channel_url, output_file)
