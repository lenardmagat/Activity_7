class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, on: bool = False, radius: float = 5, color: str = "blue"):
        self.speed = speed 
        self.on = on
        self.radius = radius
        self.color = color

    @property
    def speed(self) -> int:
        return self.__speed
    
    @speed.setter 
    def speed(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Speed must be an integer")
        if value not in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            raise ValueError("Speed must be Slow(1), Medium(2), Fast(3)")
        self.__speed = value

    