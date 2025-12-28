from kokoro import KPipeline
import soundfile as sf
import hashlib
import json
from pathlib import Path

def generate_audio(text: str, path: str, speed: float=1, voice: str='af_heart') -> str:
    pipeline = KPipeline(lang_code='a')
    generator = pipeline(text, voice=voice, speed=speed)
    for i, (gs, ps, audio) in enumerate(generator):
        sf.write(f'{path}', audio, 24000)
        break # current support only one paragraph

def generate_from_json(input_json:str):
    # add databse folder when not exists
    audio_path = Path("./database/audio")
    if not audio_path.exists():
        audio_path.mkdir(parents=True, exist_ok=True)
    
    if not audio_path.is_dir():
        raise Exception("Cannot create database")

    manifest = json.loads(input_json)

    for entry in manifest["data"]:
        for k in entry:
            text = entry[k]["text"]
            filename = hashlib.md5(f"{text}{manifest["speed"]}{manifest["voice"]}".encode('utf-8')).hexdigest()
            path_str = audio_path / f"{filename}.wav"
            print(path_str)
            generate_audio(text, path=path_str, speed=manifest["speed"], voice=manifest["voice"])
            entry[k]["audio"] = str(path_str.absolute())
    
    with open(f"./database/{manifest["name"]}.json", "w") as f:
        json.dump(manifest, f)

if __name__ == "__main__":
    input_json = """
        {
            "name": "example",
            "voice": "af_heart",
            "speed": 1.0,
            "data": [
                {
                    "word": {
                        "text": "winter"
                    },
                    "sentence": {
                        "text": "The winter is coming."
                    }
                },
                {
                    "word": {
                        "text": "fall"
                    },
                    "sentence": {
                        "text": "Leaves fell from the tree."
                    }
                }
            ]
        }"""
    generate_from_json(input_json)