"""
Spark - PySpark
"""
import time

from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster('local[*]').setAppName('test51')

sc = SparkContext(conf=conf)

print(sc.version)

rdd1 = sc.parallelize([12, 13, 14, 15, 16])

rdd2 = sc.parallelize((12, 13, 14, 15, 16))

rdd3 = sc.parallelize({12, 13, 14, 15, 16})

rdd4 = sc.parallelize({'a': 12, 'b': 13, 'c': 14, 'd': 15, 'e': 16})

rdd5 = sc.parallelize('Hello World')

print(rdd1.collect())

print(rdd2.collect())

print(rdd3.collect())

print(rdd4.collect())

print(rdd5.collect())

sc.stop()
