from moviepy.editor import *

if __name__ == '__main__':
    mp4_file_name = '小城故事    鋼琴曲 抒情鋼琴曲 純鋼琴輕音樂 [精選集].mp4'
    mp3_file_name = '小城故事    鋼琴曲 抒情鋼琴曲 純鋼琴輕音樂 [精選集].mp3'
    # mp4_file_name = 'mp3_OK'
    print('save to mp3: %s' % mp3_file_name)

    video = VideoFileClip(mp4_file_name)
    video.audio.write_audiofile(mp3_file_name)
