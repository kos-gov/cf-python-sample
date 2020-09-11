from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, HttpResponseNotFound
from home import envs

# Create your views here.


def index(request):

    data = {'cfapp': envs.get_apps(), 'cfservice': envs.get_svcs()}

    return render(request, 'index.html', data)


def error(request):
    # return HttpResponseNotFound('<h1>not found</h1>')
    raise Http404("Not Found")


def ping(request):
    fp = open('ping.txt', mode='r')
    context = fp.read()
    fp.close()
    return HttpResponse(context, content_type="application/text")
