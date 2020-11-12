from django.shortcuts import render,HttpResponse
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')

def song(request,song):
    song = song.replace('_','/')
    url = "https://songsear.ch/"+song

    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    info = soup.find_all('div', class_="text-center")
    s_name = info[0].contents[1]
    s_by = info[0].contents[2]

    lyrics = soup.find_all('blockquote')[0]

    div = BeautifulSoup("<div></div>", 'html.parser')
    div.append(s_name)
    div.append(s_by)
    div.append(lyrics)

    return HttpResponse(div)
