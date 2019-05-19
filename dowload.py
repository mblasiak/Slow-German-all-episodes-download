import urllib.request
import urllib.error

latest_podcast_number=183
for i in range(latest_podcast_number, 1, -1):
    path="path/to/download"
    try:
        if i > 173:
            urllib.request.urlretrieve("https://cdn.podseed.org/slowgerman/sg" + str(i) + ".mp3",
                                       path+"/sg" + str(i) + ".mp3")
        else:
            urllib.request.urlretrieve("https://slowgerman.com/folgen/sg" + str(i) + ".mp3",
                                       path+"/sg" + str(i) + ".mp3")
    except urllib.error.HTTPError:
        print("No mp3 " + str(i))
