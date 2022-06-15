from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView

def news(request):
    news = News.objects.all()
    return render(request, 'main_app/main.html', {'news': news})

class NewsDetailView(DetailView):
    model = News
    template_name = 'main_app/datails_view.html'
    context_object_name = 'article'

def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма была не верной'
    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main_app/create.html', data)

def register(request):
    pass

