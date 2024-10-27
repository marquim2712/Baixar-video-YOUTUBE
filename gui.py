import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp_downloader_logic import get_video_formats, download_video
import threading

# Função para iniciar a interface gráfica
def start_gui():
    root = tk.Tk()
    root.title("Downloader de Vídeos do YouTube")
    
    # Estilizando o fundo da janela
    root.configure(bg="#333333")  # Cor de fundo cinza escuro
    root.geometry("600x400")
    
    # Definindo uma fonte padrão
    default_font = ("Helvetica", 12)
    
    # Texto para inserir URL
    url_label = tk.Label(root, text="Insira o link do vídeo:", bg="#333333", fg="#FFFFFF", font=default_font)
    url_label.pack(pady=10)

    url_entry = tk.Entry(root, width=60, font=default_font)
    url_entry.pack(pady=5)

    # Label para a resolução
    resolution_label = tk.Label(root, text="Selecione a resolução do vídeo:", bg="#333333", fg="#FFFFFF", font=default_font)
    resolution_label.pack(pady=10)

    # Variável que armazenará a resolução selecionada
    selected_resolution = tk.StringVar()

    # Inicializa a variável resolution_menu
    resolution_menu = None

    # Barra de progresso estilizada
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    
    # Estilo ttk para botões
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 10), background="#333333", foreground="#FFFFFF")
    
    # Função para carregar as resoluções disponíveis
    def load_resolutions():
        nonlocal resolution_menu  # Permite o uso da variável resolution_menu definida fora da função
        video_url = url_entry.get()
        if not video_url:
            messagebox.showerror("Erro", "Por favor, insira o link do vídeo.")
            return

        try:
            formats = get_video_formats(video_url)  # Obtém os formatos disponíveis
            if formats:
                if resolution_menu:
                    resolution_menu.pack_forget()  # Remove o menu antigo, se houver
                resolution_menu = tk.OptionMenu(root, selected_resolution, *formats)
                resolution_menu.configure(bg="#444444", fg="#FFFFFF", font=default_font)
                resolution_menu.pack(pady=10)
                selected_resolution.set(formats[0])  # Seleciona a primeira resolução por padrão
                download_button.config(state=tk.NORMAL)  # Habilita o botão de download
            else:
                messagebox.showerror("Erro", "Nenhuma resolução disponível.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar resoluções: {str(e)}")

    # Função para iniciar o download em uma thread separada
    def start_download():
        video_url = url_entry.get()
        resolution = selected_resolution.get()
        if video_url and resolution:
            # Desabilitar botões enquanto o download está em andamento
            download_button.config(state=tk.DISABLED)
            progress.pack(pady=20)
            threading.Thread(target=on_download, args=(video_url, resolution)).start()
        else:
            messagebox.showerror("Erro", "Por favor, insira o link do vídeo e selecione uma resolução.")

    # Função de download
    def on_download(video_url, resolution):
        try:
            download_video(video_url, resolution)
            messagebox.showinfo("Sucesso", "Download finalizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {str(e)}")
        finally:
            # Habilitar os botões novamente após o download
            download_button.config(state=tk.NORMAL)
            progress.pack_forget()

    # Botão para carregar as resoluções
    load_button = tk.Button(root, text="Carregar Resoluções", command=load_resolutions, bg="#4CAF50", fg="#FFFFFF", font=default_font)
    load_button.pack(pady=20)

    # Botão de download (desabilitado inicialmente)
    download_button = tk.Button(root, text="Baixar", state=tk.DISABLED, bg="#2196F3", fg="#FFFFFF", font=default_font)
    download_button.pack(pady=20)

    root.mainloop()
