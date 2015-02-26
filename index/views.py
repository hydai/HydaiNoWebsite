from django.shortcuts import render

# Create your views here.
def index(request):
    """index: Main page"""
    return render(request, 'index/index.html')

def custom_404(request):
    """custom 404 page"""
    return render(request, 'base/404.html', status=404)

def custom_500(request):
    """custom 500 page"""
    return render(request, 'base/500.html', status=500)

def base_html(request):
    """basic html frame of all pages"""
    return render(request, 'base/base.html')
