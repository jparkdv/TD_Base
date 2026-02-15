# 여러 개의 센서를 리스트(List) 하나로 묶어서 관리하고, 특정 센서를 선택하거나 전체 개수를 파악하는 시스템

# Scenario
# 센서 이름 4개가 들어있는 리스트(sensor_list)를 생성할 것. (예: "Motion", "Temperature", "Humidity", "Door")
# 현재 연결된 모든 센서 리스트를 출력할 것.
# 인덱싱(Indexing)을 사용하여 첫 번째 센서(0번)와 세 번째 센서(2번)를 각각 출력할 것.
# len() 함수를 사용하여 "Total Sensors: 4" 형태로 총 개수를 출력할 것.

hardware_list = ["motion", "temperature", "humidity", "door"]

print("Connected Sensors:", hardware_list[0])
print("Connected Sensors:", hardware_list[2])

print(hardware_list)

print("Total Sensors:", len(hardware_list))