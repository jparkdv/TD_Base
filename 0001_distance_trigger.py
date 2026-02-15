# 관객의 거리에 반응하는 기초 인터랙션 시스템

# Scenario
# 관람객과의 거리(visitor_distance)를 실시간으로 측정하는 변수를 설정할 것.
# 작품이 반응할 기준 거리(threshold_distance)를 정할 것.
# 관람객이 기준보다 가까이 오면 작품을 재생(start)하고, 아니면 정지(stop)하는 로직을 함수로 구현할 것.

visitor_distance = 1.0
threshold_distance = 1.2

def play_artwork(visitor_distance, threshold_distance):
    if visitor_distance < threshold_distance:
        print("play_artwork('start')")
    else:
        print("play_artwork('stop')")

play_artwork(visitor_distance, threshold_distance)