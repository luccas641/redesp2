import json
from django.shortcuts import render
from django.http import HttpResponse

class JsonResponse(HttpResponse):
    def __init__(self, content, **kwargs):
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(json.dumps(content), **kwargs)

class JsonDataResponse(HttpResponse):
    """
    Returns a json dumped dict with fields 'message' and 'data'.

    """
    def __init__(self, *args, **kwargs):
        message = None
        data = None
        if len(args) > 0:
            message = args[0]
        if len(args) > 1:
            data = args[1]
        if 'message' in kwargs:
            message = kwargs['message']
        kwargs.pop('message')
        if 'data' in kwargs:
            data = kwargs['data']
            kwargs.pop('data')

        kwargs['content'] = json.dumps(dict(message=message, data=data))

        if 'content_type' not in kwargs:
            kwargs['content_type'] = 'application/json'

        super(JsonDataResponse, self).__init__(**kwargs)

matrix = [[0 for x in range(3)] for x in range(3)]
player = 0
count = 0
i = 0
n = False

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def auth(request):
    global count

    count = count + 1
    if(count>2):
        return JsonResponse({"player": "error"})

    return JsonResponse({'player': count})

def postChoice(request):
    global i
    global player

    i = request.GET['i']
    player = (player +1) %2
    return JsonResponse({'msg': "ok"})


def getChoice(request):
    p = int(request.GET['p'])-1

    global n
    if(n==True):
        return JsonResponse({'player': 2})

    if(p==player):
        return JsonResponse({'id': i})

    return JsonResponse({'msg': "error"})

def new(request):
    global player
    global count
    global n

    if(n==False):
        count = 0
        player = 0
        i = 0
        n = True
    else:
        n = False
    return JsonResponse({'msg': "ok"})
