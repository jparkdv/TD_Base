# 리스트의 데이터를 추가(Append), 삭제(Remove), 수정(Modify)하여 장비 재고를 최신화하는 시스템

# Scenario
# 초기 리스트 생성: inventory = ["Projector", "Speaker", "Sensor", "Laptop"]
# "Sensor"가 고장 나서 제거할 것. (.remove 사용)
# 새로운 "Laser" 장비를 리스트 끝에 추가할 것. (.append 사용)
# 리스트의 첫 번째(인덱스 0) 장비를 "4K_Projector"로 변경할 것.
# 최종 리스트와 총 개수(len)를 출력할 것.

inventory = ["Projector", "Speaker", "Sensor", "Laptop"]
inventory.remove("Sensor")
inventory.append("Laser")
inventory[0] = "4K_Projector"

print("Updated Inventory number:", len(inventory))

      