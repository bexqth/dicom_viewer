from tkinter import Label
from PIL import ImageTk

class image_panel(Label):

    def __init__(self, parent, **kw):
        super().__init__(parent)
        self.tk_image = None

    def display_dicom_image(self, image, width, height):
        self.config(bg="#0a0f16")
        self.config(image="")
        self.update()

        img_resized = image.resize((width, height))
        self.tk_image = ImageTk.PhotoImage(img_resized)
        self.config(image= self.tk_image)
        self.image = self.tk_image