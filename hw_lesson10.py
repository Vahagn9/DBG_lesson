class Vehicle:
    def __init__(self, max_speed, time_to_100):
        self.max_speed = max_speed
        self.time_to_100 = time_to_100

    def acceleration(self):
        return 27.78 / self.time_to_100  # converted speed 100 km/h to 27.78 m/s


class Bmw(Vehicle):
    def __init__(self, max_speed=290, bmw_time_to_100=4):
        super().__init__(max_speed, bmw_time_to_100)


class Mercedes(Vehicle):
    def __init__(self, max_speed=300, mers_time_to_100=5):
        super().__init__(max_speed, mers_time_to_100)


car1 = Bmw(250, 6)
car2 = Mercedes(320, 3)
car3 = Bmw()
car4 = Mercedes()
print(f'car1 acceleration is : {car1.acceleration()}')
print(f'car1 max speed is : {car1.max_speed}')
print(f'car2 acceleration is : {car2.acceleration()}')
print(f'car2 max speed is : {car2.max_speed}')
print(f'car3 acceleration is : {car3.acceleration()}')
print(f'car3 max speed is : {car3.max_speed}')
print(f'car4 acceleration is : {car4.acceleration()}')
print(f'car4 max speed is : {car4.max_speed}')
