from lib2to3.pgen2 import driver
from django.shortcuts import render
import sqlite3
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

df_track = spark.read.format('jbdc') \
    .options(driver='org.sqlite.JDBC', dbtable='home_track', \
        url='jdbc:sqlite:db.sqlite3').load()

df_query = spark.read.format('jbdc') \
    .options(driver='org.sqlite.JDBC', dbtable='home_usertrack', \
        url='jdbc:sqlite:db.sqlite3').load()


# Create your views here.
def get_home(reques):
    return render(reques, 'home.html')