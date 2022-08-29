From python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /mongo_engine_test
WORKDIR /mongo_engine_test
COPY . /mongo_engine_test/
RUN pip install -r requirements.txt
