# 장비 전원 상태와 배터리 잔량을 계층적으로 관리하는 복합 조건 시스템을 설계합니다.
# Design a complex conditional system for hierarchical management of power status and battery levels.

# Scenario
# 메인 전원(power_on)의 활성화 여부를 최우선으로 판별할 것.
# 전원 인가 상태(True)에 한하여 배터리 모니터링 로직을 가동할 것.
# 배터리 20% 이하 감지 시, 시스템 보호를 위한 '절전 모드' 신호를 발생시킬 것.
# Prioritize verifying the activation status of the main power.
# Activate battery monitoring logic only when power is active.
# Trigger a 'Power Save Mode' signal for system protection below 20% battery.



def manage_power(power_on, battery_level):
    if power_on:
        if battery_level <= 20:
            print("manage_power('activate_power_save_mode')")
        else:
            print("manage_power('normal_operation')")
    else:
        print("manage_power('system_off')")

manage_power(True, 15)