class Auto:
    def __init__(auto, marca, modelo, asientos, color, tipo, combustible, precio, garantia, fecha_ingreso):
        auto.marca = marca
        auto.modelo = modelo
        auto.asientos = asientos
        auto.color = color
        auto.tipo = tipo
        auto.combustible = combustible
        auto.precio = precio
        auto.garantia = garantia
        auto.fecha_ingreso = fecha_ingreso

    def mostrar_informacion(auto):
        print(f"Marca: {auto.marca}")
        print(f"Modelo: {auto.modelo}")
        print(f"Asientos: {auto.asientos}")
        print(f"Color: {auto.color}")
        print(f"Tipo: {auto.tipo}")
        print(f"Precio: ${auto.precio}")
        print(f"Garantia: {auto.garantia} años")
        print(f"Fecha: {auto.fecha_ingreso}\n")



