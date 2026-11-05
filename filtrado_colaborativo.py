ana = ["Matrix", "Inception", "Avatar", "Terminator", "Blade Runner", "Dune"]
carlos = ["Matrix", "Inception", "Terminator", "Titanic", "Gladiador", "Troya", "Corazon Valiente"]
elena = ["Shrek", "Frozen", "Enredados", "Toy Story", "Coco", "Moana", "Intensa Mente"]
marcos = ["Matrix", "Inception", "Avatar", "Terminator", "Blade Runner", "Interstellar", "Avengers", "Star Wars", "Guardianes de la Galaxia"]
luis = ["Matrix", "Avatar", "Dune", "Interstellar", "Batman", "Spider-Man", "Iron Man", "Joker"]
sofia = ["Titanic", "Enredados", "Coco", "Orgullo y Prejuicio", "Diario de una Pasion", "La La Land"]

nombres = ["Ana", "Carlos", "Elena", "Marcos", "Luis", "Sofia"]
listas_peliculas = [ana, carlos, elena, marcos, luis, sofia]

def buscar_posicion_usuario(nombre_buscar):
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre_buscar.lower():
            return i
    return -1

def peliculas_en_comun(lista1, lista2):
    comunes = []
    for i in range(len(lista1)):
        pelicula = lista1[i]
        if pelicula in lista2:
            comunes.append(pelicula)
    return comunes

def porcentaje_similitud(lista1, lista2):
    comunes = peliculas_en_comun(lista1, lista2)
    union = []

    for p in lista1:
        union.append(p)
    for p in lista2:
        if p not in union:
            union.append(p)

    if len(union) == 0:
        return 0
    return round((len(comunes) / len(union)) * 100, 1)

def ordenar_ranking(lista_ranking):
    n = len(lista_ranking)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ranking[j][1] < lista_ranking[j + 1][1]:
                aux = lista_ranking[j]
                lista_ranking[j] = lista_ranking[j + 1]
                lista_ranking[j + 1] = aux

def recomendar_peliculas(nombre_objetivo):
    pos = buscar_posicion_usuario(nombre_objetivo)
    if pos == -1:
        print("El usuario no existe.")
        return

    mis_peliculas = listas_peliculas[pos]
    print("Usuario seleccionado:", nombres[pos])
    print("Peliculas vistas por", nombres[pos] + ":", mis_peliculas)

    ranking_vecinos = []

    for i in range(len(nombres)):
        if i != pos:
            otra_lista = listas_peliculas[i]
            comunes = peliculas_en_comun(mis_peliculas, otra_lista)
            similitud = porcentaje_similitud(mis_peliculas, otra_lista)

            if len(comunes) > 0:
                ranking_vecinos.append([nombres[i], similitud, comunes, otra_lista])

    ordenar_ranking(ranking_vecinos)

    print("\n1. Comparacion de similitud con otros usuarios:")
    for v in ranking_vecinos:
        print(" -", v[0], "| Similitud:", str(v[1]) + "%", "| Coincidencias:", len(v[2]), "->", v[2])

    mejor_vecino = ranking_vecinos[0]
    nombre_mejor = mejor_vecino[0]
    similitud_mejor = mejor_vecino[1]
    peliculas_mejor = mejor_vecino[3]

    recomendacion_directa = []
    for p in peliculas_mejor:
        if p not in mis_peliculas:
            recomendacion_directa.append(p)

    print("\n2. Usuario mas parecido a", nombres[pos] + ":", nombre_mejor, "(" + str(similitud_mejor) + "% de similitud)")
    print("   RECOMENDACION FINAL PARA", nombres[pos].upper() + ":", recomendacion_directa)
    print("   Pelicula principal recomendada:", recomendacion_directa[0])


recomendar_peliculas("Ana")
