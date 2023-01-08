from pathlib import Path
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from sys import argv

if len(argv) == 2:
  try:
    video = YouTube(
      argv[1],
      use_oauth = True,
      allow_oauth_cache = True
    )

    print("\nDownloading \"", video.title, "\" by ", video.author, sep = "")
    print("Published on", video.publish_date.strftime("%b %d, %Y"))
    print(f'{video.views:,}', "views")

    stream = video.streams.get_highest_resolution()

    download_path = str(Path.home() / "Downloads")
    output_path = stream.download(output_path = download_path)

    print("\nDownloaded to", output_path)
  except RegexMatchError:
    print("Invalid URL. Please try again.")
else:
  print("Please provide the URL of the YouTube video you would like to download.")