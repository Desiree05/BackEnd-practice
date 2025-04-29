from django.shortcuts import render, HttpResponse

html_base = """
<h1>¡Bienvenido!</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de...</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contacto/">Contacto</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + """
        <h2>Portada</h2>
        <p>Esto es la portada</p>
        """)


def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de...</h2>
        <p>Me llamo Victoria y soy programadora.</p>
        """)

def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portfolio</h2>
        <h3>Mis proyectos:</h3>
        """)

def contacto(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Aquí os dejo mi email: desimarce05@gmail.com</p>
        """)