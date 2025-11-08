from tkinter import Frame, Label

class info_panel(Frame):
    def __init__(self, parent, **kw):
        # Voláme super PRED konfiguráciou
        super().__init__(parent, **kw)
        
        self.primary_color = "#57534D"
        self.text_light = "#ecf0f1"      
        
        self.text_color = self.text_light
        self.labels = []
        
        self.create_labels()
        self.set_layout()

    def create_labels(self):
        title_label = Label(self, text="Patient Information", 
                           bg=self.cget("bg"), fg="white",
                           font=("Segoe UI", 18, "bold"))  # Zväčšené písmo
        title_label.grid(row=0, column=0, sticky="w", padx=15, pady=(15, 20))
     
        names = ["Patient Name", "Patient ID", "Modality", "Study Date", "Image Size"]
        for i in range(len(names)):
            label = Label(self, text=names[i] + ": --", 
                         bg=self.cget("bg"), fg=self.text_color,
                         font=("Segoe UI", 12),  # Zväčšené písmo
                         anchor="w", wraplength=230) 
            self.labels.append(label)

    def set_layout(self):
        for i in range(len(self.labels)):
            self.labels[i].grid(row=i+1, column=0, sticky="w", padx=15, pady=10)

    def update_info(self, info):
        for i in range(len(self.labels)):
            self.labels[i].config(text=info[i])
