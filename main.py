import requests
import re
import json

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'
TIMEOUT = 15

headers = {'User-Agent': UA}
sess = requests.Session()
cuk = ""
stream_url = ''

def get_key_from_url(url):
    try:
        response = requests.get(url)
        keys = response.text.split('\n')
        return keys
    except Exception as e:
        print("Error fetching keys:", e)
        return []

keys = get_key_from_url('https://raw.githubusercontent.com/blacksourcellc/tutupasswordyuh/keys/password.txt')

def getkey(pwd=False):
    if keys:
        return keys[0]  # Assuming the first line is the key
    else:
        print("No keys found.")
        return ''

def PlayVideo(url):   
    try:
        key = getkey()
        html = sess.get(url, headers=headers).text
        cuk = sess.cookies.get_dict()

        # Extracting necessary data from HTML
        html = html.replace("\'", '"')
        streamtok = re.findall('stream\-name\s*=\s*"([^"]+)"', html, re.DOTALL + re.I)
        csrf_token = re.findall('csrf\-token"\s*content\s*=\s*"([^"]+)"', html, re.DOTALL)[0]

        # Updating headers
        headers.update({
            "X-CSRF-TOKEN": csrf_token,
            "Content-Type": "application/json",
        })

        # Making the POST request to retrieve the token
        json_data = {"password": key}
        response = sess.post('https://thetvapp.to/token/' + streamtok[0], headers=headers, json=json_data)
        stream_url = response.text

        # Displaying headers, cookies, and stream URL
        headers_to_display = {
            'User-Agent': headers['User-Agent'],
            'X-CSRF-TOKEN': headers['X-CSRF-TOKEN'],
            'Cookie': sess.cookies.get_dict(),
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Alt-Used': 'thetvapp.to',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Content-Length': '27',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',

        }
       
        print("Stream URL:", stream_url)

        # Save headers to a JSON file
        with open('headers.json', 'w') as f:
            json.dump(headers_to_display, f, indent=4)

    except Exception as e:
        print("Error:", e)

PlayVideo("https://thetvapp.to/tv/ae-live-stream/")
