from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs


# Create your views here.
def home(request):
    return render(request, 'index.html')

def search(request):
    if request.method == "POST":
        search = request.POST['search']
        url = 'https://www.ask.com/web?q=' + search
        res = requests.get(url)
        soup = bs(res.text, 'lxml')

        resultList = soup.find_all('div', {'class': 'PartialSearchResults-item'})
        final = []
        for result in resultList:
            result_title = result.find(class_='PartialSearchResults-item-title').text
            result_url = result.find('a').get('href')
            result_desc = result.find(class_='PartialSearchResults-item-abstract').text

            final.append((result_title,result_url,result_desc))
        context = {"final":final}

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
    