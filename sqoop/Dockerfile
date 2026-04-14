FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV SQOOP_VERSION=1.4.7
ENV SQOOP_HOME=/opt/sqoop
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_VERSION=3.2.1
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$PATH:$SQOOP_HOME/bin:$HADOOP_HOME/bin

# Installer Java et wget
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Installer Hadoop
RUN wget -q https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} ${HADOOP_HOME} && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Installer Sqoop
RUN wget -q https://archive.apache.org/dist/sqoop/${SQOOP_VERSION}/sqoop-${SQOOP_VERSION}.bin__hadoop-2.6.0.tar.gz && \
    tar -xzf sqoop-${SQOOP_VERSION}.bin__hadoop-2.6.0.tar.gz && \
    mv sqoop-${SQOOP_VERSION}.bin__hadoop-2.6.0 ${SQOOP_HOME} && \
    rm sqoop-${SQOOP_VERSION}.bin__hadoop-2.6.0.tar.gz

# Installer les librairies manquantes
RUN wget -q https://repo1.maven.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.jar \
    -P ${SQOOP_HOME}/lib/ && \
    wget -q https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.28/mysql-connector-java-8.0.28.jar \
    -P ${SQOOP_HOME}/lib/ && \
    wget -q https://repo1.maven.org/maven2/commons-io/commons-io/2.8.0/commons-io-2.8.0.jar \
    -P ${SQOOP_HOME}/lib/

# Config Sqoop
RUN echo "export JAVA_HOME=${JAVA_HOME}" >> ${SQOOP_HOME}/conf/sqoop-env.sh && \
    echo "export HADOOP_HOME=${HADOOP_HOME}" >> ${SQOOP_HOME}/conf/sqoop-env.sh && \
    echo "export HADOOP_COMMON_HOME=${HADOOP_HOME}" >> ${SQOOP_HOME}/conf/sqoop-env.sh && \
    echo "export HADOOP_MAPRED_HOME=${HADOOP_HOME}" >> ${SQOOP_HOME}/conf/sqoop-env.sh && \
    echo "export HADOOP_COMMON_LIB_NATIVE_DIR=${HADOOP_HOME}/lib/native" >> ${SQOOP_HOME}/conf/sqoop-env.sh

VOLUME ["/data"]
CMD ["tail", "-f", "/dev/null"]