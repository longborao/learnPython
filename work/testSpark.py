#-*- coding: utf-8 -*-
#!env/bin/python

from pyspark import SparkConf, SparkContext

conf = SparkConf()
conf.setAppName("PYSPARK_JOB_NAME")
sc = SparkContext(conf = conf)