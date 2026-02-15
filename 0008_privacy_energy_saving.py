# 프라이버시 모드가 켜져 있다면, 움직임이 감지되어도 녹화하지 않고 절전 상태를 유지하는 시스템

# Scenario
# 프라이버시 모드 활성화 여부(is_privacy_mode)를 불리언(True/False) 변수로 설정할 것.
# 움직임 감지 여부(motion_detected)를 불리언(True/False) 변수로 설정할 것.
# 함수(manage_privacy)를 정의할 때, 위 두 값을 전달받을 매개변수(privacy, motion)를 괄호 안에 작성할 것.
# 논리 연산자(not)와 if-elif-else를 사용하여 다음 로직을 구현할 것.
#  - 프라이버시 모드가 켜져(True) 있다면 -> "Privacy Mode ON: Recording Disabled" 출력
#  - 프라이버시 모드가 꺼져(not) 있고(and), 움직임이 감지(True)되면 -> "Motion Detected: Recording Started" 출력
#  - 나머지 경우 -> "System Standby (Energy Saving)" 출력

privacy_mode = True
motion_detected = True

def manage_privacy(privacy_mode, motion_detected):
    if privacy_mode:
        print("Privacy Mode ON: Recording Disabled")
    elif not privacy_mode and motion_detected:
        print("Motion Detected: Recording Started")
    else:
        print("System Standby (Energy Saving)")

manage_privacy(privacy_mode, motion_detected)