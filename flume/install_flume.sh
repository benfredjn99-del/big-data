#!/bin/bash
echo "================================================"
echo " Installation de Apache Flume"
echo "================================================"
echo ""

FLUME_VERSION=1.11.0
FLUME_DIR=/opt/flume

if [ -d "$FLUME_DIR" ]; then
    echo "Flume deja installe dans $FLUME_DIR"
    flume-ng version
    exit 0
fi

echo "Telechargement de Flume $FLUME_VERSION..."
wget -q https://downloads.apache.org/flume/${FLUME_VERSION}/apache-flume-${FLUME_VERSION}-bin.tar.gz -O /tmp/flume.tar.gz

echo "Extraction..."
tar -xzf /tmp/flume.tar.gz -C /opt/
mv /opt/apache-flume-${FLUME_VERSION}-bin $FLUME_DIR
rm /tmp/flume.tar.gz

echo "Configuration du PATH..."
export PATH=$PATH:$FLUME_DIR/bin
echo "export PATH=\$PATH:$FLUME_DIR/bin" >> ~/.bashrc

echo ""
echo "Flume installe !"
flume-ng version