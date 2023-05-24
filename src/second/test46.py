"""
类型注解，紧紧是提示性，不是强制性的限制
"""
import json
import random
from typing import Union

# 基础数据和容器类型注解，显示的变量定义，一般无需注解
var_1: int = 1

var_2: str = 'hello'

var_3: float = 1.0

var_4: bool = True

var_11: list = [1, 2, 3]

var_12: tuple = (1, 'hello', 1.0)

var_13: dict = {'a': 1, 'b': 2}

var_14: set = {1, 2, 3}

# 基础容器详细注解
var_5: list[int] = [1, 2, 3]

var_6: tuple[int, str, float] = (1, 'hello', 1.0)

var_7: dict[str, int] = {'a': 1, 'b': 2}

var_8: set[int] = {1, 2, 3}


# 类对象类型注解
class Person:
    pass


var_9: Person = Person()

# 使用注释type进行类型注解
var_20 = random.randint(1, 10)  # type: int
var_21 = json.loads('{"a":1}')  # type: dict

# 紧紧是提示性，不是强制性的限制
var_22: int = 'hello'
print(var_22)


# 函数类型注解
def func_1(a: int, b: int) -> float:
    return float(a + b)


f = func_1(1, 2)

# Union类型注解
var_23: list[Union[int, str]] = [1, 'hello']


# Union函数注解
def func_2(data: Union[int, str]) -> Union[int, str]:
    return data
