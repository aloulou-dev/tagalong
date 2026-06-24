import unittest
from weather_api import get_weather_forecast

class TestWeatherAPI(unittest.TestCase):
    def test_weather_returns_data(self):
        result = get_weather_forecast("New York", "2026-06-24", "2026-06-26")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

    #verify a 3-day trip returns 3 weather entries
    def test_weather_trip_length(self):
        result = get_weather_forecast("New York", "2026-06-24", "2026-06-26")
        self.assertEqual(len(result), 3)

    #test each weather record conatins the expected fields
    def test_weather_has_required_keys(self):
        result = get_weather_forecast("New York", "2026-06-24", "2026-06-26")
        first_day = result[0]

        self.assertIn("date", first_day)
        self.assertIn("condition", first_day)
        self.assertIn("avg_temp_f", first_day)

if __name__ == "__main__":
    unittest.main()