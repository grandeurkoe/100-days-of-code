from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

DEPARTURE_CITY = "London"

flight_sheet_data = DataManager()
flight_search = FlightSearch()
flight_structure_data = FlightData()
flight_notification = NotificationManager()

cities = flight_sheet_data.get_column('city')
lowest_prices = flight_sheet_data.get_column('lowestPrice')

iata_codes = flight_search.get_iata_code(cities, 'city')
departure_iata_code = flight_search.get_iata_code([DEPARTURE_CITY], 'city')

# flight_data.update_column(iata_codes, 'iataCode')

cheapest_flights = flight_search.get_cheapest_flight(departure_iata_code, iata_codes, lowest_prices, DEPARTURE_CITY, cities)

best_offer = flight_structure_data.get_best_offer(cheapest_flights)

# flight_notification.sms_best_offer(best_offer)
