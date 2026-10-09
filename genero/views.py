from django.shortcuts import render

# ---------------------------------------------------------
# VISTA 1: TERROR
# ---------------------------------------------------------
def terror(request):
    peliculas = [
        {"nombre": "The Babadook", "anio": 2014, "imagen": "images/babadook.png", "descripcion": "Una madre viuda y su hijo son atormentados por un monstruo que surge de las páginas de un siniestro libro infantil."},
        {"nombre": "La Bruja", "anio": 2015, "imagen": "images/bruja.jpg", "descripcion": "Una familia puritana en la Nueva Inglaterra de 1630 se desmorona ante fuerzas oscuras y misteriosas del bosque."},
        {"nombre": "El Conjuro", "anio": 2013, "imagen": "images/conjuro.jpg", "descripcion": "Los investigadores paranormales Ed y Lorraine Warren ayudan a una familia aterrorizada por una presencia maligna en su granja."},
        {"nombre": "El Exorcista", "anio": 1973, "imagen": "images/Exorcista.jpg", "descripcion": "Dos sacerdotes luchan por salvar el alma de una niña de 12 años poseída por una entidad demoníaca milenaria."},
        {"nombre": "Hereditary", "anio": 2018, "imagen": "images/Hereditary.jpg", "descripcion": "Tras la muerte de la abuela matriarca, una familia empieza a descubrir secretos crípticos y aterradores sobre su linaje."},
        {"nombre": "Insidious", "anio": 2010, "imagen": "images/Insidious.jpg", "descripcion": "Un matrimonio descubre que su hijo en coma se ha convertido en un recipiente para fantasmas de una dimensión oscura."},
        {"nombre": "It", "anio": 2017, "imagen": "images/it.jpg", "descripcion": "Un grupo de niños marginados de Derry enfrenta a un cambiaformas demoníaco que toma la forma de un temible payaso."},
        {"nombre": "Actividad Paranormal", "anio": 2007, "imagen": "images/Paranormal.jpg", "descripcion": "Una pareja joven instala cámaras en su casa tras percibir fenómenos extraños, desatando sucesos escalofriantes."},
        {"nombre": "Un Lugar en Silencio", "anio": 2018, "imagen": "images/silencio.jpg", "descripcion": "En un mundo invadido por depredadores guiados por el sonido, una familia lucha por sobrevivir en absoluto mutismo."},
        {"nombre": "Siniestro", "anio": 2012, "imagen": "images/Siniestro.jpg", "descripcion": "Un escritor de crímenes reales descubre una caja de películas en super 8 con asesinatos brutales cometidos en su nueva casa."},
    ]
    context = {'genero': 'Terror', 'peliculas': peliculas}
    return render(request, 'genero/terror.html', context)


# ---------------------------------------------------------
# VISTA 2: CRIMEN
# ---------------------------------------------------------
def crimen(request):
    peliculas = [
        {"nombre": "Fargo", "anio": 1996, "imagen": "images/Fargo.jpg", "descripcion": "Un endeudado vendedor de autos orquesta el secuestro de su esposa, desencadenando una sangrienta cadena de crímenes."},
        {"nombre": "Heat", "anio": 1995, "imagen": "images/heat.jpg", "descripcion": "Un astuto ladrón de bancos y un detective obsesivo de Los Ángeles juegan una peligrosa partida de ajedrez táctico."},
        {"nombre": "Infiltrados", "anio": 2006, "imagen": "images/infiltrados.png", "descripcion": "Un policía encubierto en la mafia irlandesa y un topo de la mafia en la policía intentan identificarse mutuamente."},
        {"nombre": "Buenos Muchachos", "anio": 1990, "imagen": "images/muchacho.jpg", "descripcion": "La fascinante y destructiva historia del ascenso y caída de Henry Hill en el crimen organizado de Nueva York."},
        {"nombre": "El Padrino", "anio": 1972, "imagen": "images/padrino.jpg", "descripcion": "El patriarca de una dinastía mafiosa transfiere el control de su imperio clandestino a su hijo más reservado."},
        {"nombre": "Prisioneros", "anio": 2013, "imagen": "images/Prisoners.jpg", "descripcion": "La desesperada búsqueda de un padre que decide tomar la justicia en sus manos al desaparecer su pequeña hija."},
        {"nombre": "Pulp Fiction", "anio": 1994, "imagen": "images/Pulp.jpg", "descripcion": "Las vidas de dos matones, la esposa de un gángster y un boxeador se cruzan en relatos entrelazados llenos de violencia."},
        {"nombre": "Scarface", "anio": 1983, "imagen": "images/scarface.png", "descripcion": "Tony Montana, un refugiado cubano en Miami, construye violentamente un gigantesco imperio del narcotráfico."},
        {"nombre": "Seven", "anio": 1995, "imagen": "images/seven.png", "descripcion": "Dos detectives rastrean la pista de un metódico asesino serial que utiliza los siete pecados capitales como temática."},
        {"nombre": "Zodiac", "anio": 2007, "imagen": "images/zodiac.jpg", "descripcion": "La obsesiva cacería del infame Asesino del Zodiaco contada por periodistas e investigadores en San Francisco."},
    ]
    context = {'genero': 'Crimen', 'peliculas': peliculas}
    return render(request, 'genero/crimen.html', context)


