from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about-me/">Acerca de</a></li>
        <li><a href="/portfolio/">Portfolio</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

def home(request):
    return HttpResponse(html_base + """
        <h2>Bienvenidos</h2>
        <p>Esto es la portada.</p>
    """)

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Francisco y me encanta Django!</p>
    """)

def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portfolio</h2>
        <p>Algunos de mis trabajos</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Aquí puedes contactar conmigo</p>
    """)
