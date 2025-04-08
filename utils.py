import re
import yt_dlp
import os
from uuid import uuid4

def is_valid_youtube_url(url):
    pattern = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return bool(pattern.match(url))

def download_video(url):
    video_id = str(uuid4())
    output_path = f"{video_id}.mp4"

    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_path
