import tkinter
import customtkinter
#from pytube import YouTube

# import defined functions
from analyze_and_download_function import startDownload


# Application window settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Application window frame settings
app = customtkinter.CTk()
app.geometry("720x480")
app.title("U-TubeGrabby")

# UI elements
# Adding URL lable
url_label = customtkinter.CTkLabel(app, text="Copy and paste the YouTube URL")
url_label.pack(padx=10, pady=10)

#  Adding URL entry field
link_var = tkinter.StringVar()
url_entry_field = customtkinter.CTkEntry(app, width=350, height=40, textvariable=link_var)
url_entry_field.pack(padx=10, pady=10)

# Adding download button
def downloadVideo():
    startDownload(url_entry_field.get())
download_button = customtkinter.CTkButton(app, text="Analyze", command=downloadVideo)
download_button.pack(padx=10, pady=10)

# Run application
app.mainloop()