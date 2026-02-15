# for 반복문과 if 조건문을 결합하여 특정 조건에 맞는 데이터만 새로운 리스트에 수집한다.

#  - for 문을 사용하여 all_reports를 순회하세요.
#  - if 문으로 "Error"인 항목만 찾으세요.
#  - 찾은 항목을 error_list에 추가(.append)하세요.
#  -  마지막에 error_list와 그 길이를 출력하세요.

all_reports = ["Normal", "Error", "Normal", "Error", "Warning"]
error_list = []

for report in all_reports:
    if report == "Error":
        error_list.append(report)
        error_list.append(report)
print(error_list, len(error_list))