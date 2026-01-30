# 다수의 하드웨어 자산을 리스트 형태로 통합관리하는 인벤토리 시스템을 구축합니다.

# Scenario
# 현재 전시장에 설치된 장비 목록(hardware_list)을 리스트로 생성할 것.
# 새로운 장비가 추가되었을 때 리스트 끝에 데이터를 삽입하는 로직을 구현할 것.
# 특정 장비가 철거되었을 때 리스트에서 해당 데이터를 제거하는 로직을 구현할 것.

# Create a list of hardware currently installed in the gallery.
# Implement logic to insert data at the end of the list when new equipment is added.
# Implement logic to remove specific data from the list when equipment is decommissioned.)

hardware_list = ["Camera", "Sensor", "Display, Projector"]

def  update_inventory(action, item):
    if action == "add":
        hardware_list.append(item)
        print(f"Added: {item}")
    elif action == "remove":
        if item in hardware_list:
            hardware_list.remove(item)
            print(f"Removed: {item}")
        else:
            print(f"Item not found: {item}")

update_inventory("add", "Microphone")
update_inventory("remove", "Sensor")