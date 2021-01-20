import tkinter as tkinter 
from tkinter import font
import requests

HEIGT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:",entry)

#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={API key}


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str= "There was a problem retrieving that information"
    return final_str

def get_weather(city):
    weather_kye ='6195ea558f91684ddebeddf41d914098'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_kye, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tkinter.Tk()

canvas = tkinter.Canvas(root, height=HEIGT, width=WIDTH)
canvas.pack()

background_image = tkinter.PhotoImage(file='landscape.png.png')
background_label = tkinter.Label(root, image=background_image)
background_label.place(relheight=1)


frame = tkinter.Frame(root, bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = tkinter.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tkinter.Button(frame, text="Get Weather",font=40,command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame = tkinter.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')


label = tkinter.Label(lower_frame,font=('Modern,30'))
label.place(relwidth=1,relheight=1)

print(tkinter.font.families())

root.mainloop()