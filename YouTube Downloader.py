from yt_dlp import YoutubeDL

def download_youtube_video(url, output_folder='downloads'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage:
if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)