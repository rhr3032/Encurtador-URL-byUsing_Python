#pip install pyshorteners
import pyshorteners


url = "yourURl"

shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)
print(short_url)