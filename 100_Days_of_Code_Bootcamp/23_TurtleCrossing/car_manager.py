from car import Car


class CarManager:
    def __init__(self):
        self.cars = []
        for car in range(0, 10):
            self.car_1 = Car()
            self.cars.append(self.car_1)

    def move_cars(self):
        for car in self.cars:

            if car.xcor() < -225:
                car.set_random_y()

            car.move()

    def check_if_hit_player(self, player):
        for car in self.cars:

            if car.distance(player) < 30:
                print("Hit")
                return True
            else:
                return False
