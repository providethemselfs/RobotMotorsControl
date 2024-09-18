import time

#стартовая позиция (широта)
position = 66.1233251
#скорость(км/ч)
velocity = 20;
#нормировочный коэффициент скорости
velocity_delimiter = 0.00005;
while True:
    time.sleep(0.5)
    print ("we fly at: ", position)
    position += velocity * velocity_delimiter
