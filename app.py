from gtts import gTTS 
import requests 
from bs4 import BeautifulSoup 
import sys 

def createMP3(data, fn):
  gTTS(data).save('{0}.mp3'.format(fn))

def get_data(url):
  data = requests.get(url).text
  return BeautifulSoup(data, 'html.parser').get_text()

args = sys.argv[1:]
#print(args)
print("creating audio book...")
createMP3(get_data(args[1]), args[0])
print("created audio book")