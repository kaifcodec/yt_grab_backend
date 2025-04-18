import re
import yt_dlp
import os
import json
def is_valid_youtube_url(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return re.match(youtube_regex, url) is not None

def get_video_info(url):
    """
    Extracts video metadata using yt-dlp with cookies.txt for authentication.
    Assumes cookies.txt is located in the root directory of the repository.
    """
    ydl_opts = {
        'cookiefile': 'cookies.txt'  # Directly use cookies.txt from the root directory
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title"),
            "length": info.get("duration"),
            "author": info.get("uploader"),
            "views": info.get("view_count"),
            "thumbnail_url": info.get("thumbnail")
        }

def download_video(url):
    """
    Downloads a video using yt-dlp, authenticating with cookies.txt.
    """
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'cookiefile': 'cookies.txt',  # Points to the uploaded cookies.txt file
        'verbose': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])
        return result

def create_cookies_file():
    """
    Creates a cookies.txt file using the COOKIES_FILE_CONTENT environment variable,
    preserving the Netscape format.
    """
    cookie_file_content = os.getenv("COOKIES_FILE_CONTENT")
    if cookie_file_content:
        with open("cookies.txt", "w") as f:
            f.write(cookie_file_content)
        print("cookies.txt file created successfully!")
        # Remove the os.system("cat cookies.txt") line for cleaner logs in production
    else:
        print("COOKIES_FILE_CONTENT environment variable is not set.")
