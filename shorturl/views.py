from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
from .forms import URLForm

def shorten_url(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_url = ShortURL.objects.create(original_url=original_url)
            return render(request, 'shorturl/success.html', {'short_url': short_url})
    else:
        form = URLForm()
    return render(request, 'shorturl/index.html', {'form': form})

def redirect_to_original(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(short_url.original_url)
