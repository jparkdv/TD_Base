# 관객 부재시의 에너지 절감 시스템을 구축합니다.

# Scenario
# 관객 감지여부 체크.
# 관객이 감지되지 않았을 때만 "Saving Energy" 신호를 발생시킬 것.
# 관객이 감지되면 "Full Operation" 신호를 발생시킬 것

audienvce_detected = True   

def privacy_energy_saving(audience_detected):
    if not audience_detected:
        print("Saving Energy")
    else:
        print("Full Operation")

privacy_energy_saving(False)