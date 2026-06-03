from .Schema import FanData
from .Helper import ReturnValue
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self, FanData: FanData):
        self.speed = FanData.speed 
        self.on = FanData.on
        self.radius = FanData.radius
        self.color = FanData.color

    @speed.setter 
    def speed(self, value: int):
        if not isinstance(value, int):
            return ReturnValue.failure("Speed must be an integer")
        if value not in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            return ReturnValue.failure("Speed must be Slow(1), Medium(2), Fast(3)")
        self.__speed = value
    
    @property
    def speed(self) -> ReturnValue:
        ReturnValue.success(self.__speed)
    
    @on.setter
    def on(self, value: bool):
        if not isinstance(value, bool):
            return ReturnValue.failure("On must be a bool")
        self.__on = self.on

    @property
    def on(self) -> ReturnValue:
        ReturnValue.success(self.__on)
         
    @radius.setter
    def radius(self, value: float):
        if not isinstance(value, float):
            return ReturnValue.failure("Radius must be a float")
        if value < 0:
            return ReturnValue.failure("Radius must be greater than 0")
        self.__radius = self.radius
    
    @property
    def radius(self) -> ReturnValue:
        return ReturnValue.success(self.__radius)
    
    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            return ReturnValue.failure("color must be string")
        self.__color = self.color

    @property
    def color(self) -> ReturnValue:
        return ReturnValue.success(self.__color)
    


        
    

    