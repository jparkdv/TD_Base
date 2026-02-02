# 관객의 거리에 반응하는 기초 인터랙션 시스템을 구축합니다.
# Establish a foundational interaction system that responds to audience proximity.

# Scenario
# 전시장에 인터랙티브 미디어아트 작품을 설치.
# Install an interactive media art piece in the exhibition hall.
# 센서가 관람객과의 거리를 실시간으로 측정.
# The sensor measures the distance to the visitor in real time.
# 관람객이 1.2미터보다 가까이 오면 작품이 재생.
# The artwork begins playback when a visitor approaches within 1.2 meters.

visitor_distance = 1.0
threshold_distance = 1.2

def play_artwork(action):
    if visitor_distance < threshold_distance:
        print("play_artwork('start')")
    else:
        print("play_artwork('stop')")

play_artwork("start")