import os

from flask import Flask, jsonify, request

from infer import transcribe_audio

app = Flask(__name__)


@app.route("/transcribe", methods=["POST"])
def transcribe():
    data = request.get_json()
    audio_path = data["audio_path"]
    if not os.path.isfile(audio_path):
        return jsonify({"error": f"File not found: {audio_path}"}), 404

    output_dir = os.path.join(os.path.dirname(audio_path), "text")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, os.path.basename(audio_path) + ".txt")

    transcribe_audio(audio_path, output_path)

    return jsonify({"output_path": output_path}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
