from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from .forms import FindForm
from django.db.models import Q

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

#create model
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm()
    }
    return render(request, 'hello/create.html', params)

#edit model
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

#delete model
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)

#find model
def find(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        list = str.split()
        data = Friend.objects.filter(name__in=list)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)
