# a) Create a pyspark dataframe from the following information:
# id, name, salary
# 100, Esteri, 5700
# 110, Uolevi, 2200
# 202, Kalervo, 3333
# 250, Albert, 2310
# 300, Mia, 1750
from pyspark.sql import SparkSession
data = [{'id': 100, 'name': 'Esteri', 'salary': 5700},
        {'id': 110, 'name': 'Uolevi', 'salary': 2200},
        {'id': 202, 'name': 'Kalervo', 'salary': 3333},
        {'id': 250, 'name': 'Albert', 'salary': 2310},
        {'id': 300, 'name': 'Mia', 'salary': 1750}]

spark = SparkSession.builder.getOrCreate()
df = spark.createDataFrame(data)
df.show(df.count(), False)

# b) Add a fourth column called Temporary. Randomize this value for every person. Possible values are True and False.
from pyspark.sql.functions import *
df = df.withColumn('Temporary', when(rand() > 0.5, 'True').otherwise('False'))
df.show(df.count(), False)

# c) Show only those dataframe rows where the value of Temporary field is False and the amount of salary is greater than 2300.
df1 = df.where(df['Temporary'] == 'False').where(df['salary'] > 2300)
df1.show(df1.count(), False)