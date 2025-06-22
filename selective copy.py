import os, shutil, sys

src, dst, ext = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(dst, exist_ok=True)
for folder, _, files in os.walk(src):
    for f in files:
        if f.lower().endswith(ext.lower()):
            srcpath = os.path.join(folder, f)
            shutil.copy2(srcpath, dst)
            print(f"Copied {srcpath}")
