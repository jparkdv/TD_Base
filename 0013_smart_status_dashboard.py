# 각 장비의 이름과 현재 상태를 지정하고 관리하는 시스템을 구축합니다.

# Scenario

devices = {
    "Camera" : "Online",
    "Sensor" : "Offline",
    "Display" : "Online"
    }

def update_device(device_name, status):
    devices[device_name] = status
    print(f"update_device('{device_name}'is now '{status}')")

def show_status():
    for device, status in devices.items():
        print(f"show_status('{device}': '{status}')")

show_status()  