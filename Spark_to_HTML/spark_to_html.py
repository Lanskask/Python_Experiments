import findspark
findspark.init()
import pyspark
sc = pyspark.SparkContext(appName="SQL-EX Data")

from pyspark import SQLContext
sqlContext = SQLContext(sc)

REAL_DATA_FOLDER = "/home/a1/0_Programming/Some_Hadoop_Code_with_SQL/SQL-EX/data/"
HD_REAL_DATA_FOLDER = "file://" + REAL_DATA_FOLDER

laptop_df = sqlContext \
    .read.format("csv") \
    .option("delimiter", "\t") \
    .option("header", "true") \
    .option("inferschema", "true") \
    .option("mode", "DROPMALFORMED") \
    .load(HD_REAL_DATA_FOLDER + "Laptop.csv") 


laptop_df.show()