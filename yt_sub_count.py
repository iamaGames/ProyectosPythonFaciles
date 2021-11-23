from time import sleep
from googleapiclient.discovery import build
from tkinter import *
from PIL import ImageTk, Image

api_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' #tu clave de desarrollador 

youtube = build('youtube', 'v3', developerKey=api_key)



def main():
    ventana.after(10000, update_subs)
    ventana.mainloop()
    sleep(10)
    suscribers = get_sub_count()
    subs_str.set(suscribers)

def update_subs():
    subscribers = get_sub_count()
    subs_str.set(subscribers)
    ventana.after(10000, update_subs)

def get_sub_count():
    request = youtube.channels().list(
        part='statistics',
        id='UC5j1czowr-syXH7b3hi7Kgw'
    )
    response = request.execute()
    suscribers = response["items"][0]["statistics"]["subscriberCount"]
    return suscribers

def create_window():
    ventana = Tk()
    ventana.title("Contador Subs")
    ventana.config(bg="white")
    ventana.geometry("500x500")
    ventana.resizable(width=False, height=False)
    return ventana


def create_profile_img():
    imagen_canal = ImageTk.PhotoImage(
    Image.open("./img/perfil.png").resize((200, 200), Image.ANTIALIAS))
    imagen_label = Label(ventana, image=imagen_canal)
    imagen_label.pack(side=TOP, pady=40)


def create_subs_label(get_sub_count, ventana):
    subs_str = StringVar()
    subscribers = get_sub_count()
    subs_str.set(subscribers)
    subs_label = Label(ventana, font = ('Roboto',70,'bold'), textvariable=subs_str)
    subs_label.config(bg="white", fg='#000')
    subs_label.pack(side=BOTTOM, pady = 50)
    return subs_str

create_profile_img()
ventana = create_window()
subs_str = create_subs_label(get_sub_count, ventana)
main()



