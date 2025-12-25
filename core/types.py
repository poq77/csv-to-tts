from dataclasses import dataclass
from pathlib import Path


@dataclass
class DicatationEntry:
    term: str
    text: str
    audio_text_path: Path
    aduio_term_path: Path
