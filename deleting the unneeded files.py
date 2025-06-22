import sys
from pathlib import Path

root = Path(sys.argv[1])
for p in root.rglob('*'):
    try:
        if p.is_file() and p.stat().st_size > 100 * 1024**2:
            print(f"{p.resolve()} — {p.stat().st_size / (1024**2):.2f} MB")
    except (OSError, PermissionError):
        pass
