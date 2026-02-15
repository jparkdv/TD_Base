# 전원 상태와 운영 시간이라는 두 가지 서로 다른 데이터를 동시에 판단하여 시스템의 활성화 여부를 결정

# Scenario
# 시스템의 전원 상태(power_on)를 불리언(True/False)으로 설정할 것.
# 현재 시각(current_hour)을 24시간 형식의 정수로 설정할 것.
# 논리 연산자(and)를 사용하여 전원이 켜져 있고, 시간이 10시~18시 사이일 때만 작동(activate)하도록 설계할 것.
# 두 조건 중 하나라도 맞지 않으면 비활성화(deactivate)할 것.

power_on = True
current_hour = 14

def check_system(power_on, current_hour):
    if power_on and 10 <= current_hour < 18:
        print("check_system('activate')")
    else:
        print("check_system('deactivate')")

check_system(power_on, current_hour )