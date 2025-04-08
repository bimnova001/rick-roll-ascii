import cv2
import os
import time
import tempfile
import random
import time
# ASCII แสดงจาก pixel
ASCII_CHARS = "@%#*+=-:. "
WIDTH, HEIGHT = 120, 40




def frame_to_ascii(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (WIDTH, HEIGHT))
    ascii_str = ""
    for row in resized:
        for pixel in row:
            ascii_str += ASCII_CHARS[pixel // 25]
        ascii_str += "\n"
    return ascii_str

def play_ascii_video_from_bin(bin_path):
    global warning_shown
    # อ่าน binary data แล้วสร้างไฟล์วิดีโอชั่วคราว
    with open(bin_path, "rb") as f:
        binary_data = f.read()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(binary_data)
        video_path = tmp.name

    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ascii_frame = frame_to_ascii(frame)
        os.system("cls" if os.name == "nt" else "clear")
        print(ascii_frame)
        time.sleep(0.03)
    cap.release()
    
play_ascii_video_from_bin("fun.bin")



