import argparse

from faster_whisper import WhisperModel


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio using faster-whisper"
    )
    parser.add_argument("audio_path", type=str, help="Path to the audio file")
    args = parser.parse_args()

    model = WhisperModel("tiny", device="cuda")
    segments, info = model.transcribe(args.audio_path, word_timestamps=True)
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))


if __name__ == "__main__":
    main()
