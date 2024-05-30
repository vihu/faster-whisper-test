FROM nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04

WORKDIR /root

RUN apt-get update -y && apt-get install -y python3-pip

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY infer.py ./
COPY server.py ./

CMD ["python3", "server.py"]
