class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data, return_date):
    if data is None:
        return FlightData("None", "None", "None", "None", "None")

    best_flights = [flights for flights in data["best_flights"]]
    other_flights = [flights for flights in data["other_flights"]]
    flights_list = best_flights + other_flights

    cheapest_flight = flights_list[0]
    for item in flights_list:
        if item["price"] < cheapest_flight["price"]:
            cheapest_flight = item
    return FlightData(cheapest_flight["price"],
                      cheapest_flight["flights"][0]["departure_airport"]["name"],
                      cheapest_flight["flights"][0]["arrival_airport"]["name"],
                      cheapest_flight["flights"][0]["departure_airport"]["time"],
                      return_date,
                      len(cheapest_flight["flights"])-1)





