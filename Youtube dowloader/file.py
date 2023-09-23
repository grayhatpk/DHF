from pytube import YouTube

def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path)
        print("Download successful!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
