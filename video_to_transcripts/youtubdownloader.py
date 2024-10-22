"""
source used to lean whisper: https://octalbyte.com/youtube_downloader/
created: 10/10/24
Author: Steven Fuller
"""
import yt_dlp
import os

def youtube_downloader(video_url):  
    # directory to download videos to
    download_path = 'Videos/'
    os.makedirs(download_path, exist_ok=True)

    # settings for youtube downloader
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'restrictfilenames': True,
        'noplaylist': False,  # Changed to allow playlist downloads
        'ignoreerrors': True,
    }

    # loop that will download each video in a playlist
    # modified from single video downloader on : https://octalbyte.com/youtube_downloader/
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Set download=True to start downloading immediately
            info = ydl.extract_info(video_url, download=True)  

            # Check if the info contains entries for playlists
            if 'entries' in info:
                for item in info['entries']:
                    filename = ydl.prepare_filename(item)
                    print(f"Downloading: {filename}")  
                    ydl.download([item['url']])  
                    print(f"Downloaded: {filename}")  
            else:
                filename = ydl.prepare_filename(info)
                print(f"Downloading: {filename}")  
                ydl.download([info['url']])  
                print(f"Downloaded: {filename}")  
        # exceptions so that the program runs even if there is an error
        except yt_dlp.utils.DownloadError as e:
            print(f"Skipped: {video_url} - {e}") 
        except Exception as e:  
            print(f"An unexpected error occurred: {e}")  

if __name__ == "__main__":
    # Prompt user for playlist url input
    video_url = input("Please enter the video URL or playlist URL: ")  
    youtube_downloader(video_url)  