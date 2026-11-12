from __future__ import annotations
def run(paths):
 from pathlib import Path
 return [Path(p).stem for p in paths]
