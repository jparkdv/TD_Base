# 특정 키워드가 포함된 센서만 골라내어 집중 점검하는 필터링 로직을 설계합니다.

hardware_list = ["Sony_Camera", "Infrared_Sensor", "Projector", "Touch_Sensor"]

def selective_sensor_check(hardware_list, keyword):
    for hardware in hardware_list:
        if keyword in hardware:
            print(f"Checking {hardware}... Passed")