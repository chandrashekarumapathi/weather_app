import tkinter as tk
import requests
import time


# Defining a function to get data from API
def get_weather(canvas):
    city = textfield.get()
    api = f'http://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID=bbd2ffb9da433cea1b774cfe5c32c0b9'
    json_data = requests.get(api).json()
    # condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    temp_min = int(json_data['main']['temp_min'] - 273.15)
    temp_max = int(json_data['main']['temp_max'] - 273.15)
    feels_like = int(json_data['main']['feels_like'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 3600))
    sunset = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunset'] - 3600))

    final_info = str(temp) + '°C'
    final_data = '\n' + 'Minimum Temperature: ' + str(temp_min) + '°C' + '\n' + 'Maximum Temperature: ' + str(temp_max) + '°C' + '\n' + "Feels like: " + str(feels_like) + '°C' + '\n' + 'Pressure: ' + str(pressure) + '\n' + 'Humidity: ' + str(humidity) + '\n' + 'Wind Speed: ' + str(wind) + '\n' + 'Sunrise Time: ' + sunrise + '\n' + 'Sunset Time: ' + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)



# Defining User Interface
canvas = tk.Tk()

# Setting the geometry of the canvas
canvas.geometry("600x500")

# Defining the title of our canvas
canvas.title("Weather App")

# Creating few fonts
f = ('poppins', 15, 'bold')
t = ('poppins', 35, 'bold')

# Defining a text field to get input from user
textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', get_weather)

# Creating labels to show data
label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()

