import math

sequence = list(map(int, input().split(" ")))
total_length = len(sequence)
finish = math.floor(total_length / 2)

total_time_firstCar = 0
total_time_secondCar = 0

for i in range(0, finish):
    f_car_time = sequence[i]
    s_car_time = sequence[total_length - 1 - i]

    if f_car_time == 0:
        total_time_firstCar *= 0.80

    if s_car_time == 0:
        total_time_secondCar *= 0.80

    total_time_firstCar += f_car_time
    total_time_secondCar += s_car_time

winner = min(total_time_firstCar, total_time_secondCar)
left_or_right = "right" if total_time_firstCar > total_time_secondCar else "left"

print(f"The winner is {left_or_right} with total time: {winner:.1f}")