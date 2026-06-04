class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self) -> None:
        self.__speed += 5
        return 0
    
    def brake(self) -> None:
        self.__speed -= 5
        return 0
    
    def get_speed(self) -> float:
        return self.__speed