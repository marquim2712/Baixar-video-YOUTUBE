Se você não tiver o Python instalado, baixe e instale a partir do site oficial: https://www.python.org/

2 Instalação de dependências
yt-dlp
yt-dlp é uma versão aprimorada do youtube-dl que permite a extração de vídeos de várias plataformas, incluindo o YouTube.

Para instalar o yt-dlp, use o seguinte comando:

pip install yt-dlp
Tkinter
O Tkinter já vem incluído na instalação padrão do Python para a maioria dos sistemas. No entanto, se você estiver usando uma distribuição minimalista do Python, pode ser necessário instalá-lo separadamente. Em sistemas baseados em Linux, você pode instalá-lo com o seguinte comando:

sudo apt-get install python3-tk
Para usuários de Windows e Mac, o Tkinter já está incluído, portanto, não há necessidade de instalação adicional.

3 Outros pacotes necessários
Instale qualquer outra dependência necessária com o seguinte comando:

pip install -r requirements.txt
(O arquivo requirements.txt deve conter qualquer outra dependência que venha a ser adicionada ao projeto).

Como Executar o Aplicativo
Faça o download ou clone este repositório.

git clone https://github.com/seu-usuario/youtube-downloader.git
cd youtube-downloader
Execute o aplicativo com o seguinte comando:

python yt_dlp_downloader.py
A interface gráfica será aberta. Agora, basta inserir o link do vídeo do YouTube, carregar as resoluções disponíveis e selecionar uma para iniciar o download.

OU EXECUTE SEU APP PELO O ARQUIVO yt_dlp_downloader.py NO TERMINAL DE COMANDO.