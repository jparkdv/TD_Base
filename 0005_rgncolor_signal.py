# 장비 보호를 위한 유효 RGB 색상 신호 검증 및 안전 장치 시스템을 구현합니다.
# Implement a validation and safety system for RGB color signals to protect hardware equipment.

# Scenario
# 디지털 예술에서 색은 보통 (R, G, B) 세 숫자의 조합으로 표현.
# 각 값은 0.0에서 1.0 사이. 
# 만약 어느 하나라도 1.0을 초과하거나 0.0 미만이라면 "Invalid Color"라는 경고를 띄워야 장비 고장을 막을 수 있음.

def check_color_signal(r, g, b):
    if 0.0 <= r <= 1.0 and 0.0 <= g <= 1.0 and 0.0 <= b <= 1.0:
        print("color_signal : OK")
    else:
        print("color_signal : Invalid Color ")

check_color_signal(1.0, 0.5, 0.2)
