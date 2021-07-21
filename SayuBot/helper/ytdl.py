import os
import wget
import youtube_dl
from PIL import Image


class Youtube:
    def __init__(self, url, out):
        self.url = url
        self.out = out

    def download(self):
        url = self.url
        out = self.out
        video_info = youtube_dl.YoutubeDL().extract_info(url, download=False)
        # Demás datos, title, ext
        _title = video_info["title"]
        try:
            _ext = video_info["ext"]
        except KeyError:
            _ext = video_info["entries"][0]["formats"][0]["ext"]
        if _ext == "unknown_video":
            _ext = "mp4"
        # Options + Download
        options = {"format": "best",
                   "outtmpl": out + _title + "." + _ext}
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])
        return out + _title + "." + _ext

    def thumb(self):
        url = self.url
        out = self.out
        video_info = youtube_dl.YoutubeDL().extract_info(url, download=False)
        # Thumbnail?
        try:
            try:
                thumbnail = video_info["thumbnail"]
            except KeyError:
                thumbnail = video_info["entries"][0]["thumbnail"]
            data = wget.download(thumbnail, out)
            if data[-4:] == "webp":
                image = Image.open(data).convert("RGB")
                image.save(out + "thumb.jpg", "jpeg")
                os.unlink(data)
            elif data[-4:] == ".jpg":
                os.rename(data, out + "thumb.jpg")
        except Exception as e:
            print(e)
        if "thumb.jpg" in os.listdir(out):
            return True
        else:
            return False
