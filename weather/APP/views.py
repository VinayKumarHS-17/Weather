from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    context = {}
    city = request.GET.get('q')
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8a98f0710adbe624a8e81cec137b2200"

    try:
        resp = requests.get(url=URL)
        data=resp.json()
        if resp.status_code==200: 
            data['main']['temp']=round(data['main']['temp']-273.15,2)
            return render(request,'search.html',{'resp':data})
        else:
            return render(request,'search.html',{'e':'City not found'})
    
    except requests.exceptions.RequestException as e:
        return render(request,'search.html',{'e':str(e)})
    