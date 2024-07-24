import json
import random

# Base de datos simulada
usuarios = {}
productos = {
    "tecnologia": {
        1: "Laptop",
        2: "Smartphone",
        3: "Tablet",
        4: "Smartwatch",
        5: "Auriculares",
        6: "Cámara",
        7: "Impresora",
        8: "Monitor",
        9: "Teclado",
        10: "Ratón"
    },
    "alimentos": {
        11: "Manzanas",
        12: "Pan",
        13: "Leche",
        14: "Queso",
        15: "Huevos",
        16: "Carne",
        17: "Pasta",
        18: "Arroz",
        19: "Cereal",
        20: "Yogur"
    },
    "belleza": {
        21: "Shampoo",
        22: "Acondicionador",
        23: "Jabón",
        24: "Loción",
        25: "Crema facial",
        26: "Maquillaje",
        27: "Perfume",
        28: "Desodorante",
        29: "Esmalte de uñas",
        30: "Cepillo"
    }
}

# Funciones auxiliares
def guardar_datos():
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)

def cargar_datos():
    global usuarios
    try:
        with open('usuarios.json', 'r') as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        usuarios = {}

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    if nombre in usuarios:
        print("Usuario ya registrado.")
    else:
        usuarios[nombre] = {"historial": []}
        print(f"Usuario {nombre} registrado con éxito.")
        guardar_datos()

def mostrar_productos():
    print("Productos disponibles:")
    for categoria, items in productos.items():
        print(f"\nCategoría: {categoria.capitalize()}")
        for id, producto in items.items():
            print(f"  {id}. {producto}")

def recomendar_producto(nombre):
    if usuarios[nombre]["historial"]:
        ultima_compra = usuarios[nombre]["historial"][-1]
        categoria_ultima_compra = next((cat for cat, items in productos.items() if ultima_compra in items), None)
        similares = [id for id in productos[categoria_ultima_compra] if id != ultima_compra]
        if similares:
            recomendacion = random.choice(similares)
            print(f"Basado en tu última compra, te recomendamos: {productos[categoria_ultima_compra][recomendacion]}")
            eleccion = input("¿Deseas comprar el producto recomendado? (s/n): ").lower()
            if eleccion == 's':
                usuarios[nombre]["historial"].append(recomendacion)
                print(f"Has comprado {productos[categoria_ultima_compra][recomendacion]}.")
                guardar_datos()
        else:
            print("No hay productos similares para recomendar.")
    else:
        print("No hay historial de compras para hacer recomendaciones.")

def comprar_producto(nombre):
    mostrar_productos()
    eleccion = int(input("Ingrese el ID del producto que desea comprar: "))
    if any(eleccion in items for items in productos.values()):
        usuarios[nombre]["historial"].append(eleccion)
        categoria = next(cat for cat, items in productos.items() if eleccion in items)
        print(f"Has comprado {productos[categoria][eleccion]}.")
        guardar_datos()
        recomendar_producto(nombre)
    else:
        print("Producto no válido.")

def menu():
    cargar_datos()
    while True:
        print("\n1. Registrar usuario")
        print("2. Comprar producto")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            registrar_usuario()
        elif opcion == 2:
            nombre = input("Ingrese su nombre: ")
            if nombre in usuarios:
                comprar_producto(nombre)
            else:
                print("Usuario no registrado.")
        elif opcion == 3:
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú
menu()