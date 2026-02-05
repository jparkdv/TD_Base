# 장비 리스트를 알파벳 순으로 정렬하여 가독성 높은 목록을 만듭니다.

unsorted_hardware = ["Projector", "Camera", "Sensor", "Display", "Audio_Interface"]

def print_sorted_inventory(hardware_list):
    sorted_list = sorted(hardware_list)
    
    print("--- 📋 Alphabetical Hardware List ---")
    for index, item in enumerate(sorted_list, start=1):
        print(f"{index}. {item}")

# 정렬 시스템 가동
print_sorted_inventory(unsorted_hardware)