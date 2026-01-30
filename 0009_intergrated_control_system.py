# 전시 운영 조건과 비상 상황을 동시에 분석하는 통합 제어 시스템을 설계합니다.

# Scenario
# 전시장 운영상태와 비상상태를 나눔.
# 전시장이 운영중이고, 비상상황이 아닐 때만 "System Active" 신호를 발생시킬 것.
# 비상상황이 발생하면 "EMERGENCY STOP" 신호를 우선 발생시킬 것.
# 전시장에 관객이 없을 때는 "Idle Mode" 신호를 발생시킬 것.
# 가장 위험한 상황을 맨 위로 올리는 것이 안전 설계임.

operational = True
emergency = False
audoience_detected = False

def integrated_control_system(operational, emergency, audience_detected):
    if emergency:
        print("EMERGENCY STOP")
    elif operational:
        if audience_detected:
            print("System Active")
        else:
            print("Idle Mode")
    else:
        print("Idle Mode")