from faster_whisper import WhisperModel


def transcribe_audio(audio_path, output_path):
    model = WhisperModel("tiny", device="cuda")
    segments, info = model.transcribe(audio_path, word_timestamps=True)
    with open(output_path, "w") as f:
        for segment in segments:
            f.write(
                "[%.2fs -> %.2fs] %s\n" % (segment.start, segment.end, segment.text)
            )
