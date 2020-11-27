from django.shortcuts import render
from cardlist.models import Card

def index(request):
    latest_card_list = Card.objects.all().order_by('card_id')[:55]
    context = {'latest_card_list':latest_card_list}
    return render(request, 'cardlist/index.html', context)

def detail(request, card_id):
    row = Card.objects.get(pk = card_id)
    return render(request, 'cardlist/detail.html', {'row': row})
        # Create your views here.
