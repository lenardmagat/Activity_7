class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self, speed: int = SLOW, radius: float = 5.0, color: str = "blue", on: bool = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self) -> int:
        return self.__speed
    
    def set_speed(self, speed: int) -> None:
        if speed not in [self.SLOW, self.MEDIUM, self.FAST]:
            return print("Invalid input.")
        self.__speed = speed
        return 0
    
    def get_radius(self) -> float:
        return self.__radius
    
    def set_radius(self, radius: float) -> None:
        if radius <= 0: return print("Invalid Output.")
        self.__radius = radius
        return 0

    def get_color(self) -> str:
        return self.__color
    
    def set_color(self, color: str) -> None:
        self.__color = color
        return 0

    def get_on(self) -> bool:
        return self.__on
    
    def set_on(self, on: bool) -> None:
        self.__on = on
        return 0 