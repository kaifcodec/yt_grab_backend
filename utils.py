import re
from pytube import YouTube

def is_valid_youtube_url(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return re.match(youtube_regex, url) is not None

def get_video_info(url):
    yt = YouTube(url)
    return {
        "title": yt.title,
        "length": yt.length,
        "author": yt.author,
        "views": yt.views,
        "thumbnail_url": yt.thumbnail_url
    }

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    output_path = stream.download()
    return output_path
