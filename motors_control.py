import time

#стартовая позиция (широта)
position = 66.1233251
#скорость(км/ч)
velocity = 10;
#нормировочный коэффициент скорости
velocity_delimiter = 0.0001;
while True:
    time.sleep(1)
    print ("we fly at: ", position)
    position += velocity * velocity_delimiter
