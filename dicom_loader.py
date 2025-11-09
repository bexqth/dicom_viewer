import pydicom
from PIL import Image
from tkinter import filedialog

class dicom_loader:
    def __init__(self):
        self.filepath = ""
        self.dataset = None
        self.image = None
        self.pixel_array = None

        self.patient_name = ""
        self.patient_id = ""
        self.modality = ""
        self.study_date = ""
        self.image_size = ""

    def open_file(self):
        pass

    def load_dicom_image(self, filepath):
        self.dataset = pydicom.dcmread(filepath)
        self.pixel_array = self.dataset.pixel_array
        self.image = Image.fromarray(self.pixel_array)

    def set_patient_info(self):
        self.patient_name = self.dataset.PatientName 
        self.patient_id = self.dataset.PatientID
        self.modality = self.dataset.Modality
        date_str = str(self.dataset.StudyDate)
        if len(date_str) == 8:
            year = date_str[0:4]
            month = date_str[4:6]
            day = date_str[6:8]
            self.study_date = f"{day}.{month}.{year}"
        else:
            self.study_date = date_str 
        self.image_size =  f"{self.dataset.Rows} x {self.dataset.Columns}"

    def get_tk_image(self):
        return self.tk_image

    def get_patient_name(self):
        return self.patient_name
    
    def get_patient_id(self):
        return self.patient_id
    
    def get_modality(self):
        return self.modality
    
    def get_study_date(self):
        return self.study_date
    
    def get_image_size(self):
        return self.image_size