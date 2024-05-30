FROM nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04
WORKDIR /root
RUN apt-get update -y && apt-get install -y python3-pip
COPY infer.py ./
RUN pip3 install faster-whisper
CMD ["python3", "infer.py"]
