from pytube import YouTube

def startDownload(url):
    try:
        youtube_Obj = YouTube(url)  # Create a YouTub object from the url   
        video = youtube_Obj.streams.get_highest_resolution()   # Get the highest resolution video stream  
        video.download('C:/Users/User/OneDrive/Desktop/Sadeesha-Dias-DevArc Projects/U-TubeGrabby/videos')  # Download the video to defined folder
    except:
        print("There was an error in the URL!")
    print("Download Complete!")