import os
import threading
import time
import tkinter
import customtkinter
from pytube import YouTube

# import custome functions
from check_internet_connection_function import check_internet_connection

#Function implementation
def startDownload(url, downloadPath):
    try:
        youtube_Obj = YouTube(url, on_progress_callback=onProgress)  # Create a YouTub object from the url   
        video = youtube_Obj.streams.get_highest_resolution()   # Get the highest resolution video stream  
        video.download(downloadPath)
        print("Download Completed!")
    except Exception as e:
        print("An error occured during the download: ", e)

def onProgress(stream, chunk, bytes_remaining):
    totalFile_size = stream.filesize
    print('TTZ: ',totalFile_size)
    print('remaining bytes: ',bytes_remaining)
    downloaded = totalFile_size - bytes_remaining
    print('downloaded bytes: ',downloaded)
    percent = int(downloaded / totalFile_size * 100)
    print('Percent: ', percent)
    percent_str = str(percent)
    print('Percent string: ', percent_str)
    

    progress_text.configure(text=percent_str + '%')
    progress_bar.set(float(percent) / 100)
    progress_text.update()
    progress_bar.update()


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

# Setting the progress bar
progress_bar = customtkinter.CTkProgressBar(app, width=450)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=30)

# Setting up progress label
progress_text = customtkinter.CTkLabel(app, text="Downloaded: 0")
progress_text.pack()


# Adding download button
def downloadVideo():
    
    url = url_entry_field.get()
    download_path = os.path.join(os.path.dirname(__file__), "vidoes")
    os.makedirs(download_path, exist_ok=True)

    if (check_internet_connection()):
        download_thread = threading.Thread(target=startDownload, args=(url, download_path))
        download_thread.start()
        print("Downloading...")    
    else:
        print("download failed")

download_button = customtkinter.CTkButton(app, text="Download", command=downloadVideo)
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