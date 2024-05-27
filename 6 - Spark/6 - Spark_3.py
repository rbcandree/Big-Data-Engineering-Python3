#pip install pyspark
#sudo apt install default-jre
#pip install numpy

from pyspark.sql import SparkSession

#Step 1: Creating a SparkSession
spark = SparkSession.builder.appName("Datacamp Pyspark Tutorial").config("spark.memory.offHeap.enabled","true").config("spark.memory.offHeap.size","10g").getOrCreate()

#Step 2: Creating the DataFrame
#df = spark.read.csv('OnlineRetail.csv',header=True,escape="\"")
df = spark.read.option('delimiter', ';').csv('OnlineRetail.csv',header=True,escape="\"")
df.show(5,0)

#Step 3: Exploratory Data Analysis
print(df.count())
print(df.select('CustomerID').distinct().count())
from pyspark.sql.functions import *
from pyspark.sql.types import *
#df.groupBy('Country').agg(countDistinct('CustomerID').alias('country_count')).show()
df.groupBy('Country').agg(countDistinct('CustomerID').alias('country_count')).orderBy(desc('country_count')).show()

spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")
df = df.withColumn('date',to_timestamp("InvoiceDate", 'dd.MM.yyyy HH:mm'))
df.select(max("date")).show()
df.select(min("date")).show()

#Step 4: Data Pre-processing
#Recency
df = df.withColumn("from_date", lit("10.12.01 08:26"))
df = df.withColumn('from_date',to_timestamp("from_date", 'yy.MM.dd HH:mm'))

df2=df.withColumn('from_date',to_timestamp(col('from_date'))).withColumn('recency',col("date").cast("long") - col('from_date').cast("long"))
df2 = df2.join(df2.groupBy('CustomerID').agg(max('recency').alias('recency')),on='recency',how='leftsemi')
df2.show(5,0)
df2.printSchema()

#Frequency
df_freq = df2.groupBy('CustomerID').agg(count('InvoiceDate').alias('frequency'))
df_freq.show(5,0)
df3 = df2.join(df_freq,on='CustomerID',how='inner')
df3.show(5,0)
df3.printSchema()

#Monetary Value
m_val = df3.withColumn('TotalAmount',col("Quantity") * col("UnitPrice"))
m_val = m_val.groupBy('CustomerID').agg(sum('TotalAmount').alias('monetary_value'))
finaldf = m_val.join(df3,on='CustomerID',how='inner')
finaldf = finaldf.select(['recency','frequency','monetary_value','CustomerID']).distinct()
finaldf.show(5,0)
finaldf.printSchema()

#Standardization
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler

assemble=VectorAssembler(inputCols=[
    'recency','frequency','monetary_value'
], outputCol='features')
#assembled_data=assemble.transform(finaldf) - caused an error
assembled_data=assemble.setHandleInvalid('skip').transform(finaldf)

scale=StandardScaler(inputCol='features',outputCol='standardized')
data_scale=scale.fit(assembled_data)
data_scale_output=data_scale.transform(assembled_data)

data_scale_output.select('standardized').show(2,truncate=False)