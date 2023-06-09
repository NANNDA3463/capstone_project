import customtkinter
import settingpage
import obd
from tkdial import ScrollKnob
import pandas as pd
import tkinter as tk
import main
import PIL

is_recording = False
class Drive_Page(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #obd 초기화
        obd.logger.setLevel(obd.logging.DEBUG)
        self.ports = obd.scan_serial()

        #lables 초기화
        self.labels = {}
        # RPM, 속도, 흡기온, 촉매온도, 유온, 공기온, 유압, 엔진가동시간
        self.label_texts = {
            "RPM": "RPM",  # RPM, 가져와짐
            "SPEED": "SPEED",  # 속도, 가져와짐
            "FUEL_LEVEL": "FUEL_LEVEL",  # 연료량, 가져와짐
            "CATALYST_TEMP_B1S1": "CATALYST_TEMP_B1S1",  # 촉매온도, 가져와짐
            # "OIL_TEMP": "OIL_TEMP",  # 유온, 안가져와짐
            "INTAKE_TEMP": "INTAKE_TEMP",  # 흡기온, 가져와짐
            "INTAKE_PRESSURE": "INTAKE_PRESSURE",  # 매니폴드압,가져와짐
            "RUN_TIME": "RUN_TIME",  # 가동시간, 가져와짐
            "COOLANT_TEMP": "COOLANT_TEMP",  # 냉각수온도, 가져와짐
            "THROTTLE_POS": "THROTTLE_POS",  # 스로틀위치, 가져와짐
            "ENGINE_LOAD": "ENGINE_LOAD",  # 엔진부하, 가져와짐
            "FUEL_RATE": "FUEL_RATE",  # 연료유량, 안가져와짐
        }

        for key, text in self.label_texts.items():
            label = customtkinter.CTkLabel(self)
            self.labels[key] = label

        #pandas 초기화
        self.df = pd.DataFrame()
        self.is_recording = False

        # configure grid layout (40x40)
        self.grid_columnconfigure(list(range(0, 40)), weight=1)
        self.grid_rowconfigure(list(range(0, 40)), weight=1)
        self.configure(fg_color="transparent", bg_color="transparent")

        # new bottom Frame
        self.bottombar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.bottombar_frame.grid(row=39, column=0, columnspan=40, sticky="news")
        # column_configure는 그리드 내부의 값들에게 영향을 준다.
        self.bottombar_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.bottombar_frame.grid_rowconfigure(0, weight=1)

        self.bottombar_button_1 = customtkinter.CTkButton(self.bottombar_frame, text="주행", corner_radius=0,
                                                          font=customtkinter.CTkFont(size=20, weight="bold"))
        self.bottombar_button_1.grid(row=0, column=0, padx=1, sticky="news")

        self.bottombar_button_2 = customtkinter.CTkButton(self.bottombar_frame, text="랩타임측정", corner_radius=0,
                                                          font=customtkinter.CTkFont(size=20, weight="bold"))
        self.bottombar_button_2.grid(row=0, column=1, padx=1, sticky="news")
        self.bottombar_button_3 = customtkinter.CTkButton(self.bottombar_frame, text="엔진출력", corner_radius=0,
                                                          font=customtkinter.CTkFont(size=20, weight="bold"))
        self.bottombar_button_3.grid(row=0, column=2, padx=1, sticky="news")
        self.bottombar_button_4 = customtkinter.CTkButton(self.bottombar_frame, text="설정", corner_radius=0,
                                                          font=customtkinter.CTkFont(size=20, weight="bold"),
                                                          command=lambda: parent.switch_frame(settingpage.Setting_Page))
        self.bottombar_button_4.grid(row=0, column=3, padx=1, sticky="news")

        # 간격
        pad_value = 7
        # 좌측 값들

        self.leftbar_frame = customtkinter.CTkFrame(self)
        self.leftbar_frame.grid(row=0, column=0, rowspan=39, columnspan=2, sticky="news", pady=20, padx=20)
        self.leftbar_frame.grid_columnconfigure(list(range(0, 2)), weight=1)
        self.leftbar_frame.grid_rowconfigure(list(range(0, 40)), weight=1)

        #self.left_label_1_1 = customtkinter.CTkLabel(self.leftbar_frame, text="45℃", width=100,
        #                                             font=customtkinter.CTkFont(size=40, weight="bold"))
        self.labels["FUEL_RATE"] = customtkinter.CTkLabel(self.leftbar_frame, width=100,
                                                     font=customtkinter.CTkFont(size=40, weight="bold"))
        self.labels["FUEL_RATE"].grid(row=10, column=0, padx=10, sticky="nws")
        self.left_label_1_2 = customtkinter.CTkLabel(self.leftbar_frame, text="연료소모(L/h)", width=50,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
        self.left_label_1_2.grid(row=10, column=1, padx=10, sticky="ws")

        self.labels["CATALYST_TEMP_B1S1"] = customtkinter.CTkLabel(self.leftbar_frame, width=100,
                                                     font=customtkinter.CTkFont(size=40, weight="bold"))
        #self.left_label_2_1 = customtkinter.CTkLabel(self.leftbar_frame, text="70", width=100,
        #                                             font=customtkinter.CTkFont(size=40, weight="bold"))
        self.labels["CATALYST_TEMP_B1S1"].grid(row=10 + pad_value, column=0, padx=10, sticky="nws")
        self.left_label_2_2 = customtkinter.CTkLabel(self.leftbar_frame, text="촉매온도(℃)", width=50,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
        self.left_label_2_2.grid(row=10 + pad_value, column=1, padx=10, sticky="ws")

        self.left_label_3_2 = customtkinter.CTkLabel(self.leftbar_frame, text="120", width=100,
                                                     font=customtkinter.CTkFont(size=40, weight="bold"))
        self.left_label_3_2.grid(row=10 + pad_value * 2, column=0, padx=10, sticky="nws")

        self.labels["COOLANT_TEMP"] = customtkinter.CTkLabel(self.leftbar_frame, text="0", width=50,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))

        self.labels["COOLANT_TEMP"].grid(row=10 + pad_value * 2, column=1, padx=10, sticky="ws")

        # 우측 값들
        self.rightbar_frame = customtkinter.CTkFrame(self)
        self.rightbar_frame.grid(row=0, column=38, rowspan=39, columnspan=2, sticky="news", pady=20, padx=20)
        self.rightbar_frame.grid_columnconfigure(list(range(0, 2)), weight=1)
        self.rightbar_frame.grid_rowconfigure(list(range(0, 40)), weight=1)

        self.labels["FUEL_LEVEL"] = customtkinter.CTkLabel(self.rightbar_frame, width=100,
                                            font=customtkinter.CTkFont(size=40, weight="bold"))

        self.labels["FUEL_LEVEL"].grid(row=10, column=0, padx=10, sticky="nes")
        self.right_label_1_2 = customtkinter.CTkLabel(self.rightbar_frame, text="공기온(℃)", width=50,
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
        self.right_label_1_2.grid(row=10, column=1, padx=10, sticky="es")


        #self.right_label_2_1 = customtkinter.CTkLabel(self.rightbar_frame, text="120", width=100,
        #                                              font=customtkinter.CTkFont(size=40, weight="bold"))
        self.labels["FUEL_PRESSURE"] = customtkinter.CTkLabel(self.rightbar_frame, width=100,
                                              font=customtkinter.CTkFont(size=40, weight="bold"))
        self.labels["FUEL_PRESSURE"].grid(row=10 + pad_value, column=0, padx=10, sticky="nes")
        self.right_label_2_2 = customtkinter.CTkLabel(self.rightbar_frame, text="유압(kPa)", width=50,
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
        self.right_label_2_2.grid(row=10 + pad_value, column=1, padx=10, sticky="es")

        self.labels["RUN_TIME"] = customtkinter.CTkLabel(self.rightbar_frame, width=100,
                                         font=customtkinter.CTkFont(size=40, weight="bold"))
        #self.right_label_3_1 = customtkinter.CTkLabel(self.rightbar_frame, text="20.6", width=100,
        #                                              font=customtkinter.CTkFont(size=40, weight="bold"))
        self.labels["RUN_TIME"].grid(row=10 + pad_value * 2, column=0, padx=10, sticky="nes")
        self.right_label_3_2 = customtkinter.CTkLabel(self.rightbar_frame, text="시간(sec)", width=50,
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
        self.right_label_3_2.grid(row=10 + pad_value * 2, column=1, padx=10, sticky="es")

        # 중앙값들
        # self.centerbar_frame = customtkinter.CTkFrame(self)
        # self.centerbar_frame.grid(row = 0, column = 2, rowspan = 39, columnspan = 36, sticky = "news", pady = 20)
        # self.centerbar_frame.grid_columnconfigure(list(range(0,3)), weight=1)
        # self.centerbar_frame.grid_rowconfigure(list(range(0,10)), weight=1)

        #중앙 다이얼
        self.center_meter = ScrollKnob(self, text="", start=-1, end=5000, steps=1, radius=250, bar_color="#1F6AA5",
                                       progress_color="white", outer_length=0,
                                       border_width=30, start_angle=250, inner_width=0, outer_width=5,
                                       text_font=customtkinter.CTkFont(size=20, weight="bold")
                                       )
        self.meter_bg_change()
        self.center_meter.grid(row=10, column=19)
        self.center_slider = customtkinter.CTkSlider(self, from_=0, to=5000, number_of_steps=5000)
        self.center_slider.grid(row=11, column=19)

        self.center_label_frame = customtkinter.CTkLabel(self)
        self.center_label_frame.grid(row=12, column=2, rowspan=24, columnspan=36, sticky="news")
        self.center_label_frame.grid_rowconfigure(list(range(4)), weight=1)
        self.center_label_frame.grid_columnconfigure(list(range(2)), weight=1)

        self.labels["RPM"] = customtkinter.CTkLabel(self.center_label_frame,
                                    font=customtkinter.CTkFont(size=50, weight="bold"))
        #self.center_label_1_1 = customtkinter.CTkLabel(self.center_label_frame, text="0",
        #                                               font=customtkinter.CTkFont(size=50, weight="bold"))
        self.labels["RPM"].grid(row=0, column=0, sticky="news")
        self.center_label_1_2 = customtkinter.CTkLabel(self.center_label_frame, text="RPM",
                                                       font=customtkinter.CTkFont(size=30, weight="bold"))
        self.center_label_1_2.grid(row=0, column=1, sticky="news")

        self.labels["SPEED"] = customtkinter.CTkLabel(self.center_label_frame,
                                      font=customtkinter.CTkFont(size=50, weight="bold"))
        #self.center_label_2_1 = customtkinter.CTkLabel(self.center_label_frame, text="30",
        #                                               font=customtkinter.CTkFont(size=50, weight="bold"))
        self.labels["SPEED"].grid(row=1, column=0, sticky="news")
        self.center_label_2_2 = customtkinter.CTkLabel(self.center_label_frame, text="km/h",
                                                       font=customtkinter.CTkFont(size=30, weight="bold"))
        self.center_label_2_2.grid(row=1, column=1, sticky="news")

        # 슬라이더 테스트
        self.center_slider.configure(command=self.test_label_change)
        self.bind("<FocusIn>", self.meter_bg_change)

        #after 테스트
        #self.after_test1()
        #self.start_recording()

    def test_label_change(self, value):
        self.labels["RPM"].configure(text=round(value))
        self.center_meter.set(value)

    #Custom Tkiner 호환용 함수(배경색 맞추기)
    def meter_bg_change(self):
        print(customtkinter.get_appearance_mode())
        if (customtkinter.get_appearance_mode() == "Light"):
            self.center_meter.configure(bg = "#EBEBEB")
        elif(customtkinter.get_appearance_mode() == "Dark"):
            self.center_meter.configure(bg="#242424")

    def obd_update(self):
        # OBD-II 데이터를 읽고 라벨에 표시합니다.
        data = {}
        for key, label in self.labels.items():
            response = self.connection.query(obd.commands[key])
            value = str(response.value)
            label.configure(text=self.label_texts[key] + value)
            print(value[0])
            data[key] = value
            if (key == "RPM") :
                self.center_meter.set(int(value[:3]))
        #df_row = pd.DataFrame(data, index=[0])
        #self.df.append(df_row, ignore_index=True)
        # 1초마다 라벨을 업데이트합니다.
        self.after(100, self.obd_update)

    #재귀함수 식
    def after_test1(self):
        print("hi")
        self.after(1000, self.after_test1)

    def save_data(self):
        # DataFrame을 엑셀 파일로 저장
        self.df.to_excel("obd_data.xlsx", index=False)

    def stop_recording(self):
        global is_recording
        is_recording = False

    def start_recording(self):
        global is_recording
        if not is_recording:
            is_recording = True
            self.obd_update()

