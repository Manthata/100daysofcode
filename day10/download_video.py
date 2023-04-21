

import requests
url = ''

file_name = 'trial_video.mp4' 
resp = requests.get(url) # making requests to server
with open(file_name,'wb') as f:
    f.write(resp.content)

