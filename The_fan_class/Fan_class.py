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
    
    


        
    

    