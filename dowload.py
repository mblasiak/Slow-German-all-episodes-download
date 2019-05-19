import urllib.request
import urllib.error

for i in range(183, 1, -1):
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
