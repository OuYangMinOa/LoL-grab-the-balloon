import requests
import bs4
import pyperclip

last_lol = None

while True:
	url = "https://forum.gamer.com.tw/C.php?bsn=17532&snA=674866&tnum=9129"

	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
	}

	req  = requests.get(url,headers=headers)
	soup = bs4.BeautifulSoup(req.content,"lxml")

	get_text = soup.find_all("article", class_="reply-content__article c-article")[4].text

	if ("LOL" in get_text and last_lol != get_text):
		L_start  = get_text.index("L")
		last_lol = get_text
		LOL      = get_text[L_start:L_start+13]
		print(LOL)

		pyperclip.copy(LOL)
