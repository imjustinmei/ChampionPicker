from django.shortcuts import render
from partypes.models import Partype

from champions.models import Champion

# Create your views here.


def index(request):
    partypes = Partype.objects.all()
    champions = Champion.objects.all().order_by('partype_id', 'name')

    if champions.count() == 0:
        return redirect("/")

    context = {'partypes': partypes, 'champions': champions}
    return render(request, 'partypes.html', context)
