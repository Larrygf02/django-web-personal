from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """
    <h1>Mi web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/portafolio/">Portafolio</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return HttpResponse(html_base + "<h2>Acerca de</h2>")


def portafolio(request):
    return HttpResponse(html_base + "<h2>Portafolio</h2>")

def contact(request):
    return HttpResponse(html_base + "<h2>Contacto</h2>")