import re
import yt_dlp
import os

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
    Creates a cookies.txt file using the COOKIES environment variable.
    """
    cookie_data = os.getenv("COOKIES")
    if cookie_data:
        with open("cookies.txt", "w") as f:
            for cookie in cookie_data.split("; "):
                name, value = cookie.split("=")
                f.write(f".youtube.com\tTRUE\t/\tFALSE\t1893456000\t{name}\t{value}\n")
        print("cookies.txt file created successfully!")
    else:
        print("COOKIES environment variable is not set.")
