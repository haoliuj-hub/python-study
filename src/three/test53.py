"""
案例：读取文件，计算单词出现的数量
"""

from pyspark import SparkContext, SparkConf

import os

os.environ['PYSPARK_PYTHON'] = r'C:\Users\liu40\.conda\envs\dataspell\python.exe'

conf = SparkConf().setMaster('local[*]').setAppName('test53')

sc = SparkContext(conf=conf)

rdd = sc.textFile('../../resource/example/hello.txt') \
    .flatMap(lambda x: x.split(' ')) \
    .map(lambda x: (x, 1)) \
    .reduceByKey(lambda x, y: x + y)

print(rdd.collect())

sc.stop()
