# 0014_error_report.py
# Goal: "Offline" 장비만 추출하여 수리 대상 리스트를 생성합니다.

# 1. 기존 데이터 (0013번 활용)
devices = {
    "Camera": "Online",
    "Sensor": "Offline",
    "Display": "Online",
    "Projector": "Offline"
}

def generate_error_report(device_dict):
    # 빈 리스트를 먼저 만듭니다.
    error_list = []
    
    # 딕셔너리를 탐색합니다.
    for name, status in device_dict.items():
        # 여기에 "Offline"인 경우에만 error_list에 이름을 추가하는 로직을 작성해 보세요.
        if status == "Offline":
            error_list.append(name)
            
    # 2. 결과 출력
    print("--- 🛠️ Repair Required List ---")
    if len(error_list) > 0:
        for item in error_list:
            print(f"- Target: {item}")
        print(f"Total {len(error_list)} devices need attention.")
    else:
        print("All systems are green. No repairs needed!")

# 리포트 생성기 가동
generate_error_report(devices)