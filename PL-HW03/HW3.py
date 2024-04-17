import requests
from bs4 import BeautifulSoup
import re
import csv
import json

# 資料在這個 URL 上
url = "https://www.ptt.cc/bbs/AfterPhD/M.1246244269.A.F38.html"

# 發送 HTTP 請求並獲取網頁內容
response = requests.get(url)
html_content = response.content

# 使用 BeautifulSoup 解析 HTML 內容
soup = BeautifulSoup(html_content, "html.parser")

# 找到包含資料的元素
data_elements = soup.find_all("div", class_="school-data")

# 初始化 lists 用於儲存資料
schools = []
departments = []
applicants = []

# 遍歷每個包含資料的元素
for element in data_elements:
    # 使用正則表達式提取資料
    school_pattern =  r"(\w+)\s*大學"
    department_pattern = r"(\w+)\s*系"
    applicant_pattern = r"(\w+)\s*位"
    
    school_match = re.search(school_pattern, element.text)
    department_match = re.search(department_pattern, element.text)
    applicant_match = re.search(applicant_pattern, element.text)
    
    if school_match and department_match and applicant_match:
        schools.append(school_match.group(1))
        departments.append(department_match.group(1))
        applicants.append((applicant_match.group(1)))

# 創建 CSV 檔案
with open("school_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["School", "Department", "Applicants"])
    for i in range(len(schools)):
        writer.writerow([schools[i], departments[i], applicants[i]])

# 創建 JSON 檔案
data = {
    "schools": schools,
    "departments": departments,
    "applicants": applicants
}
with open("school_data.json", "w") as jsonfile:
    json.dump(data, jsonfile)