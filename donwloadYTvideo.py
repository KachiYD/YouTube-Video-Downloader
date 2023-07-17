from pytube import YouTube

#This code only downloads non-age restricted videos

link = input("Enter Youtube Video link: ")

ytVideo = YouTube(link)

finalVideo = ytVideo.streams.get_highest_resolution()

path = input("Enter the path to download the video to: ")

finalVideo.download(path)

print("\nCongratulations!! Your video \"{0}\" has been downloaded to \"{1}\"".format(ytVideo.title, path))
