from time import sleep
from googleapiclient.discovery import build
from tkinter import *
from PIL import ImageTk, Image

api_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' #tu clave de desarrollador 

youtube = build('youtube', 'v3', developerKey=api_key)

def check_nuevos_subs():
    ventana.mainloop()
    sleep(10)
    request = youtube.channels().list(
        part='statistics',
        id='UC5j1czowr-syXH7b3hi7Kgw'
    )
    response = request.execute()
    suscribers = response["items"][0]["statistics"]["subscriberCount"]
    subs_str.set(suscribers)


request = youtube.channels().list(
        part='statistics',
        id='UC5j1czowr-syXH7b3hi7Kgw'
    )

response = request.execute()
suscribers = response["items"][0]["statistics"]["subscriberCount"]

#Creamos una ventana
ventana = Tk()
ventana.title("Contador Subs")
ventana.config(bg="white")
ventana.geometry("500x500")
ventana.resizable(width=False, height=False)

imagen_canal = ImageTk.PhotoImage(
    Image.open("./img/perfil.png").resize((200, 200), Image.ANTIALIAS))
imagen_label = Label(ventana, image=imagen_canal)
imagen_label.pack(side=TOP, pady=40)

#Creamos una etiqueta para el contador de suscripciones
subs_str = StringVar()
subs_str.set(suscribers)
subs_label = Label(ventana, font = ('Roboto',70,'bold'), textvariable=subs_str)
subs_label.config(bg="white", fg='#000')
subs_label.pack(side=BOTTOM, pady = 50)

check_nuevos_subs()



