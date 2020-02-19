import unittest

from personalprojects.Digi24.Pages.Digi24_Home import Defs

class TestWeather(unittest.TestCase):

    weather = Defs()
    weather.load()
    weather.get_weather_header_name()
    weather.get_weather_values()
    weather.quit()

if __name__ == "__main__":
    unittest.main()