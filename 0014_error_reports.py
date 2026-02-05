# 딕셔너리를 탐색하여 "Offline" 상태인 장비만 자동으로 추출해 리포트 리스트를 작성합니다.

devices = {
    "Camera": "Online",
    "Sensor": "Offline",
    "Display": "Online",
    "Projector": "Offline"
}

def generate_error_report(device_dict):
    error_list = []
    
    for name, status in device_dict.items():
        if status == "Offline":
            error_list.append(name)
            
    print("--- 🛠️ Repair Required List ---")
    if len(error_list) > 0:
        for item in error_list:
            print(f"- Target: {item}")
        print(f"Total {len(error_list)} devices need attention.")
    else:
        print("All systems are green. No repairs needed!")

generate_error_report(devices)