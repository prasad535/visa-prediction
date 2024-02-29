import os
import sys
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str
