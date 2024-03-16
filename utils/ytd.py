from pytube import YouTube


def youtube(url):
    youtube_data = YouTube(url)
    streams = youtube_data.streams.filter(progressive=True)
    title = streams[0].title.strip()
    data = [f"*{i.mime_type}*: {i.url}\n_{i.filesize_mb}mb_" for i in streams]
    return f"""*{title}*\n{''.join(data)}"""
