import requests
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('400x400')
root.title('Weather Forecast')
root.resizable(width=False, height=False)

# Set the background image
background_image = Image.open('weather_background.png')
background_image = background_image.resize((400, 400), Image.BILINEAR) 
background_image = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Replace 'API_KEY' with actual API key
api_key = 'API_KEY'  

def get_weather():
    city = input_city_box.get()
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    
    # Make the API request
    response = requests.get(base_url)
    data = response.json()
    
    # Process the weather data
    if response.status_code == 200:
        weather = data['weather'][0]['main']
        desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        max_temp = data['main']['temp_max']
        min_temp = data['main']['temp_min']
        wind = data['wind']['speed']
        display_label.config(text=f"Weather: {weather}\n"+
                                  f"Description: {desc}\n"+
                                  f"Temperature: {temperature}°C\n"+
                                  f"Humidity: {humidity}%\n"+
                                  f"Max Temp: {max_temp}°C\n"+
                                  f"Min Temp: {min_temp}°C\n"+
                                  f"Wind Speed: {wind}m/s")
    else:
    	display_label.config(text='Error: ' + data['message'])

header = Label(root, text='Weather Forecast Tool', font=("Times New Roman", "24"), bg="white")
header.pack()

input_city = Label(root, text="Enter City", font=("Times New Roman", "20"), bg="white")
input_city.pack()
input_city_box = Entry(root, font=("Times New Roman", "18"))
input_city_box.pack()

get_weather = Button(root, text="Get Weather", font=("Times New Roman", "14"), command=get_weather)
get_weather.pack()

display_label = Label(root, font=("Times New Roman", "16"))
display_label.pack()

exit = Button(root, text="Exit",font=("Times New Roman", "14"), command=exit)
exit.pack()
root.mainloop()
