"""
异常
"""
try:
    f = open("../../resource/测试3.txt", "r", encoding="utf-8")
except:
    f = open("../../resource/测试3.txt", "w", encoding="utf-8")

try:
    1 / 0
except ZeroDivisionError as e:
    print(e)

# 捕获多个异常
try:
    1 / 0
except (ZeroDivisionError, NameError) as e:
    print(e)

# 捕获所有异常
try:
    1 / 0
except Exception as e:
    print("出现异常了")

# 异常else
try:
    1 / 1
except Exception as e:
    print("出现异常了")
else:
    print("没有异常")

# 异常finally
try:
    f = open("../../resource/测试4.txt", "r", encoding="utf-8")
except Exception as e:
    print("出现异常了")
    f = open("../../resource/测试4.txt", "w", encoding="utf-8")
else:
    print("没有异常")
finally:
    print("finally")
    f.close()
