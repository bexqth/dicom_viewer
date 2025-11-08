from tkinter import Tk, Frame, Button, filedialog, PhotoImage
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

        self.set_layout()
        self.set_buttons()

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            loader = dicom_loader()
            loader.load_dicom_image(filepath)
            loader.set_patient_info() 

            self.window.update_idletasks()

            width = self.data_frame.winfo_width()
            height = self.data_frame.winfo_height()
            self.image_panel.display_dicom_image(loader.image, width, height)
            
            info = [
                "Name: " + str(loader.get_patient_name()),
                "ID: " + str(loader.get_patient_id()),
                "Modality: " +  str(loader.get_modality()),
                "Date: " + str(loader.get_study_date()),
                "Size: " + str(loader.get_image_size())
            ]
            self.info_panel.update_info(info)

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

    def set_buttons(self):
        open_button = Button(self.button_frame, 
                           text="Open DICOM", 
                           highlightbackground=self.primary_color,
                           command=self.open_file,
                           font=("Segoe UI", 10, "bold"))
        open_button.pack(side="left", padx=15, pady=8)

    def run(self):
        self.window.mainloop()