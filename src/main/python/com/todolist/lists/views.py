#!/usr/bin/env python

from django.shortcuts import render, redirect
from lists.models import Item


def main_view(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'main.html', {'items': items})
