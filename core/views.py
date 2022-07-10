from django.views.generic import View
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'pages/index.html', context)