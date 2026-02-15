# 리스트 슬라이싱(Slicing)을 사용하여 데이터의 일부분만 선택하고, 특정 데이터의 존재 여부(in)를 확인한다.

# Scenario
# 전체 센서 리스트 생성: ["Motion", "Flame", "Smoke", "CO2", "Lidar", "Camera"]
# 처음 3개의 센서만 선택하여 'quick_check' 변수에 저장하고 출력. ([0:3])
# 마지막 2개의 센서만 선택하여 'precision_check' 변수에 저장하고 출력. ([-2:])
# "Smoke" 센서가 리스트에 있는지 if-in 문으로 확인, 있다면 "Fire Safety Sensor Detected." 출력.

all_sensors = ["Motion", "Flame", "Smoke", "CO2", "Lidar", "Camera"]
quick_check = all_sensors[:3]
precision_check = all_sensors[-2:]

if "Smoke" in all_sensors:
    print("Fire Safety Sensor Detected.")

print("Quick Check Sensors:", quick_check)
print("Precision Check Sensors:", precision_check)

