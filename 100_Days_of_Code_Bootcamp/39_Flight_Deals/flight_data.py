class FlightData:
    def __init__(self,
                 given_price,
                 given_origin_city,
                 given_origin_airport,
                 given_destination_city,
                 given_destination_airport,
                 given_out_date,
                 given_return_date):

        self.price = given_price
        self.origin_city = given_origin_city
        self.origin_airport = given_origin_airport
        self.destination_city = given_destination_city
        self.destination_airport = given_destination_airport
        self.out_date = given_out_date
        self.return_date = given_return_date
