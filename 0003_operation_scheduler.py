# 시간과 전원 상태를 동시에 고려하는 복합 조건문을 설계하세요.
# Design a complex conditional statement that considers both time and power status.

# Scenario
# 전시장 내 시스템을 자동화. 작품은 다음 두가지의 조건이 모두 충족될 때만 작동.
# 전원상태가 켜져있을 때. 운영시간이 오전 10시부터 오후 6시 사이일 때.

power_on = True
current_hour = 14

def check_system():
    if power_on and 10 <= current_hour < 18:
        print("check_system('activate')")
    else:
        print("check_system('deactivate')")

check_system()