FROM bde2020/flume:latest

USER root

# Hadoop env fix
ENV HADOOP_HOME=/usr/local/hadoop
ENV HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop

# IMPORTANT: force Hadoop libs in classpath
ENV HADOOP_CLASSPATH=/usr/local/hadoop/share/hadoop/common/*:/usr/local/hadoop/share/hadoop/hdfs/*:/usr/local/hadoop/share/hadoop/common/lib/*:/usr/local/hadoop/share/hadoop/hdfs/lib/*