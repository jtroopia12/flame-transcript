**Desenvolvido por Herzog, KT, P4rallax.**

![image](https://github.com/user-attachments/assets/f282355b-0772-4ff3-8269-02e88f021c9d)


🔥🔥🔥 **Flame Transcript: Script de Transcrição para Detectar Cortes de Lives.** 🔥🔥🔥

Necessário ter conhecimento básico de Terminal (cmd) para executar, visto que o Script não tem interface gráfica, não tenho mais interesse em atualizar o código do Script então a divulgação é livre, essa documentação README, serve para executar os scripts a fim de identificar cortes de lives, vídeos, onde determinado termo, frase foi dita. O script é útil principalmente para resgatar lives antigas ou gigantescas e captar momentos específicos que ocorreram. 


**Faça o Download do repositório do ZIP**
![image](https://github.com/user-attachments/assets/ed647c46-0856-4062-8804-8e738df8c889)



📖 **Motivação**

Clipadores são um dos pilares do FlameWar, apesar de recentemente o tal ofício ter sido desmerecido, bem como a banalização do passado por parte de diversos participantes, porém manter a memória do flame é extremamente importante, principalmente por se tratar de uma bolha volátil, onde por muitas vezes as pessoas negam o que falaram ou mudam as narrativas conforme a treta do momento, clipar não se encaixa em crime nenhum, desde que não seja utilizado para monetizar em cima do conteúdo de outro.

**Importante:** O dono do conteúdo, possuí os aparatos e suporte do Youtube para a remoção de cortes, porém não é capacitado em proteger seus vídeos e lives das “transcrições auto-geradas.” Pelo próprio Youtube. 

Essa ferramenta irá fazer o download e analisar as transcrições de vídeos e lives, com base em palavras, frases ditas pelo dono da live ou convidados, irá gerar um EXCEL onde conterá o nome da live, a palavra capturada e um pequeno trecho onde é possível identificar o contexto da palavra e verificar se vale a pena conferir.
Nem sempre a ferramenta será precisa, visto que depende especificamente da oratória, dicção e microfone dos participantes das lives/vídeos, muitas vezes palavras e/ou nomes difíceis podem ser capturados de forma errado, exemplo, muitas vezes “Herzog” foi capturado como “Zog” ou “Rizorg”, por isso é importante ao executar o script gerar várias possíveis combinações a fim de conseguir captar as palavras nos vídeos.


**Essa ferramenta NÃO faz downloads de transcrições de lives privadas ou não-listadas, deletadas, visto ser impossível ter acesso as URLS dessas lives/vídeos.**
Apesar de batizada como ‘Flame Transcript’, ela pode ser usada em qualquer meio, desde que seja no Youtube. 



🛠️ **Como utilizar**


**1 –** Primeiro Passo: Instalação das Dependências


**1.1 -** Fazer o Download do Python, sempre baixe o Python 3.  https://www.python.org/downloads/

![image](https://github.com/user-attachments/assets/982a9d17-be19-4fef-bd86-1abb7f34f244)


**1.2 –** Faça o Download de um Terminal/CMD decente, recomendo utilizar o Windows Terminal é possível baixá-lo gratuitamente pela Microsoft Store.


![image](https://github.com/user-attachments/assets/14c3d276-62fe-4626-91aa-dc38c668cf4e)


**1.3 –** Rode o seguinte comando no terminal/cmd para verificar se deu certo a instalação do python, deve retornar a versão, dê um Google se ocorrer algum erro na hora da instalação do Python, na minha maquina tenho o Python 3.12.7, mas já tem a versão 3.13, por exemplo. É necessário ser sempre a versão 3, o que vier depois do 3 é irrelevante. 


**python --version**

![image](https://github.com/user-attachments/assets/f243b943-4e45-4011-ab26-584eb66af645)


**1.4 –** Faça o download de uma IDE ou o Notepad++ eu recomendo utilizar o Visual Studio Code.  
https://code.visualstudio.com/


**1.5 –** Abra o Visual Studio Code e carregue a pasta, onde estão os scripts. 


![image](https://github.com/user-attachments/assets/c3dc53cd-4bb9-4571-b5e6-4f6c889043b7)

**2 –** Segundo passo: Como executar os Scripts


**2.1 –** É necessário abrir a pasta onde os scripts estão localizados diretamente no Terminal, se não tem familiaridades com comandos de terminal (cd, pwd, ls) etc. Recomendo abrir o local da pasta – Botão direito – Abrir no Terminal.


![image](https://github.com/user-attachments/assets/94c34adf-2a42-4e01-a1f8-8d9df6e7a60f)


![image](https://github.com/user-attachments/assets/9dfbaaeb-62f8-4de1-a6ef-113195d17e46)


Certifique que dentro da pasta contenha os 3 scripts necessários para a execução. 
É necessário executar o seguinte comando para instalar as dependências Python para executar os scripts, estando na pasta do projeto execute no terminal.


**pip install -r requirements.txt**


**2.2 –** Fazer o Download de todas as URLS de um canal específico. 


A primeira etapa é fazer o download de todas as URLS de um canal, para isso irá utilizar o script urlcollector.py, obviamente você só vai executá-lo 1 vez por canal, utilizarei o canal do Pop como exemplo. 


Agora com o terminal aberto. **(Lembrando sempre do terminal estar aberto na pasta, onde contenha os arquivos de script, veja o item 2.1, caso não tenha feito.)**
Execute o seguinte comando: 


**python .\urlcollector.py**


Se tudo der certo o script irá começar a fazer o download das URLS e após concluir ele avisará que deu certo.


![image](https://github.com/user-attachments/assets/b79db22e-6810-4c2d-93d1-05821871b325)


Deve colar a URL do canal conforme o print.
Deve colocar o nome do arquivo texto com a extensão .txt, igual o print “**pop.txt**”


![image](https://github.com/user-attachments/assets/c2a1f242-0a65-45df-912a-35fe80709120)


![image](https://github.com/user-attachments/assets/5e62ef33-80e5-4b55-b15d-f486b625fe1e)


**2.3 –** Fazer o Download das Transcrições dos vídeos.


A etapa mais demorada é essa, onde após coletar as URLS é necessário realizar o download das transcrições.

Execute o seguinte Script. (É necessário possuir as URLS, capturadas no passo anterior.)

**python .\download_transcriptions.py**

É necessário digitar o nome da Pasta onde as transcrições serão salvas. 

![image](https://github.com/user-attachments/assets/e26c3694-e823-4169-8c3a-879b0b3002f2)

Após realizar o download das transcrições que pode demorar dependendo da quantidade de vídeos/lives é possível verificar na pasta as transcrições baixadas.

![image](https://github.com/user-attachments/assets/19ac4571-6b02-470c-a9d3-eb161f3e1760)


**3.0 –** Usar o script de analisar transcrições


Os passos 1.0 e 2.0, devem ser rodados uma vez para cada canal que for baixado as transcrições. O Script de análise de palavras-chaves será o mais frequente de ser utilizado. 


**Considerações:** As transcrições são auto-geradas pelo Youtube através do youtube-transcription-api, por se tratar de uma ferramenta de acessibilidade é impossível evitar que as transcrições sejam geradas, porém por serem auto-geradas algumas terminologias, nomes, frases podem estar mal-escritas, isso depende da dicção, microfone dos participantes das lives.

Pesquisar palavras de forma absoluta pode gerar problemas em encontrar o termo, por tanto é importante colocar várias palavras para ter um melhor resultado.
**Exemplos: Herzog, Zog, Rizorg, Hezog**


**3.1 –** Execute o script de transcrição.


**python .\transcriptplus.py**

- Selecione a pasta que foi feito o download das transcrições.
- Preencha as palavras separadas por vírgula conforme o print.
- As palavras com condicionais significam que o script irá imprimir as palavras solicitadas, caso elas façam um “match” com outra palavra irá trazer. 
- Adicione o nome do excel que será gerado, coloque com a extensão, exemplo
**pop.xlsx**
  

![image](https://github.com/user-attachments/assets/03ddc4c9-925c-4960-99ef-57ce9b091040)

![image](https://github.com/user-attachments/assets/c9177132-0881-41da-811d-5bab691ac6c8)


Após rodar o script e caso as palavras forem capturas ele irá criar o Excel.

**3.2 –** Analisando o Excel gerado.


![image](https://github.com/user-attachments/assets/380b1902-8d64-450d-8cae-881ddae17c3f)

O excel possui 3 colunas.


**Nome do Arquivo:** É o nome da live/vídeo que é baixada pelo script de download de transcrições. 


**SomosGamersOtarios__Todo_ano_anunciam_jogos_SEM_DATA_e_Depois_Somem_.._** *ScUGjaC5igI*


**Em negrito:** O nome da live os espaços são computados como underlines.


*Em itálico:* É a URL do vídeo. 

**Palavras Capturadas:**  São as palavras que foram capturadas pelo Script.
**Trechos Encontrados:** Uma breve descrição dos trechos encontrados para dar contexto.


**4.0 –** Como encontrar o timestamp e clipar os termos encontrados. 

Após identificar os trechos da live, recomendo que invés de assistir toda a live, procure o trecho citado através do plugin de transcrições do Youtube. 

https://chromewebstore.google.com/detail/transcri%C3%A7%C3%A3o-do-youtube/jgibaoklabopileepldnlkbbcibhbgmd

![image](https://github.com/user-attachments/assets/be2f5210-c536-4cbe-a060-0a0babb2947f)

Pesquise usando o CTRL + F os termos capturados pelo script e clique no tempo para avançar para a hora do corte.

![image](https://github.com/user-attachments/assets/1e33ea46-f40e-495e-bad6-3a0d48b3ab5d)

![image](https://github.com/user-attachments/assets/6c43008a-4a10-4690-883d-1b46a87d5fbb)

**4.1 –** Caso a live não esteja pública e você tem a live baixada, upe-a como não-listada no seu canal e aguarde algumas horas até que a transcrição seja gerada. 


































