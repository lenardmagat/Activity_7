from Fan_class import Fan

fan1 = Fan()
fan1.set_speed(Fan.FAST)
fan1.set_radius(10.0)
fan1.set_color("Yellow")
fan1.set_on(True)

fan2 = Fan()
fan2.set_speed(Fan.MEDIUM)
fan2.set_radius(5.0)
fan2.set_color("Blue")
fan2.set_on(False)

print(f"fan1: speed: {fan1.get_speed()}, radius: {fan1.get_radius()}, color: {fan1.get_color()}, on: {fan1.get_on()}")
print(f"fan1: speed: {fan2.get_speed()}, radius: {fan2.get_radius()}, color: {fan2.get_color()}, on: {fan2.get_on()}")