from Fan_class import Fan, FanData
fan1_data = FanData(speed = 3, radius = 10, color = "yellow", on = True) 
fan1 = Fan(fan1_data)
print(fan1.color, fan1.speed, fan1.radius, fan1.on)