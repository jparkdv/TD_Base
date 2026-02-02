# 미디어 아트 조명의 미세 제어를 위한 정밀 데이터(Float) 처리 시스템을 구축합니다.
# Establish a precision data (Float) processing system for fine-tuned media art lighting control.

## Scenario
# 미디어 아트 조명 시스템에서 밝기는 0.0(꺼짐)에서 1.0(최대) 사이로 조절.
# 현재 밝기가 목표치보다 낮으면 조명을 높이고, 도달하면 유지.

target_brightness = 0.75
current_brightness = 0.45

def adjust_lighting(current_brightness, target_brightness):
    if current_brightness < target_brightness:
        print("adjust_lighting('increase')")
    else:
        print("adjust_lighting('maintain')")

adjust_lighting(current_brightness, target_brightness)