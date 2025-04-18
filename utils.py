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

import os

import os

def create_cookies_file():
    """
    Creates a properly formatted cookies.txt file using the COOKIES_FILE_CONTENT environment variable.
    """
    cookie_file_content = os.getenv("COOKIES_FILE_CONTENT")
    if cookie_file_content:
        with open("cookies.txt", "w") as f:
            # Write only valid cookie lines
            for line in cookie_file_content.strip().split("\n"):
                # Skip empty lines and comments
                if line.strip().startswith("#") or not line.strip():
                    continue
                
                # Split and validate fields
                fields = line.split()
                if len(fields) == 7:
                    # Join fields with tabs and write to the file
                    formatted_line = "\t".join(fields) + "\n"
                    f.write(formatted_line)
                else:
                    print(f"Skipping invalid line: {line.strip()}")
        print("cookies.txt file created successfully!")
    else:
        print("COOKIES_FILE_CONTENT environment variable is not set.")
