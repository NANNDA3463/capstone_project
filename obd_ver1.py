import obd
import customtkinter as ctk
import tkinter as tk

# OBD-II 어댑터의 포트와 속도에 맞게 설정합니다.
obd.logger.setLevel(obd.logging.DEBUG)
ports = obd.scan_serial()  # 유효한 USB 또는 RF 포트 목록을 반환
print(ports)
connection = obd.OBD(portstr=ports[0], baudrate=38400, fast=False, timeout=10)  # USB 또는 RF 포트에 자동 연결

# Tkinter window를 생성합니다.
root = tk.Tk()
root.title("OBD-II Data")

# OBD-II 데이터를 표시할 라벨들을 생성합니다.
labels = {}
label_texts = {
    "RPM": "RPM: ",
    "SPEED": "SPEED: ",
    # 추가로 표시하고 싶은 다른 OBD-II 데이터도 여기에 추가할 수 있습니다.
}

for key, text in label_texts.items():
    label = ctk.CTkLabel(root, text=text)
    label.pack()
    labels[key] = label

def update_labels():
    # OBD-II 데이터를 읽고 라벨에 표시합니다.
    for key, label in labels.items():
        response = connection.query(obd.commands[key])
        label.configure(text=label_texts[key] + str(response.value))

    # 1초마다 라벨을 업데이트합니다.
    root.after(100, update_labels)

# 라벨을 업데이트합니다.
update_labels()

# Tkinter loop를 시작합니다.
root.mainloop()