# ---------------------------------------------------------
# VISTA 3: COMEDIA
# ---------------------------------------------------------
def comedia(request):
    peliculas = [
        {"nombre": "Mi Pobre Angelito", "anio": 1990, "imagen": "images/angelito.jpg", "descripcion": "Un ingenioso niño de ocho años es olvidado por su familia y debe defender su casa de dos torpes ladrones."},
        {"nombre": "Click", "anio": 2006, "imagen": "images/click.png", "descripcion": "Un adicto al trabajo obtiene un control remoto mágico capaz de adelantar, pausar y rebobinar momentos de su vida."},
        {"nombre": "Son como niños", "anio": 2010, "imagen": "images/comoNinos.jpg", "descripcion": "Cinco amigos de la infancia se reúnen años después junto a sus familias para pasar un fin de semana lleno de risas."},
        {"nombre": "Deadpool", "anio": 2016, "imagen": "images/Deadpool.jpg", "descripcion": "Un mercenario irreverente adquiere poderes de curación acelerada y sale en busca de venganza con humor descarado."},
        {"nombre": "La Máscara", "anio": 1994, "imagen": "images/mascara.jpg", "descripcion": "Un tímido empleado bancario encuentra una máscara de origen nórdico que libera su alocada y carismática personalidad."},
        {"nombre": "¿Qué pasó ayer?", "anio": 2009, "imagen": "images/quePaso.avif", "descripcion": "Tres padrinos de boda despiertan de una despedida de soltero en Las Vegas sin recordar nada y sin el novio."},
        {"nombre": "Scary Movie", "anio": 2000, "imagen": "images/scary.jpg", "descripcion": "Divertida y disparatada parodia que se burla de los clichés más populares de las películas de terror adolescente."},
        {"nombre": "Shrek", "anio": 2001, "imagen": "images/shrek.jpg", "descripcion": "Un ogro solitario emprende un viaje para rescatar a una particular princesa y recuperar la paz de su hogar."},
        {"nombre": "Supercool", "anio": 2007, "imagen": "images/superCool.jpg", "descripcion": "Dos inseparables amigos de secundaria se ven envueltos en absurdas desventuras intentando conseguir alcohol para una fiesta."},
        {"nombre": "Tonto y Retonto", "anio": 1994, "imagen": "images/tonto.png", "descripcion": "Dos amigos muy despistados atraviesan el país para devolverle un maletín perdido a una hermosa mujer."},
    ]
    context = {'genero': 'Comedia', 'peliculas': peliculas}
    return render(request, 'genero/comedia.html', context)

# ---------------------------------------------------------
# VISTA 3: ROMANCE
# ---------------------------------------------------------

