## Faster-Whisper Test

### Structure:

```
28.0 KiB faster-whisper-test
16.0 KiB ├─ audio-files
16.0 KiB │  └─ sample.ogg
 4.0 KiB ├─ README.md
 4.0 KiB ├─ infer.py
 4.0 KiB └─ Dockerfile

1 directory, 4 files
```

### Requirements

- Docker
- NVIDIA Docker runtime (`sudo apt install nvidia-container-runtime`)

### Setup

```bash
$ docker build -t faster-whisper-app .
$ docker run --gpus all --rm -p 5000:5000 -v $(pwd)/audio-files:/tmp/vm faster-whisper-test
```
