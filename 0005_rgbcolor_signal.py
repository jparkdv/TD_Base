# 현재 시스템의 상태(정상, 경고 등)를 입력받아, 그에 맞는 RGB 색상 데이터를 출력한다.

# Scenario
# 시스템의 상태를 나타내는 변수(system_status)를 설정할 것.
# 함수를 정의할 때 상태 값을 전달받을 매개변수(status)를 괄호 안에 작성할 것.
# if-elif-else를 사용하여 각 상태에 맞는 RGB 튜플(Tuple) 값을 결정하고 출력할 것.

system_status = "warning"

def set_rgb_color(status):
    if status == "normal":
        print("set_rgb_color((0, 255, 0))")  # 녹색
    elif status == "warning":
        print("set_rgb_color((255, 255, 0))")  # 노란색
    elif status == "error":
        print("set_rgb_color((255, 0, 0))")  # 빨간색
    else:
        print("set_rgb_color((255, 255, 255))")  # 흰색 (알 수 없는 상태)
