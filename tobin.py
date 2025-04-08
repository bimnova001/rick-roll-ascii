# convert_to_bin.py
with open("fun.mp4", "rb") as f:
    data = f.read()

with open("video.bin", "wb") as f:
    f.write(data)

