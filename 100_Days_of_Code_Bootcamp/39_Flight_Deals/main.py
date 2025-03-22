from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager

ORIGIN_CITY_IATA_CODE = "LON"

new_fly_search = FlightSearch()
new_data_manager = DataManager()
sheet_data = new_data_manager.get_sheet_data()

tomorrow = datetime.now()
six_months_from_today = datetime.now() + timedelta(days=180)

for line_data in sheet_data:
    line_data['iataCode'] = new_fly_search.get_destination_code(line_data['city'])
    # new_data_manager.update_line(line_data)

for line_data in sheet_data:
    new_data_manager.update_line(line_data)

print(sheet_data)
