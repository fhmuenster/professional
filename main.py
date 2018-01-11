import time
import fischertechnik.factories as f

c = f.controller_factory.create_graphical_controller()
l = f.output_factory.create_lamp(c, 1)

while True:
    l.set_brightness(255)
    time.sleep(1)
    l.set_brightness(0)
    time.sleep(1)