from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('pyspark_hdfs_to_hdfs').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel('WARN')

MASTER_NODE_INSTANCE = 'deongcp-dataproc-cluster-m'
log_file_rdd = sc.textFile(f'hdfs://{MASTER_NODE_INSTANCE}/data/logs_example.txt')

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

log_file_count.write.save('hdfs://{}/data/article_count'.format(MASTER_NODE_INSTANCE), format='csv', mode='overwrite')