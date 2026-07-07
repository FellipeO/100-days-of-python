#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
import flight_search
import notification_manager
import datetime as dt
import flight_data

my_manager = data_manager.DataManager()
my_search = flight_search.FlightSearch()
users = my_manager.get_customer_emails()
tomorrow = dt.datetime.now() + dt.timedelta(days=1)
six_months_from_today = dt.datetime.now() + dt.timedelta(weeks=24)

for destination in my_manager.read_data()["prices"]:
    print(f"Searching for direct flights from LHR to {destination["iataCode"]}...")
    flights = my_search.check_flights("LHR", destination["iataCode"], tomorrow, six_months_from_today, "1")
    if not flights:
        print(f"Searching for non-direct flights from LHR to {destination["iataCode"]}")
        flights = my_search.check_flights("LHR", destination["iataCode"], tomorrow, six_months_from_today, "")
    cheapest_flight = flight_data.find_cheapest_flight(flights, six_months_from_today)
    if int(destination["lowestPrice"]) > int(cheapest_flight.price):
        print(f"{destination["iataCode"]}: {cheapest_flight.price}")
        for user in users["users"]:
            my_notification_manager = notification_manager.NotificationManager()
            my_notification_manager.send_message(cheapest_flight, destination["iataCode"], user["email"])
        my_manager.update_sheet(cheapest_flight.price, destination["iataCode"])
    else:
        print(f"{destination["iataCode"]}: {destination["lowestPrice"]}")
