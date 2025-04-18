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
    ydl_opts = {
        'cookiefile': 'cookies.txt'  # Use cookies from the cookies.txt file
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
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'cookiefile': 'cookies.txt'  # Use cookies from the cookies.txt file
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])
        return result

def create_cookies_file():
    """
    Creates a cookies.txt file using the COOKIES_FILE_CONTENT environment variable.
    """
    cookie_file_content = os.getenv("COOKIES_FILE_CONTENT")
    if cookie_file_content:
        with open("cookies.txt", "w") as f:
            f.write(cookie_file_content)
        print("cookies.txt file created successfully!")
    else:
        print("COOKIES_FILE_CONTENT environment variable is not set.")
