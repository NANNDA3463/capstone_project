import customtkinter
import drive_page
import settingpage

from tkdial import ScrollKnob
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RPI-Datalogger Project.py")
        self.geometry(f"{800}x{480}")
        self._frame = None
        self.switch_frame(drive_page.Drive_Page)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(side = "top", fill = 'both', expand = "True")
    """
        container = customtkinter.CTkFrame(self, fg_color="transparent")
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (drive_page.Drive_Page, settingpage.Setting_Page):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(drive_page.Drive_Page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    """
if __name__ == "__main__":
    app = App()
    app.mainloop()