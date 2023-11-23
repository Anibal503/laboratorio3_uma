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



auto1 = Auto(marca="Toyota", modelo="Corolla", asientos=5, color="Azul",
             tipo="Sedan", combustible="Gasolina", precio=26000, garantia=8, fecha_ingreso="15-julio-2022")

auto2 = Auto(marca="Nissan", modelo="Altima", asientos=5, color="Blanco",
             tipo="Sedan", combustible="Gasolina", precio=32000, garantia=5, fecha_ingreso="18-julio-2022")

auto1.mostrar_informacion()
auto2.mostrar_informacion()
