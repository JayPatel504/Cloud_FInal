# Cloud_Final

To create Spark Cluster:<br/>
Create 4 EC2 instances<br/>

In each instance, run the following:<br/>
sudo apt update -y && sudo apt upgrade -y<br/>
sudo apt install -y default-jre default-jdk python3-pip<br/>
wget https://apache.claz.org/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz<br/>
tar -xvzf spark-3.1.1-bin-hadoop3.2.tgz<br/>
mv spark-3.1.1-bin-hadoop3.2 spark<br/>
pip3 install numpy<br/>
<br/>
In the Master Node, run the following:<br/>
ssh-keygen -t rsa -P ""<br/>
<br/>
Copy the contents of .ssh/id_rsa.pub (of master) to .ssh/authorized_keys (of all 4 nodes)<br/>
<br/>
In the Master Node:<br/>
cp spark/conf/spark-env.sh.template spark/conf/spark-env.sh<br/>
cp spark/conf/spark-defaults.conf.template spark/conf/spark-defaults.conf<br/>
cp spark/conf/workers.template spark/conf/workers<br/>
cd spark<br/>
nano conf/spark-env.sh<br/>
  (Add this line anywhere in the file)<tab/><br/>
  JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64<br/>
  (Save and Exit)<br/>
nano conf/spark-defaults.conf<br/>
  (Delete the # in front of spark.master & spark.eventLog.enabled<br/>
   Replace master in <spark://master:7077> with local IP of Master Node<br/>
   Replace true to false next to <spark.eventLog.enabled>)<br/>
   (Save and Exit)<br/>
nano conf/workers<br/>
  (Enter local IP of each Worker Node on a newline)<br/>
  (Save and Exit)<br/>
