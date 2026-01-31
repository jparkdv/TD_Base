# 인벤토리에 등록된 모든 장비를 순차적으로 점검하는 자동화 루프를 설계합니다.

# Scenario
# 모든 아이템에 순차적으로 접근하여 상태를 점검하는 루프를 구현할 것.
# 각 아이템의 상태를 출력하는 로직을 포함할 것.

harware_list = ["Camera", "Sensor", "Display", "Projector", "Microphone"]

def check_inventory_health(hardware_list):
    for item in hardware_list:
        print(f"Checking status of: {item}")
        # Here you would include actual health check logic
        print(f"{item} is operational.")

check_inventory_health(harware_list)
