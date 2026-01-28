# 사람이 작품 앞에 다가왔을 때 반응하는 가장 기초적인 인터랙션 시스템을 구축해야합니다.
# Build the most basic interaction system that reacts when someone approaches the artwork.

# Scenario
# 전시장에 인터랙티브 미디어아트 작품을 설치했습니다. 
# 센서가 관람객과의 거리를 실시간으로 측정하고 있습니다.
# 관람객이 1.2미터보다 가까이 오면 작품이 재생되어야 합니다.

visitor_distance = 1.0
threshold_distance = 1.2

def play_artwork(action):
    if visitor_distance < threshold_distance:
        print("play_artwork('start')")
    else:
        print("play_artwork('stop')")

play_artwork("start")