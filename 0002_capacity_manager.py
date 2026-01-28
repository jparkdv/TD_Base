# 전시장 내 인원을 관리하여 안전을 보장하는 시스템을 구축하세요.
# Build a system that manages the number of people inside a gallery to ensure safety.

# Scenario
# 전시공간이 협소하여 동시 입장객을 10명으로 제한해야 합니다.
# 현재 센서가 전시장 안에 몇 명이 있는지 실시간으로 알려주고 있습니다.

current_visitors = 12
max_capacity = 10

def manage_capacity():
    if current_visitors > max_capacity:
        print("manage_capacity('deny_entry')")
    else:
        print("manage_capacity('allow_entry')")

manage_capacity()