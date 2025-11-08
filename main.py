from tkinter import *
import matplotlib.pyplot as plt
import pydicom
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from PIL.Image import Resampling 

from viewer_app import viewer_app

app = viewer_app()
app.run()