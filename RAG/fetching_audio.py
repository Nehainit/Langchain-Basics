import os

video_url = "https://www.youtube.com/watch?v=J5_-l7WIO_w"

# Download audio as mp3 using yt-dlp
# os.system(f'yt-dlp -x --audio-format mp3 -o "test_export/audio.%(ext)s" {video_url}')
# os.system(f'yt-dlp -o "test_export/video.%(ext)s" {video_url}')
os.system(f'yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 -o "test_export/best_video.%(ext)s" {video_url}')


