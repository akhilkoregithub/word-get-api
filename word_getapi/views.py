from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Word

class WordGetApi(View):
    def get(self, request):
        word_obj = Word.objects.first()
        if word_obj:
            word = word_obj.word
        else:
            word = "Test"
        return JsonResponse({'word': word})