def romance(request):
    peliculas = [
        {"nombre": "Titanic", "anio": 1997, "imagen": "images/titanic.PNG", "descripcion": "Un joven artista y una chica de clase alta se enamoran a bordo del transatlántico más famoso de la historia."},
        {"nombre": "Diario de una Pasión", "anio": 2004, "imagen": "images/diario_de_una_pasion.PNG", "descripcion": "Un romance apasionado entre dos jóvenes de distintas clases sociales marcado por las cartas y el paso del tiempo."},
        {"nombre": "Orgullo y Prejuicio", "anio": 2005, "imagen": "images/orgullo_y_prejuicio.PNG", "descripcion": "Elizabeth Bennet y el orgulloso señor Darcy enfrentan malentendidos y diferencias sociales en la Inglaterra rural."},
        {"nombre": "La La Land", "anio": 2016, "imagen": "images/la_la_land.PNG", "descripcion": "Una aspirante a actriz y un pianista de jazz luchan por alcanzar sus sueños profesionales en Los Ángeles."},
        {"nombre": "Eterno Resplandor de una Mente sin Recuerdos", "anio": 2004, "imagen": "images/eterno_resplandor.PNG", "descripcion": "Una expareja decide someterse a un procedimiento médico para borrar mutuamente los recuerdos de su fallida relación."},
        {"nombre": "Yo Antes de Ti", "anio": 2016, "imagen": "images/yo_antes_de_ti.PNG", "descripcion": "Una joven alegre y peculiar es contratada para cuidar a un adinerado banquero que quedó tetrapléjico tras un accidente."},
        {"nombre": "Bajo la Misma Estrella", "anio": 2014, "imagen": "images/bajo_la_misma_estrella.PNG", "descripcion": "Dos adolescentes que se conocen en un grupo de apoyo para pacientes con cáncer emprenden un viaje juntos."},
        {"nombre": "Antes del Amanecer", "anio": 1995, "imagen": "images/antes_del_amanecer.PNG", "descripcion": "Un joven estadounidense y una estudiante francesa se conocen en un tren y pasan una noche inolvidable recorriendo Viena."},
        {"nombre": "Cuestión de Tiempo", "anio": 2013, "imagen": "images/cuestion_de_tiempo.PNG", "descripcion": "Un joven descubre que los hombres de su familia pueden viajar en el tiempo e intenta conquistar al amor de su vida."},
        {"nombre": "500 Días con Ella", "anio": 2009, "imagen": "images/500_dias_con_ella.PNG", "descripcion": "Un redactor de tarjetas reflexiona de forma no lineal sobre los 500 días que pasó junto a una mujer escéptica del amor."},
    ]
    context = {
        'genero': 'Romance',
        'peliculas': peliculas
    }
    return render(request, 'genero/romance.html', context)


# --------------------------------------------------
# VISTA 3: SUSPENSO
# --------------------------------------------------

def suspenso(request):
    peliculas = [
        {"nombre": "Perdida (Gone Girl)", "anio": 2014, "imagen": "images/gone_girl.PNG", "descripcion": "La misteriosa desaparición de una mujer en su aniversario de bodas convierte a su esposo en el principal sospechoso."},
        {"nombre": "El Silencio de los Inocentes", "anio": 1991, "imagen": "images/silencio_inocentes.PNG", "descripcion": "Una joven agente del FBI recurre a la ayuda del brillante caníbal Hannibal Lecter para atrapar a un asesino serial."},
        {"nombre": "Los Otros (The Others)", "anio": 2001, "imagen": "images/the_others.PNG", "descripcion": "Una madre protege a sus hijos fotosensibles en una mansión aislada donde extrañas presencias comienzan a manifestarse."},
        {"nombre": "El Sexto Sentido", "anio": 1999, "imagen": "images/sexto_sentido.PNG", "descripcion": "Un psicólogo infantil intenta ayudar a un niño atormentado por su capacidad para ver y comunicarse con los muertos."},
        {"nombre": "La Isla Siniestra", "anio": 2010, "imagen": "images/isla_siniestra.PNG", "descripcion": "Dos agentes federales viajan a un hospital psiquiátrico en una isla remota para investigar la fuga de una peligrosa reclusa."},
        {"nombre": "Fragmentado", "anio": 2016, "imagen": "images/fragmentado.PNG", "descripcion": "Un hombre con 23 personalidades distintas secuestra a tres adolescentes mientras una oscura entidad amenaza con emerger."},
        {"nombre": "Prisioneros", "anio": 2013, "imagen": "images/prisioneros.PNG", "descripcion": "Tras la desaparición de su hija pequeña y ante la falta de pistas policiales, un padre desesperado toma la justicia en sus manos."},
        {"nombre": "Corre (Run)", "anio": 2020, "imagen": "images/run.PNG", "descripcion": "Una adolescente en silla de ruedas comienza a sospechar de los oscuros secretos que oculta su sobreprotectora madre."},
        {"nombre": "El Club de la Pelea", "anio": 1999, "imagen": "images/fight_club.PNG", "descripcion": "Un oficinista insomne y un carismático vendedor de jabón forman un club clandestino con reglas brutales."},
        {"nombre": "El Efecto Mariposa", "anio": 2004, "imagen": "images/efecto_mariposa.PNG", "descripcion": "Un joven descubre cómo viajar a su infancia leyendo sus viejos diarios, pero cada cambio que realiza altera drásticamente su presente."},
    ]
    context = {
        'genero': 'Suspenso',
        'peliculas': peliculas
    }
    return render(request, 'genero/suspenso.html', context)