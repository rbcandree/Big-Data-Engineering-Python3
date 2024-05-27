# a) Create a pyspark dataframe with the following properties:
# - two columns: "id" and "salary";
# - randomize the amount of salary from interval [1000, 6000].
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import random

spark = SparkSession.builder.appName('Some_dataframe').getOrCreate()
 
# columns & expected schema
columns = StructType([StructField('id', IntegerType(), True), StructField('salary', IntegerType(), True)])

# list of tuples with randomized values
data = []
for num in range(1, 21):
    data.append((num, random.randint(1000, 6000)))

# dataframe with expected schema
df = spark.createDataFrame(data, schema = columns)
 
df.show(df.count(), False)

def my_value_modifying_function(value):
    return None if int(value*0.8) < 1000 else int(value*0.8)

# register our user defined function with return type integer
nullify_small_udf = udf(my_value_modifying_function, IntegerType())

df = df.withColumn('I_never_liked_him', nullify_small_udf("salary"))

df.show(df.count(), False)