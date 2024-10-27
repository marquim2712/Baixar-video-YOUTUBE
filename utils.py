import os
from datetime import datetime

# Cria uma pasta com a data atual
def create_download_folder():
    today = datetime.now().strftime('%Y-%m-%d')  # Formato de data AAAA-MM-DD
    folder_name = os.path.join(os.getcwd(), today)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)  # Cria a pasta se não existir
    return folder_name
