import customtkinter
import settingpage

from tkdial import ScrollKnob

#customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
#customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Drive_Page(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)


        # configure grid layout (4x4)
        self.grid_columnconfigure(list(range(0, 40)), weight=1)
        self.grid_rowconfigure(list(range(0, 40)), weight=1)
        self.configure(fg_color="transparent", bg_color="transparent")


        # new bottome Frame
        self.bottombar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.bottombar_frame.grid(row=39, column=0, columnspan=40, sticky="news")
        # columnconfigure는 그리드 내부의 값들에게 영향을 준다.
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

        self.left_label_1_1 = customtkinter.CTkLabel(self.leftbar_frame, text="45℃", width=100,
                                                     font=customtkinter.CTkFont(size=40, weight="bold"))
        self.left_label_1_1.grid(row=10, column=0, padx=10, sticky="nws")
        self.left_label_1_2 = customtkinter.CTkLabel(self.leftbar_frame, text="흡기온도", width=50,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
        self.left_label_1_2.grid(row=10, column=1, padx=10, sticky="ws")
        self.left_label_2_1 = customtkinter.CTkLabel(self.leftbar_frame, text="70℃", width=100,
                                                     font=customtkinter.CTkFont(size=40, weight="bold"))
        self.left_label_2_1.grid(row=10 + pad_value, column=0, padx=10, sticky="nws")
        self.left_label_2_2 = customtkinter.CTkLabel(self.leftbar_frame, text="엔진온도", width=50,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
        self.left_label_2_2.grid(row=10 + pad_value, column=1, padx=10, sticky="ws")
        self.left_label_3_1 = customtkinter.CTkLabel(self.leftbar_frame, text="120℃", width=100,
                                                     font=customtkinter.CTkFont(size=40, weight="bold"))
        self.left_label_3_1.grid(row=10 + pad_value * 2, column=0, padx=10, sticky="nws")
        self.left_label_3_2 = customtkinter.CTkLabel(self.leftbar_frame, text="배기온도", width=50,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
        self.left_label_3_2.grid(row=10 + pad_value * 2, column=1, padx=10, sticky="ws")

        # 우측 값들
        self.rightbar_frame = customtkinter.CTkFrame(self)
        self.rightbar_frame.grid(row=0, column=38, rowspan=39, columnspan=2, sticky="news", pady=20, padx=20)
        self.rightbar_frame.grid_columnconfigure(list(range(0, 2)), weight=1)
        self.rightbar_frame.grid_rowconfigure(list(range(0, 40)), weight=1)

        self.right_label_1_1 = customtkinter.CTkLabel(self.rightbar_frame, text="50%", width=100,
                                                      font=customtkinter.CTkFont(size=40, weight="bold"))
        self.right_label_1_1.grid(row=10, column=0, padx=10, sticky="nes")
        self.right_label_1_2 = customtkinter.CTkLabel(self.rightbar_frame, text="과부하", width=50,
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
        self.right_label_1_2.grid(row=10, column=1, padx=10, sticky="es")
        self.right_label_2_1 = customtkinter.CTkLabel(self.rightbar_frame, text="120kg", width=100,
                                                      font=customtkinter.CTkFont(size=40, weight="bold"))
        self.right_label_2_1.grid(row=10 + pad_value, column=0, padx=10, sticky="nes")
        self.right_label_2_2 = customtkinter.CTkLabel(self.rightbar_frame, text="토크", width=50,
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
        self.right_label_2_2.grid(row=10 + pad_value, column=1, padx=10, sticky="es")
        self.right_label_3_1 = customtkinter.CTkLabel(self.rightbar_frame, text="20.6", width=100,
                                                      font=customtkinter.CTkFont(size=40, weight="bold"))
        self.right_label_3_1.grid(row=10 + pad_value * 2, column=0, padx=10, sticky="nes")
        self.right_label_3_2 = customtkinter.CTkLabel(self.rightbar_frame, text="마력", width=50,
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
        self.right_label_3_2.grid(row=10 + pad_value * 2, column=1, padx=10, sticky="es")

        # 중앙값들
        # self.centerbar_frame = customtkinter.CTkFrame(self)
        # self.centerbar_frame.grid(row = 0, column = 2, rowspan = 39, columnspan = 36, sticky = "news", pady = 20)
        # self.centerbar_frame.grid_columnconfigure(list(range(0,3)), weight=1)
        # self.centerbar_frame.grid_rowconfigure(list(range(0,10)), weight=1)

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

        self.center_label_1_1 = customtkinter.CTkLabel(self.center_label_frame, text="0",
                                                       font=customtkinter.CTkFont(size=50, weight="bold"))
        self.center_label_1_1.grid(row=0, column=0, sticky="news")
        self.center_label_1_2 = customtkinter.CTkLabel(self.center_label_frame, text="RPM",
                                                       font=customtkinter.CTkFont(size=30, weight="bold"))
        self.center_label_1_2.grid(row=0, column=1, sticky="news")

        self.center_label_2_1 = customtkinter.CTkLabel(self.center_label_frame, text="30",
                                                       font=customtkinter.CTkFont(size=50, weight="bold"))
        self.center_label_2_1.grid(row=1, column=0, sticky="news")
        self.center_label_2_2 = customtkinter.CTkLabel(self.center_label_frame, text="km/h",
                                                       font=customtkinter.CTkFont(size=30, weight="bold"))
        self.center_label_2_2.grid(row=1, column=1, sticky="news")

        # 슬라이더 테스트
        self.center_slider.configure(command=self.test_label_change)
        self.bind("<FocusIn>", self.meter_bg_change)

    def test_label_change(self, value):
        self.center_label_1_1.configure(text=round(value))
        self.center_meter.set(value)

    def meter_bg_change(self):
        print(customtkinter.get_appearance_mode())
        if (customtkinter.get_appearance_mode() == "Light"):
            self.center_meter.configure(bg = "#EBEBEB")
        elif(customtkinter.get_appearance_mode() == "Dark"):
            self.center_meter.configure(bg="#242424")
