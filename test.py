from pyspark.ml import PipelineModel
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer, VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import sys
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RandomForestClassifierExample").getOrCreate()

df = spark.read.load(sys.argv[1],format="csv", sep=";", inferSchema="true", header="true")

temp = VectorAssembler(outputCol="features",inputCols=df.columns[:-1])

data=temp.transform(df)

labelIndexer = StringIndexer(inputCol='""""quality"""""', outputCol="indexedLabel").fit(data)

featureIndexer=VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=11).fit(data)

model = PipelineModel.load(sys.argv[2])

predictions = model.transform(data)

evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel",predictionCol="prediction", metricName="f1")
f1 = evaluator.evaluate(predictions)
print("F1 = %g" % (f1))

spark.stop()