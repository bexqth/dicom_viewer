from tkinter import Tk, Frame, Button, filedialog, PhotoImage, Label
from dicom_loader import dicom_loader
from image_panel import image_panel
from info_panel import info_panel

class viewer_app:

    def __init__(self):
        self.window = Tk()
        self.window.title("DICOM Viewer")
        self.window.minsize(1055, 625)
        self.window.geometry("1066x625")

        icon = PhotoImage(file = 'dicom_icon2.png')
        self.window.iconphoto(True, icon)

        self.primary_color = "#57534D"
        self.window.configure(bg=self.primary_color)
        
        self.window.grid_columnconfigure(0, weight=4)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=0)
        self.window.grid_rowconfigure(1, weight=1)

        self.dicom_files = []
        self.current_index = -1
        self.loaders = []

        self.set_layout()
        self.set_buttons()

    def open_file(self):
        filepaths = filedialog.askopenfilenames(
            title="Vyber DICOM súbory",
            filetypes=[("DICOM Files", "*.dcm"), ("All Files", "*.*")]
        )

        if filepaths:
            self.dicom_files = []
            self.loaders = []

            for path in filepaths:
                self.dicom_files.append(path)
                loader = dicom_loader()
                loader.load_dicom_image(path)
                loader.set_patient_info()
                self.loaders.append(loader) 

            self.dicom_files.sort()
            self.current_index = 0
            self.display_current_image()

    def set_layout(self):
        self.button_frame = Frame(self.window, bg=self.primary_color, height=45)
        self.button_frame.grid(row=0, column=0, columnspan=2, sticky="new")
        
        self.data_frame = Frame(self.window, bg="#A6A09B", width=800, height=570, relief = "solid", bd = 3)
        self.data_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)
        self.data_frame.grid_propagate(False)
        
        self.info_panel = info_panel(self.window, width=250, height=570, bg=self.primary_color)
        self.info_panel.grid(row=1, column=1, sticky="nsew", padx=15, pady=15)
        self.info_panel.grid_propagate(False)
        
        self.image_panel = image_panel(self.data_frame)
        self.image_panel.configure(bg="#A6A09B")
        self.image_panel.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.window.update_idletasks()

    def display_current_image(self):
        if len(self.dicom_files) == 0 or self.current_index < 0:
            return
        loader = self.loaders[self.current_index]
        
        self.window.update_idletasks()
        width = self.data_frame.winfo_width()
        height = self.data_frame.winfo_height()
        self.image_panel.display_dicom_image(loader.image, width, height)

        info = [
            "Name: " + str(loader.get_patient_name()),
            "ID: " + str(loader.get_patient_id()),
            "Modality: " + str(loader.get_modality()),
            "Date: " + str(loader.get_study_date()),
            "Size: " + str(loader.get_image_size())
        ]
        self.info_panel.update_info(info)
        self.update_index_label()

    def update_index_label(self):
        if len(self.dicom_files) > 0:
            self.index_label.config(text=f"Fotka {self.current_index + 1} / {len(self.dicom_files)}")
        else:
            self.index_label.config(text="No pictures")

    def next_image(self):
        if self.current_index < len(self.dicom_files) - 1:
            self.current_index += 1
            self.display_current_image()

    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_current_image()

    def set_buttons(self):
        open_button = Button(self.button_frame, 
                           text="Open DICOM", 
                           highlightbackground=self.primary_color,
                           command=self.open_file,
                           font=("Segoe UI", 10, "bold"))
        open_button.pack(side="left", padx=15, pady=8)

        self.prev_button = Button(self.button_frame,
                               text="←",
                               highlightbackground=self.primary_color,
                               command=self.prev_image,
                               font=("Segoe UI", 10, "bold"))
        self.prev_button.pack(side="left", padx=5, pady=8)
        
        self.next_button = Button(self.button_frame,
                               text="→",
                               highlightbackground=self.primary_color,
                               command=self.next_image,
                               font=("Segoe UI", 10, "bold"))
        self.next_button.pack(side="left", padx=5, pady=8)

        self.index_label = Label(self.button_frame, 
                                  text="Žiadne fotky", 
                                  bg=self.primary_color, 
                                  fg="white",
                                  font=("Segoe UI", 10))
        self.index_label.pack(side="left", padx=20, pady=8)


    def run(self):
        self.window.mainloop()