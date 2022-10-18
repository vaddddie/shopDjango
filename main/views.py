from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import LettersForm
from .models import Item

class index(View):
    items = Item.objects.all()
    template_name = 'main/index.html'

    def post(self, request, *args, **kwargs):
        letter_form = LettersForm(request.POST)
        context = {
            'items': self.items,
            'letter_form': letter_form,
        }

        if letter_form.is_valid():
            letter_form.save()
            return redirect('index')

        return render(request, self.template_name, context)
    
    def get(self, request, *args, **kwargs):
        letter_form = LettersForm()
        context = {
            'items': self.items,
            'letter_form': letter_form,
        }
        return render(request, self.template_name, context)


class shop(View):
    items = Item.objects.all()
    template_name = 'main/shop.html'

    def post(self, request, *args, **kwargs):
        letter_form = LettersForm(request.POST)
        context = {
            'items': self.items,
            'letter_form': letter_form,
        }

        if letter_form.is_valid():
            letter_form.save()
            return redirect('index')

        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        letter_form = LettersForm()
        context = {
            'items': self.items,
            'letter_form': letter_form,
        }
        return render(request, self.template_name, context)
