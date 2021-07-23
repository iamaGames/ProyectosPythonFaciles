from tkinter import *
import tkinter

def traducir():
    texto = input_texto.get()
    toret = ""
    for i in range(0, len(texto)):

        #añade un salto de linea cada 4 caracteres
        if i%4==0 and i!= 0:
            toret += '\n'
        ascii_texto = ord(texto[i])
        bin_texto = "{0:b}".format(ascii_texto)
        print(bin_texto)
        toret += bin_texto + ' '
    texto_traducido.set(toret)

ventana = Tk()
ventana.title("Carácteres a binario")
ventana.geometry("500x500")
ventana.resizable(width=False, height=False)

convert_label = Label(ventana, 
        text="Introduce la palabra o frase que quiere convertir a binario",
        font='Roboto 8')
convert_label.pack()

input_texto = Entry(ventana, font="Roboto 8")
input_texto.pack()

boton_traducir = Button(ventana, text="Traduce", 
        font = "Roboto 8", 
        command=traducir)
boton_traducir.pack()

converted_label = Label(ventana, 
        text="Resultado de la conversión:",
        font='Roboto 8')
converted_label.pack()

texto_traducido = StringVar()
texto_traducido.set("")
texto_traducido_label = Label(ventana, 
        textvariable=texto_traducido, 
        font="Roboto 8")
texto_traducido_label.pack()

ventana.mainloop()