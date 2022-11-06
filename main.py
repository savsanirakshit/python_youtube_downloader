from pytube import YouTube

link = input("Enter Youtube Link")
print("Download Started...")
YouTube(link).streams.first().download()
print("Download Successfully...")