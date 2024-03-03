# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import room

@login_required
def rooms_view(request):
    # Your view logic goes here
    rooms = room.objects.all()
    return render(request, 'room/room.html', {'rooms': rooms})


@login_required
def oneroom(request, slug):
    room_obj = room.objects.get(slug=slug)  # Use a different variable name, e.g., room_obj
    return render(request, 'room/onechatroom.html', {'room': room_obj})
