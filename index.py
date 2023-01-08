from pathlib import Path
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from sys import argv

# Check if there are two command line arguments: (1) the program name, and (2) the URL of the YouTube video to download
if len(argv) == 2:
  try:
    # Get the video by its URL
    video = YouTube(argv[1], use_oauth = True, allow_oauth_cache = True)

    # Print relevant information about the video
    print("\nDownloading \"", video.title, "\" by ", video.author, sep = "")
    print("Published on", video.publish_date.strftime("%b %d, %Y"))
    print(f'{video.views:,}', "views")

    # Get the highest-resolution, progressive stream of the video
    stream = video.streams.get_highest_resolution()

    # Specify the current user's Downloads folder as the download path
    download_path = str(Path.home() / "Downloads")

    # Download the video to the above path
    output_path = stream.download(output_path = download_path)

    # Print the download path
    print("\nDownloaded to", output_path)
  
  # Handle an invalid video URL
  except RegexMatchError:
    print("Invalid URL. Please try again.")
# Handle an invalid number of command line arguments
else:
  print("Please provide the URL of the YouTube video you would like to download.")