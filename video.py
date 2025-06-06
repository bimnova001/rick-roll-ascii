import cv2
import os
import time
import tempfile
import random
import time
import tkinter as tk
import threading

ASCII_CHARS = ['@', '#', '8', '&', '%', '$', '*', '+', '=', '-', ':', '.', ' ']
WIDTH, HEIGHT = 120, 40


def show_random_popup(title, message):
    def popup():
        root = tk.Tk()
        root.withdraw()  


        win = tk.Toplevel()
        win.title(title)


        win_width, win_height = 300, 100

        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x = random.randint(0, screen_width - win_width)
        y = random.randint(0, screen_height - win_height)

        win.geometry(f"{win_width}x{win_height}+{x}+{y}")

        label = tk.Label(win, text=message, font=("Arial", 16))
        label.pack(expand=True)

        btn = tk.Button(win, text="OK", command=win.destroy)
        btn.pack(pady=5)

        win.mainloop()

    threading.Thread(target=popup).start()

def show_warning():
    show_random_popup("Warning", "LOL")
    show_random_popup("Error", "LOL")


def frame_to_ascii(frame):
    resized = cv2.resize(frame, (WIDTH, HEIGHT))  # ปรับขนาดภาพ
    ascii_str = ""
    for row in resized:
        for b, g, r in row:  # ใช้ RGB
            # คำนวณความสว่าง (brightness) จาก RGB
            brightness = int((r + g + b) / 3)
            ascii_char = ASCII_CHARS[brightness * len(ASCII_CHARS) // 256]
            ascii_str += f"\033[38;2;{r};{g};{b}m{ascii_char}\033[0m"  # แสดงสี RGB
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
        threading.Thread(target=show_warning).start()
        time.sleep(0.03)
    cap.release()
    
play_ascii_video_from_bin("fun.bin")



