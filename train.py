from pyspark.ml import Pipeline
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

rf = RandomForestClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures", numTrees=500)

labelConverter = IndexToString(inputCol="prediction", outputCol="predictedLabel",labels=labelIndexer.labels)

pipeline = Pipeline(stages=[labelIndexer, featureIndexer, rf, labelConverter])

model = pipeline.fit(data)

model.save(sys.argv[2])

spark.stop()