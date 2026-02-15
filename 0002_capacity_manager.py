# 전시장 내 실시간 인원을 관리하여 공간이 수용할 수 있는 한계치를 넘지 않도록 자동으로 통제하는 시스템

# Scenario
# 현재 전시장 안에 있는 관객 수(current_visitors)를 정수형 변수로 설정할 것.
# 전시장이 수용 가능한 최대 인원(max_capacity)을 10명으로 제한할 것.
# 만약(if) 현재 인원이 최대치를 초과(>)하면 입장을 거부(deny_entry)하고, 그렇지 않으면 허용(allow_entry)하는 로직을 함수로 구현할 것.

current_visitors = 12
max_capacity = 10

def manage_capacity(current_visitors, max_capacity):
    if current_visitors > max_capacity:
        print("manage_capacity('deny_entry')")
    else:
        print("manage_capacity('allow_entry')")

manage_capacity(current_visitors, max_capacity)