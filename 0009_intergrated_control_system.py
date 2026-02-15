# 안전, 프라이버시, 배터리 상태를 종합적으로 판단하여 시스템의 최종 동작을 결정하는 통합 제어 시스템

# Scenario
# 1. 비상 여부(is_emergency), 프라이버시 모드(is_privacy)를 불리언으로 설정.
# 2. 배터리 잔량(battery_level)을 정수로 설정.
# 3. 함수(master_control)에 위 3가지 값을 매개변수로 전달할 것.
# 4. 우선순위에 따라 if-elif-else 로직을 구현할 것.
#    - [1순위] 비상 상황이면 -> "CRITICAL: Emergency Stop!"
#    - [2순위] 프라이버시 모드이면 -> "Privacy Active: Cameras OFF"
#    - [3순위] 배터리가 20 미만이면 -> "Low Battery: Saving Mode"
#    - [4순위] 모두 해당 없으면 -> "System Normal: Recording..."

emergency_status = False
privacy_mode = False
battery_level = 15

def master_control(emergency_status, privacy_mode, battery_level):
    if emergency_status:
        print("CRITICAL: Emergency Stop!"
    elif privacy_mode:
        print("Privacy Active: Cameras OFF"
    elif battery_level < 20:
        print("Low Battery: Saving Mode")
    else:
        print("System Normal: Recording...")

master_control(emergency_status, privacy_mode, battery_level)