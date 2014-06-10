import json
import requests
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'index.html')


def ask(request):
    question = request.GET.get('question')
    try:
        response = requests.post('http://default-environment-sdqm3mrmp4.elasticbeanstalk.com/AWSBot'
                                 '?request={}'.format(question.encode('utf-8')))
        message = response.content
    except:
        message = "I'm a little busy now, will ping you later :)"
    return HttpResponse(message)
