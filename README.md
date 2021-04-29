# Cloud_Final

To create Spark Cluster:
Create 4 EC2 instances

In each instance, run the following:
sudo apt update -y && sudo apt upgrade -y
sudo apt install -y default-jre default-jdk python3-pip
wget https://apache.claz.org/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz
tar -xvzf spark-3.1.1-bin-hadoop3.2.tgz
mv spark-3.1.1-bin-hadoop3.2 spark
pip3 install numpy

In the Master Node, run the following:
ssh-keygen -t rsa -P ""

Copy the contents of .ssh/id_rsa.pub (of master) to .ssh/authorized_keys (of all 4 nodes)

In the Master Node:
cp spark/conf/spark-env.sh.template spark/conf/spark-env.sh
cp spark/conf/spark-defaults.conf.template spark/conf/spark-defaults.conf
cp spark/conf/workers.template spark/conf/workers
cd spark
nano conf/spark-env.sh
  (Add this line anywhere in the file)
  JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
  (Save and Exit)
nano conf/spark-defaults.conf
  (Delete the # in front of spark.master & spark.eventLog.enabled
   Replace master in <spark://master:7077> with local IP of Master Node
   Replace true to false next to <spark.eventLog.enabled>)
   (Save and Exit)
nano conf/workers
  (Enter local IP of each Worker Node on a newline)
  (Save and Exit)
