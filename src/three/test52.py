"""
计算方法-算子
"""

from pyspark import SparkContext, SparkConf
import os

os.environ['PYSPARK_PYTHON'] = r'C:\Users\liu40\.conda\envs\dataspell\python.exe'

conf = SparkConf().setMaster('local[*]').setAppName('test52')

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9])

# map算子
rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 1)

print(rdd2.collect())

# flatMap算子。解除嵌套

rdd3 = sc.parallelize(['hello world', 'hello spark', 'hello hadoop'])

rdd4 = rdd3.map(lambda x: x.split(' '))

print(rdd4.collect())

rdd5 = rdd3.flatMap(lambda x: x.split(' '))

print(rdd5.collect())


# reduceByKey算子。按照key进行聚合

rdd6 = sc.parallelize([('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)])

rdd7 = rdd6.reduceByKey(lambda x, y: x + y)

print(rdd7.collect())

sc.stop()
