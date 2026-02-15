# 다중 센서 데이터를 분석하여 시스템의 즉각적인 비상 정지를 제어하는 통합 안전 시스템
# 화재 감지 센서나 지진 센서가 작동하면, 시스템의 다른 상태와 상관없이 즉시 운영을 중단한다.

# Scenario
# 비상 상황 여부(emergency_status)를 불리언(True/False) 변수로 설정할 것.
# 현재 시스템 모드(system_mode)를 문자열 변수로 설정할 것. (예: "Operation", "Maintenance" 등)
# 함수(check_safety)를 정의할 때, 위 두 값을 전달받을 매개변수(emergency_status, mode)를 괄호 안에 작성할 것.
# if-elif-else를 사용하여 안전 수칙을 구현할 것.
#  - 만약 비상 상황(True)이라면 -> "EMERGENCY STOP! System Halted." 출력
#  - 비상이 아니고, 모드가 "Operation"이라면 -> "Normal Operation Continuing..." 출력
#  - 나머지 경우 -> "System Idle / Maintenance Mode" 출력

emergency_status = True
system_mode = "Operation"

def check_safety(emergency_status, system_mode):
    if emergency_status:
        print("EMERGENCY STOP! System Halted.")
    elif system_mode == "Operation":
        print("Normal Operation Continuing...")
    else:
        print("System Idle / Maintenance Mode")

check_safety(emergency_status, system_mode)