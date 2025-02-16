from django. shortcuts import render, redirect 
from django.db.models import Q 
from django.contrib.auth.models import User 
from models import Room, Topic 
from .forms import RoomForm


def home(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'room.html')
# Create your views here.


def loginpage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            except: 

                context = {}
                return render(request, 'base/login_register.html', context)

                def home(request):
                    q = request.GET.get('q') if request.GET.get('q') != None else 

                    rooms = Room.objects.filter(
                        Q(topic__name__icontains=q) |
                        Q (name__icontains=q) |
                        Q(description__icontains=q)
                    )

@login_required(Login_url='login')
def deleteMessage(request, pk):
    message = message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
        return render(request, 'base/delete.html', {'obj' : message})
        