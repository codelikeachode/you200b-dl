from pytube import YouTube

def download_video(url):
    try:
        # Get the video from the URL
        yt = YouTube(url)
        
        # Get the highest quality video stream available
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        # Download the video to the current directory
        video.download()
        
        print("Video downloaded successfully")
    except Exception as e:
        print("An error occurred while downloading the video")
        print(e)
        
# Ask the user for the YouTube URL
url = input("Enter the YouTube URL: ")

# Download the video
download_video(url)