"""
字典
"""

my_dict = {}
print(my_dict, type(my_dict))

my_dict = dict()
print(my_dict, type(my_dict))

my_dict = {"name": "liuhao", "age": 18}
print(my_dict)

print(my_dict["name"])

# 新增元素
my_dict["sex"] = "男"
print(my_dict)

# 修改元素
my_dict["name"] = "liuhao2"
print(my_dict)

# 删除元素
value = my_dict.pop("sex")
print(f"字典中被移除：{value}，现在字典为：{my_dict}")

keys = my_dict.keys()
print(keys, type(keys))

# 遍历字典
for key in my_dict:
    print(f"key:{key}, value:{my_dict[key]}")

# 遍历字典的key
for key in my_dict.keys():
    print(f"key:{key}")

dept_dict = {
    "A": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "B": {
        "部门": "人事部",
        "工资": 5000,
        "级别": 2
    },
    "C": {
        "部门": "财务部",
        "工资": 1000,
        "级别": 1
    },
    "D": {
        "部门": "行政部",
        "工资": 7000,
        "级别": 4
    },
    "E": {
        "部门": "后勤部",
        "工资": 8000,
        "级别": 5
    }
}

for key in dept_dict:
    if dept_dict[key]["级别"] == 1:
        # dept_dict[key]["工资"] += 1000
        # dept_dict[key]["级别"] += 1
        var = dept_dict[key]
        var["工资"] += 1000
        var["级别"] += 1

print(dept_dict)
