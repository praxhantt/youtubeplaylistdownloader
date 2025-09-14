import yt_dlp

playlist_url = "paste_link_here"  # Replace with your playlist URL
download_path = "D:/Downloads/ytplaylistdo"  # Replace with your download folder

ydl_opts = {
    'outtmpl': f'{download_path}/%(playlist_index)s - %(title)s.%(ext)s',  # Filename template with playlist index
    'format': 'bestvideo+bestaudio/best',  # Best video and audio merged
    'ignoreerrors': True,
    'quiet': False,
    'noplaylist': False,  # Download entire playlist
    'restrictfilenames': True,  # Avoid special characters in filenames
    'nopart': True,  # Disable .part files for simplicity
    'overwrites': True,  # Overwrite existing files
    'merge_output_format': 'mp4',  # Force merged video to be in mp4 format
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

