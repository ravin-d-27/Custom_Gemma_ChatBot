from django.shortcuts import render
import json
from gradio_client import Client
from decouple import config

url = config("API_LINK")
client = Client(url)


def home(request):
    return render(request, 'myapp/home.html')

def pred(request):
    return render(request, 'myapp/preds.html')

def find(request):
    
    if request.method == 'POST':
        input_data = {"query":request.POST['review']}
        input_data_j = json.dumps(input_data)
        result = client.predict(input_data_j,api_name='/predict')
        print(result["output"])

    return render(request, 'myapp/finder.html', {"rev":result["output"]})