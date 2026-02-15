# 조명의 밝기 수치에 따라 현재 조명의 상태가 표준인지, 정밀조정이 필요한 단계인지 판별하는 시스템

# Scenario
# 목표로 하는 밝기(target_brightness)와 현재 감지된 밝기(current_brightness)변수를 설정할 것.
# 현재 밝기가 목표치보다 낮으면 조명을 더 밝게(increase) 만들 것.
# 목표치에 도달했거나 높다면 현재 상태를 유지(maintain)할 것.
# 비교 결과를 바탕으로 명령어를 출력하는 매개변수 기반 함수를 구현할 것.

target_brightness = 0.75
current_brightness = 0.45

def check_lighting(current_brightness, target_brightness):
    if current_brightness < target_brightness:
        print("check_lighting('increase')")
    else:
        print("check_lighting('maintain')")

check_lighting(current_brightness, target_brightness)