import json
import matplotlib.pyplot as plt

# 讀取JSON檔案
with open('education_salary.json', 'r') as file:
    data = json.load(file)

# 建立一個包含三個子圖的圖表
fig, axes = plt.subplots(3, 1, figsize=(10, 18))

# 調整子圖之間的間距
plt.subplots_adjust(hspace=0.5)

# 1. 各學歷之最高薪分別為何
education_order = ['elementary', 'junior high', 'high', 'university', 'master', 'doctor']
education_salaries = {education: 0 for education in education_order}

for item in data:
    education = item['education']
    salary = item['salary']
    if salary > education_salaries[education]:
        education_salaries[education] = salary

x = education_order
y = [education_salaries[education] for education in education_order]

axes[0].bar(x, y)
axes[0].set_xlabel('Education')
axes[0].set_ylabel('Salary')
axes[0].set_title('Highest Salary by Education')

# 2. 博士最高薪與最低薪資分別為何 差距為何
doctor_salaries = [item['salary'] for item in data if item['education'] == 'doctor']

# 在第二個子圖中生成博士薪資的箱形圖
axes[1].boxplot(doctor_salaries)
axes[1].set_xlabel('Education')
axes[1].set_ylabel('Salary')
axes[1].set_title('Doctor Salaries')

# 3. 薪資介於27400-37400的學歷分布比例
count = 0
for item in data:
    salary = item['salary']
    if 27400 <= salary <= 37400:
        count += 1

labels = ['Within Range', 'Outside Range']
sizes = [count, len(data) - count]

# 在第三個子圖中生成薪資範圍內外學歷的圓餅圖
axes[2].pie(sizes, labels=labels, autopct='%1.1f%%')
axes[2].set_title('Education Distribution within Salary Range')

# 顯示圖表
plt.show()