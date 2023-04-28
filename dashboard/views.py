from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from item.models import Item


# Create your views here.

@login_required
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    
    return render(request, 'dashboard/dashboard.html', {
        'items' : items,
    })
