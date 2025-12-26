from .types import DicatationEntry
from pathlib import Path
import json


def load_manifest(path: Path) -> list[DicatationEntry]:
    with open(path, 'r') as file:
        manifest = json.load(file)

    for item in data:
        item["audio_term_path"] = Path(item["audio_term_path"])
        item["audio_sentence_path"] = Path(item["audio_sentence_path"])

    entries = [DicatationEntry(**item) for item in data]

    return entries
