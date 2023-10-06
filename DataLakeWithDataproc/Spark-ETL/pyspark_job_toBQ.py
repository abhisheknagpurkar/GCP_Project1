from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('pyspark_to_BQ').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel('WARN')


log_file_rdd = sc.textFile('gs://deongcp-data-bucket/from-git/chapter-5/dataset/logs_example.txt')

log_file_split = log_file_rdd.map(lambda x : x.split(' '))
log_file_col = log_file_split.map(lambda x : (x[0], x[3], x[5], x[6]))

columns = ['ip', 'date', 'method', 'url']
log_file_df = log_file_col.toDF(columns)
log_file_df.createOrReplaceTempView('logTable')

sql = f"""
select url, count(*) as count
from logTable
where url like '%/article%'
group by url
"""
log_file_count = spark.sql(sql)
print("### Get only articles and blog records ###")
log_file_count.show()

BUCKET_NAME = 'deongcp-data-bucket'
#log_file_count.write.format('bigquery').option('temporaryGcsBucket', BUCKET_NAME).option('table', 'DataProc.article_count').mode('overwrite').save()

log_file_count.write.format('bigquery').option("writeMethod","direct").option('table', 'DataProc.article_count').mode('overwrite').save()
