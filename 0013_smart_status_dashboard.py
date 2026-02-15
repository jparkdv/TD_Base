# for 반복문을 사용하여 리스트의 모든 데이터를 순서대로 하나씩 점검한다.

# Scenario
# 1. 상태 로그 리스트 생성: ["Normal", "Normal", "Error", "Warning", "Normal"]
# 2. for 문을 사용하여 리스트의 각 항목(status)을 순회(Iteration).
# 3. 만약(if) 현재 status가 "Error"라면 -> "ALERT: System Error Detected!" 출력.
# 4. 그렇지 않다면(else) -> "System Status: [현재상태]" 형식으로 출력.

status_log = ["Normal", "Normal", "Error", "Warning", "Normal"]

for status in status_log:
    if status == "Error":
        print("ALERT: System Error Detected!")
    else:
        print(f"System Status: {status}")
