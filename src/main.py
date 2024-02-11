import tkinter
import customtkinter
from pytube import YouTube

# Application window settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Application window frame settings
app = customtkinter.CTk()
app.geometry("720x480")
app.title("U-TubeGrabby")

# Run application
app.mainloop()