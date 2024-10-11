from tkinter import *
import requests


def get_info():
    res = field.get()

    key = 'какой-то ключ'
    url = 'какой-то url'
    params = {'APPID': key, 'q': res, 'units': 'imperial'}
    result = requests.get(url, params=params)
    weather = result.json()

    # print(weather)

    info['text'] = f"{str(weather['name'])}: {weather['main']['temp']}"

root = Tk() # Создание окна
root['bg'] = '#fafafa'
root.title = 'Название приложения'
root.geometry('300x250')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwigth=0.7, relheight=0.25)

frame_button = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.55, relwigth=0.7, relheight=0.1)

field = Entry(frame_top, bg='white', font=30)
field.pack()

btn = Button(frame_top, text='Посмотреть ответ')
btn.pack()

info = Label(frame_button, text='Информация', bg='#ffb700', font=40)
info.pack()

root.mainloop() # Запуск постоянного цикла