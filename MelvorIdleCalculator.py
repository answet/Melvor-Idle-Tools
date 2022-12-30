import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Melvor Idle XP Calulator')
root.iconbitmap('./src/icono.ico')

# dimensiones de la ventana
window_width = 300
window_height = 225

# se pide las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# se calcula el centro
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# se centra la ventana
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# recibir XP Actual
xp_actual = tk.IntVar()

xp_actual_label = ttk.Label(root, text="XP Actual: ")
xp_actual_label.pack()

xp_actual_entry = ttk.Entry(root, textvariable=xp_actual)
xp_actual_entry.pack()


# recibir XP Objetivo
xp_objetivo = tk.IntVar()

xp_objetivo_label = ttk.Label(root, text="XP Objetivo: ")
xp_objetivo_label.pack()

xp_objetivo_entry = ttk.Entry(root, textvariable=xp_objetivo)
xp_objetivo_entry.pack()


# recibir el XP por intervalo
xp_intervalo = tk.IntVar()

xp_intervalo_label = ttk.Label(root, text="XP por intervalo: ")
xp_intervalo_label.pack()

xp_intervalo_entry = ttk.Entry(root, textvariable=xp_intervalo)
xp_intervalo_entry.pack()


# recibir el tiempo de intervalo
tiempo = tk.IntVar()

tiempo_label = ttk.Label(root, text="Tiempo de intervalo: ")
tiempo_label.pack()

tiempo_entry = ttk.Entry(root, textvariable=tiempo)
tiempo_entry.pack()


# Calcular Tiempo
def CalcularTiempo():
    segundos = ((xp_objetivo.get()-xp_actual.get())*tiempo.get())//xp_intervalo.get()
    minutos = 0
    horas = 0

    while segundos >= 60:
        minutos += 1
        segundos -= 60

    while minutos >= 60:
        horas += 1
        minutos -= 60
    
    ttk.Label(root,text=f'{horas}h {minutos}m {segundos}s').pack()

calcular_boton = ttk.Button(root, text="Calcular", command=CalcularTiempo)
calcular_boton.pack()

root.mainloop()