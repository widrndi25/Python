import math


def calculate_sound_velocity(temperature):
    global sound_speed
    sound_speed = 20.05 * math.sqrt(temperature + 273)
    return print("현재 소리의 속도는 " + str(round(sound_speed, 2)) + " m/s입니다")


def calculate_distance(time):
    distance = sound_speed * time
    return print("그렇다면 낙뢰 위치까지는 " + str(round(distance, 2)) + " m 떨어져 있겠네요")


tem = int(input("현재 온도를 입력해 주세요(섭씨단위로 숫자만 적으세요) : "))

calculate_sound_velocity(tem)

time = int(input("천둥 소리가 몇초 뒤에 들렸나요?(숫자만 적으세요) : "))

calculate_distance(time)
