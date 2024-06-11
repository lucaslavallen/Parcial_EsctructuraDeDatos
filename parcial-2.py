
# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:


dinosaurios = [

    {"nombre": "Tyrannosaurus Rex", "especie": "Theropoda", "peso": "7000 kg", "descubridor": "Barnum Brown", "ano_descubrimiento": 1902}, 
    {"nombre": "Triceratops", "especie": "Ceratopsidae", "peso": "6000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1889}, 
    {"nombre": "Velociraptor", "especie": "Dromaeosauridae", "peso": "15 kg", "descubridor": "Henry Fairfield Osborn", "ano_descubrimiento": 1924}, 
    {"nombre": "Brachiosaurus", "especie": "Sauropoda", "peso": "56000 kg", "descubridor": "Elmer S. Riggs", "ano_descubrimiento": 1903}, 
    {"nombre": "Stegosaurus", "especie": "Stegosauridae", "peso": "5000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1877}, 
    {"nombre": "Spinosaurus", "especie": "Spinosauridae", "peso": "10000 kg", "descubridor": "Ernst Stromer", "ano_descubrimiento": 1912}, 
    {"nombre": "Allosaurus", "especie": "Theropoda", "peso": "2000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1877}, 
    {"nombre": "Apatosaurus", "especie": "Sauropoda", "peso": "23000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1877}, 
    {"nombre": "Diplodocus", "especie": "Sauropoda", "peso": "15000 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1878}, 
    {"nombre": "Carnotaurus", "especie": "Theropoda", "peso": "1500 kg", "descubridor": "José Bonaparte", "ano_descubrimiento": 1985}, 
    {"nombre": "Styracosaurus", "especie": "Ceratopsidae", "peso": "2700 kg", "descubridor": "Lawrence Lambe", "ano_descubrimiento": 1913}, 
    {"nombre": "Therizinosaurus", "especie": "Therizinosauridae", "peso": "5000 kg", "descubridor": "Evgeny Maleev", "ano_descubrimiento": 1954}, 
    {"nombre": "Pteranodon", "especie": "Pterosauria", "peso": "25 kg", "descubridor": "Othniel Charles Marsh", "ano_descubrimiento": 1876}, 
    {"nombre": "Quetzalcoatlus", "especie": "Pterosauria", "peso": "200 kg", "descubridor": "Douglas A. Lawson", "ano_descubrimiento": 1971}, 
    {"nombre": "Plesiosaurus", "especie": "Plesiosauria", "peso": "450 kg", "descubridor": "Mary Anning", "ano_descubrimiento": 1824}, 
    {"nombre": "Mosasaurus", "especie": "Mosasauridae", "peso": "15000 kg", "descubridor": "William Conybeare", "ano_descubrimiento": 1829}

]


# a)Contar cuantas especies hay;

def contar_especies(dinosaurios):
    especies = set(dino['especie'] for dino in dinosaurios)
    return len(especies)

numero_especies = contar_especies(dinosaurios)
print(f"Número de especies: {numero_especies}")


# b)Determinar cuantos descubridores distintos hay;
def contar_descubridores(dinosaurios):
    descubridores = set(dino['descubridor'] for dino in dinosaurios)
    return len(descubridores)

numero_descubridores = contar_descubridores(dinosaurios)
print(f"Número de descubridores distintos: {numero_descubridores}")


# c)Mostrar todos los dinosaurios que empiecen con T;
def mostrar_dinosaurios_con_t(dinosaurios):
    dinos_t = []
    for dino in dinosaurios:
        if dino['nombre'][0] == "T":
            dinos_t.append(dino['nombre'])
    return dinos_t

dinosConT = mostrar_dinosaurios_con_t(dinosaurios)
print("Dinosaurios que empiezan con T:")
for nombre in dinosConT:
    print(nombre)

# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg

def mostrar_dinosaurios_ligeros(dinosaurios, peso_limite):
    dinos_ligeros = []
    for dino in dinosaurios:
        peso = int(dino['peso'][:-3])  
        if peso < peso_limite:
            dinos_ligeros.append(dino['nombre'])
    return dinos_ligeros


dinos_ligeros = mostrar_dinosaurios_ligeros(dinosaurios, 275)
print("Dinosaurios que pesan menos de 275 Kg:")
print(dinos_ligeros)



# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

def separar_dinosaurios(dinosaurios, letras):
    nueva_pila = []
    pila_restante = []
    
    for dino in dinosaurios:
        if dino['nombre'][0] in letras:
            nueva_pila.append(dino)
        else:
            pila_restante.append(dino)
    
    return nueva_pila, pila_restante

letras = {'A', 'Q', 'S'}
nueva_pila, pila_restante = separar_dinosaurios(dinosaurios, letras)

# Imprime dinosaurios en la nueva pila
print("Dinosaurios en la nueva pila (A, Q, S):")
for dino in nueva_pila:
    print(dino['nombre'])


