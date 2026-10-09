from django.shortcuts import render

# ---------------------------------------------------------
# VISTA 1: TERROR
# ---------------------------------------------------------
def terror(request):
    peliculas = [
        {"nombre": "The Babadook", "anio": 2014, "imagen": "images/babadook.png"},
        {"nombre": "La Bruja", "anio": 2015, "imagen": "images/bruja.jpg"},
        {"nombre": "El Conjuro", "anio": 2013, "imagen": "images/conjuro.jpg"},
        {"nombre": "El Exorcista", "anio": 1973, "imagen": "images/Exorcista.jpg"},
        {"nombre": "Hereditary", "anio": 2018, "imagen": "images/Hereditary.jpg"},
        {"nombre": "Insidious", "anio": 2010, "imagen": "images/Insidious.jpg"},
        {"nombre": "It", "anio": 2017, "imagen": "images/it.jpg"},
        {"nombre": "Actividad Paranormal", "anio": 2007, "imagen": "images/Paranormal.jpg"},
        {"nombre": "Un Lugar en Silencio", "anio": 2018, "imagen": "images/silencio.jpg"},
        {"nombre": "Siniestro", "anio": 2012, "imagen": "images/Siniestro.jpg"},
    ]
    context = {
        'genero': 'Terror',
        'peliculas': peliculas
    }
    return render(request, 'genero/terror.html', context)


# ---------------------------------------------------------
# VISTA 2: CRIMEN
# ---------------------------------------------------------
def crimen(request):
    peliculas = [
        {"nombre": "Fargo", "anio": 1996, "imagen": "images/Fargo.jpg"},
        {"nombre": "Heat", "anio": 1995, "imagen": "images/heat.jpg"},
        {"nombre": "Infiltrados", "anio": 2006, "imagen": "images/infiltrados.png"},
        {"nombre": "Buenos Muchachos", "anio": 1990, "imagen": "images/muchacho.jpg"},
        {"nombre": "El Padrino", "anio": 1972, "imagen": "images/padrino.jpg"},
        {"nombre": "Prisioneros", "anio": 2013, "imagen": "images/Prisoners.jpg"},
        {"nombre": "Pulp Fiction", "anio": 1994, "imagen": "images/Pulp.jpg"},
        {"nombre": "Scarface", "anio": 1983, "imagen": "images/scarface.png"},
        {"nombre": "Seven", "anio": 1995, "imagen": "images/seven.png"},
        {"nombre": "Zodiac", "anio": 2007, "imagen": "images/zodiac.jpg"},
    ]
    context = {
        'genero': 'Crimen',
        'peliculas': peliculas
    }
    return render(request, 'genero/crimen.html', context)


# ---------------------------------------------------------
# VISTA 3: COMEDIA
# ---------------------------------------------------------
def comedia(request):
    peliculas = [
        {"nombre": "Mi Pobre Angelito", "anio": 1990, "imagen": "images/angelito.jpg"},
        {"nombre": "Click", "anio": 2006, "imagen": "images/click.png"},
        {"nombre": "Son como niños", "anio": 2010, "imagen": "images/comoNinos.jpg"},
        {"nombre": "Deadpool", "anio": 2016, "imagen": "images/Deadpool.jpg"},
        {"nombre": "La Máscara", "anio": 1994, "imagen": "images/mascara.jpg"},
        {"nombre": "¿Qué pasó ayer?", "anio": 2009, "imagen": "images/quePaso.avif"},
        {"nombre": "Scary Movie", "anio": 2000, "imagen": "images/scary.jpg"},
        {"nombre": "Shrek", "anio": 2001, "imagen": "images/shrek.jpg"},
        {"nombre": "Supercool", "anio": 2007, "imagen": "images/superCool.jpg"},
        {"nombre": "Tonto y Retonto", "anio": 1994, "imagen": "images/tonto.png"},
    ]
    context = {
        'genero': 'Comedia',
        'peliculas': peliculas
    }
    return render(request, 'genero/comedia.html', context)

# ---------------------------------------------------------
# VISTA 3: ROMANCE
# ---------------------------------------------------------

def romance(request):
    peliculas = [
        {"nombre": "Titanic", "anio": 1997, "imagen": "images/titanic.PNG"},
        {"nombre": "Diario de una Pasión", "anio": 2004, "imagen": "images/diario_de_una_pasion.PNG"},
        {"nombre": "Orgullo y Prejuicio", "anio": 2005, "imagen": "images/orgullo_y_prejuicio.PNG"},
        {"nombre": "La La Land", "anio": 2016, "imagen": "images/la_la_land.jpg"},
        {"nombre": "Eterno Resplandor de una Mente sin Recuerdos", "anio": 2004, "imagen": "images/eterno_resplandor.PNG"},
        {"nombre": "Yo Antes de Ti", "anio": 2016, "imagen": "images/yo_antes_de_ti.jpg"},
        {"nombre": "Bajo la Misma Estrella", "anio": 2014, "imagen": "images/bajo_la_misma_estrella.PNG"},
        {"nombre": "Antes del Amanecer", "anio": 1995, "imagen": "images/antes_del_amanecer.PNG"},
        {"nombre": "Cuestión de Tiempo", "anio": 2013, "imagen": "images/cuestion_de_tiempo.PNG"},
        {"nombre": "500 Días con Ella", "anio": 2009, "imagen": "images/500_dias_con_ella.PNG"},
    ]
    context = {
        'genero': 'Romance',
        'peliculas': peliculas
    }
    return render(request, 'genero/romance.html', context)

# ---------------------------------------------------------
# VISTA 3: SUSPENSO
# ---------------------------------------------------------

def suspenso(request):
    peliculas = [
        {"nombre": "Perdida (Gone Girl)", "anio": 2014, "imagen": "images/gone_girl.PNG"},
        {"nombre": "El Silencio de los Inocentes", "anio": 1991, "imagen": "images/silencio_inocentes.PNG"},
        {"nombre": "Los Otros (The Others)", "anio": 2001, "imagen": "images/the_others.PNG"},
        {"nombre": "El Sexto Sentido", "anio": 1999, "imagen": "images/sexto_sentido.PNG"},
        {"nombre": "La Isla Siniestra", "anio": 2010, "imagen": "images/isla_siniestra.PNG"},
        {"nombre": "Fragmentado", "anio": 2016, "imagen": "images/fragmentado.PNG"},
        {"nombre": "Prisioneros", "anio": 2013, "imagen": "images/prisioneros.PNG"},
        {"nombre": "Corre (Run)", "anio": 2020, "imagen": "images/run.PNG"},
        {"nombre": "El Club de la Pelea", "anio": 1999, "imagen": "images/fight_club.PNG"},
        {"nombre": "El Efecto Mariposa", "anio": 2004, "imagen": "images/efecto_mariposa.PNG"},
    ]
    context = {
        'genero': 'Suspenso',
        'peliculas': peliculas
    }
    return render(request, 'genero/suspenso.html', context)