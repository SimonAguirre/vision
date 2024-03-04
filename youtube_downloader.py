from pytube import YouTube

def download_youtube_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print(f"Video downloaded successfully: {yt.title}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage: replace the URL with the desired YouTube video URL
video_url = input("Enter the YouTube video URL: ")
download_youtube_video(video_url)