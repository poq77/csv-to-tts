from dataclasses import dataclass
from pathlib import Path


@dataclass
class DicatationEntry:
    term: str
    sentence: str
    audio_term_path: Path
    audio_sentence_path: Path
