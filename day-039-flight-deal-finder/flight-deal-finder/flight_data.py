
class FlightData:
    # This class is responsible for structuring the flight data.
    def get_best_offer(self, flight):
        cheapest_flight = flight[0]['flightPrice']
        cheapest_flight_index = 0

        for flight_index in range(len(flight)):
            if flight[flight_index]['flightPrice'] < cheapest_flight:
                cheapest_flight = flight[flight_index]['flightPrice']
                cheapest_flight_index = flight_index
        print(flight[cheapest_flight_index])
        return flight[cheapest_flight_index]
