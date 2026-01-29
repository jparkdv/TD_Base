# 다중 센서 데이터를 분석하여 시스템의 즉각적인 비상 정지를 제어하는 통합 안전 로직을 설계합니다.
# Design an integrated safety logic to control immediate emergency shutdown by analyzing multi-sensor data.

# Scenario
# 전시장 온도(temp)와 연기 감지(smoke_detected) 데이터를 실시간 모니터링할 것.
# 온도가 50도 이상이거나 연기가 감지되는 경우(하나라도 해당 시), 비상 정지 신호를 발생시킬 것.
# 모든 조건이 안전 범위 내에 있을 경우에만 시스템 정상 가동 상태를 유지할 것.

# Monitor gallery temperature and smoke detection data in real-time.
# Trigger an emergency stop signal if temperature is 50°C or above, OR smoke is detected.
# Maintain normal operation only when all conditions are within the safety range.

def emergency_safety_system(temp, smoke_detected):
    if temp >= 50 or smoke_detected:
        print("emergency_safety_system('EMERGENCY STOP')")
    else:
        print("emergency_safety_system('NORMAL OPERATION')")

emergency_safety_system(55, False)
emergency_safety_system(45, True)