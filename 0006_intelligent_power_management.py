# 현재 배터리 잔량에 따라 장비의 성능 모드를 자동으로 전환하여 전시 운영 효율을 높이는 시스템

# Scenario
# 현재 배터리 잔량(battery_level)을 정수형 변수로 설정할 것. (예: 15, 50, 90 등)
# 함수를 정의할 때 배터리 잔량 값을 전달받을 매개변수(level)를 괄호 안에 작성할 것.
# if-elif-else를 사용하여 배터리 잔량에 따른 모드를 출력할 것.
#  - 배터리가 80 초과(>)이면 "High Performance Mode"
#  - 배터리가 20 이상(>=) 80 이하(<=)이면 "Standard Mode"
#  - 그 외(20 미만)이면 "Power Saving Mode"

power_on = True
battery_level = 15

def manage_power(power_on, battery_level):
    if power_on:
        if battery_level > 80:
            print("manage_power('High Performance Mode')")
        elif battery_level >= 20 and battery_level <= 80:
            print("manage_power('Standard Mode')")
        else:
            print("manage_power('Power Saving Mode')")
    else:
        print("manage_power('Device is Off')")

manage_power(True, battery_level)