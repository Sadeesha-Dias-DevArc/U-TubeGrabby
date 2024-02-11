import tkinter
import customtkinter
#from pytube import YouTube

# import defined functions
from analyze_and_download_function import startDownload
from check_internet_connection_function import check_internet_connection


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

# Adding footer with checking internet connection functionality
def update_footer():
    if check_internet_connection():
        footer.configure(fg_color="#00FA9A")
        footer_label.configure(text="Connected")
    else:
        footer.configure(fg_color="#DC143C")
        footer_label.configure(text="Not Connected")
    footer.after(1000, update_footer) # Check internet every second

footer = customtkinter.CTkFrame(app, fg_color=None, height=10)
footer.pack(side='bottom', fill='x')

footer_label = customtkinter.CTkLabel(footer, text="Checking internet  connection...", text_color='#000000', justify=tkinter.CENTER)
footer_label.pack()

update_footer() # Start checking and updating footer

# Run application
app.mainloop()