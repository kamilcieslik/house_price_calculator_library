import unittest
from calculator import exception
from calculator.prices_calculator import PricesCalculator
from calculator.util.address import Address
from datetime import datetime


class TestStringMethods(unittest.TestCase):

    def test_too_small_value_of_year(self):
        calc = PricesCalculator("AIzaSyBEmx5P3vl4ox4OU6nPgwTbU9k-_0Zm6Lo")
        address = Address("", 49.95153, 18.609122)
        calc.selected_address = address

        with self.assertRaises(
                exception.ConstructionYearViolationException) as context:
            calc.calculate_house_price("blok", "pierwotny", "cegła",
                                       1500, 25, False, False, False,
                                       True, True, False, False)

        self.assertTrue(
            'rok budowy nie może być mniejszy niż 1900' in str(context.exception))

    def test_too_big_value_of_year(self):
        calc = PricesCalculator("AIzaSyBEmx5P3vl4ox4OU6nPgwTbU9k-_0Zm6Lo")
        address = Address("", 49.95153, 18.609122)
        calc.selected_address = address

        datetime_now_year = datetime.today().year
        with self.assertRaises(
                exception.ConstructionYearViolationException) as context:
            calc.calculate_house_price("blok", "pierwotny", "cegła",
                                       datetime_now_year + 1, 25, False, False,
                                       False,
                                       True, True, False, False)

        self.assertTrue(
            'rok budowy nie może być większy niż obecny' in str(context.exception))

    def test_mismatch_building_type(self):
        calc = PricesCalculator("AIzaSyBEmx5P3vl4ox4OU6nPgwTbU9k-_0Zm6Lo")
        address = Address("", 49.95153, 18.609122)
        calc.selected_address = address

        building_type = "bloks"
        with self.assertRaises(
                exception.FlatParameterMismatchException) as context:
            calc.calculate_house_price(building_type, "pierwotny", "cegła",
                                       2000, 25, False, False, False,
                                       True, True, False, False)

        self.assertTrue(
            "wskazany rodzaj zabudowy '" + building_type + "' nie istnieje"
            in str(context.exception))

    def test_mismatch_market_type(self):
        calc = PricesCalculator("AIzaSyBEmx5P3vl4ox4OU6nPgwTbU9k-_0Zm6Lo")
        address = Address("", 49.95153, 18.609122)
        calc.selected_address = address

        market_type = "pierwotFny"
        with self.assertRaises(
                exception.FlatParameterMismatchException) as context:
            calc.calculate_house_price("blok", market_type, "cegła",
                                       2000, 25, False, False, False,
                                       True, True, False, False)

        self.assertTrue(
            "wskazany rodzaj rynku '" + market_type + "' nie istnieje"
            in str(context.exception))

    def test_name_of_reference_city(self):
        calc = PricesCalculator("AIzaSyBEmx5P3vl4ox4OU6nPgwTbU9k-_0Zm6Lo")
        address = Address("", 50.8118195, 19.1203094)  # Częstochowa
        calc.selected_address = address

        calculator_result = calc.calculate_house_price("blok", "pierwotny", "cegła",
                                                       2000, 25, False, False, False,
                                                       True, True, False, False)

        self.assertEqual(calculator_result.nearest_reference_city.name, "Katowice")


if __name__ == '__main__':
    unittest.main()
