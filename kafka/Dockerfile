FROM python:3.9-slim

RUN pip install kafka-python

WORKDIR /app
# COPY temp/ /app/
COPY . /app/
CMD ["tail", "-f", "/dev/null"]