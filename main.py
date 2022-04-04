from pytube import YouTube

yt_url = 'https://www.youtube.com/watch?v=_Cx4wGMzw-M&t=5324s'
yt = YouTube(yt_url)

print(yt.streams.desc())
mp4_file_name = yt.streams[0].title
print('Download: %s...' % mp4_file_name)
yt.streams.get_highest_resolution().download()
