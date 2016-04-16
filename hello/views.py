import json
from django.shortcuts import render
from django.http import HttpResponse

class JsonResponse(HttpResponse):
    def __init__(self, content, **kwargs):
        kwargs['content_type'] = 'application/json'
        if(isinstance(content, list)):
            super(JsonResponse, self).__init__(json.dumps([ob.__dict__ for ob in content]), **kwargs)
        else:
            super(JsonResponse, self).__init__(json.dumps(content), **kwargs)

class Message:
    def __init__(self, user, msg):
        self.user = user
        self.msg = msg

    def __str__( self ):
        return "{'user':  '%s', 'msg': '%s'}" % (self.user, self.msg)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

msgs = []
users = []
def index(request):
    return render(request, 'index.html')

def auth(request):
    global msgs
    global users
    name = request.GET['name'];
    users.append(name);

    return JsonResponse({'msg': "welcome"})

def logout(request):
    global msgs
    global users
    name = request.GET['name'];
    for i in range(len(users)):
        if(users[i]==name):
            del users[i]
            break
    return JsonResponse({'msg': "bye"})

def send(request):
    global msgs
    global users
    name = request.GET['name'];
    msg = request.GET['msg'];
    msgs.append(Message(name, msg))
    return JsonResponse({'msg': "ok"})

def get(request):
    global msgs
    global users
    return JsonResponse(msgs)
