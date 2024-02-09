from django.shortcuts import render
from app.models import Player
from app.models import ODS

# Create your views here.
def index(request):
    players = Player.objects.all()
    count = ODS.objects.count
    #Player.objects.get_or_create()
    context = {'ball': 'blabla', 'players': players, 'count' : count}

    return render(request, 'index.html', context)


def test(request):
    calcule = 8+4

    context = {'ball': 'blabla', 'calcule': calcule}
    return render(request, 'test.html', context)
