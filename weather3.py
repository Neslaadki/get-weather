import pyown


def weather(place):
    if place == "Exit":
        exit(0)
    else:
        owm = pyowm.OWM('a25b6ba061d2fea55447080b88118f3f', language='ru')

        place = input(' Привет, в каком городе хочешь узнать погоду? ')  # укажи город без пробела

        observation = owm.weather_at_place(place)
        w = observation.get_weather()

        temperature = w.get_temperature('celsius')['temp']

        print(" В городе " + place + " сейчас " + str(temperature) + " по цельсию ")
        print(" В этом городе " + w.get_detailed_status() + ", оденься нормально, плез!  ")
        weather(place)


weather(place)
