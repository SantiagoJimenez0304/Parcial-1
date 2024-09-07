from models.cliente import Cliente
from models.ventana import Ventana
from models.nave import Nave
from models.vidrio import Vidrio
from models.aluminio import Aluminio
from models.descuento import Descuento
from models.cotizacion import Cotizacion


def calcular_total(ventana, vidrio, aluminio, descuento, cantidad):
    # Calcular el perímetro de la ventana (2 veces el alto y el ancho)
    perimetro_ventana = 2 * (ventana.obtenerAncho() + ventana.obtenerAlto())
    
    # Costo del aluminio (costo por cm lineal multiplicado por el perímetro)
    costo_aluminio = perimetro_ventana * aluminio.obtenerCostoCmLineal()
    print(f"Costo de aluminio: {costo_aluminio}")
    
    # Calcular el área del vidrio (restar los marcos de aluminio)
    area_ventana = (ventana.obtenerAncho() - 3) * (ventana.obtenerAlto() - 3)
    
    # Costo del vidrio (costo por cm² multiplicado por el área)
    costo_vidrio = area_ventana * vidrio.costo_cm2
    print(f"Costo de vidrio: {costo_vidrio}")
    
    # Si el vidrio es esmerilado, se añade un costo adicional
    if vidrio.esmerilado:
        costo_vidrio += area_ventana * 5.20  # Costo adicional del esmerilado
        print(f"Costo adicional por esmerilado: {area_ventana * 5.20}")

    # Costo fijo de las esquinas (4 esquinas)
    costo_esquinas = 4 * 4310
    print(f"Costo de esquinas: {costo_esquinas}")
    
    # Costo total de una ventana
    total_ventana = costo_aluminio + costo_vidrio + costo_esquinas
    print(f"Costo total por ventana: {total_ventana}")
    
    # Calcular el total sin descuento (multiplicando por la cantidad)
    total_sin_descuento = total_ventana * cantidad
    print(f"Total sin descuento para {cantidad} ventanas: {total_sin_descuento}")
    
    return total_sin_descuento

    return total_final

def main():
    print("===== Sistema de Cotización de Ventanas PQR =====")
    
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")
    cliente = Cliente(nombre_cliente, 1, direccion_cliente)  # ID ficticio
    
    # Estilos de la ventana
    estilo_ventana = input("Ingrese el estilo de la ventana (O, XO, OXXO): ")
    ancho_ventana = float(input("Ingrese el ancho de la ventana en cm: "))
    alto_ventana = float(input("Ingrese el alto de la ventana en cm: "))
    ventana = Ventana(estilo_ventana, ancho_ventana, alto_ventana)
    
    # Información del vidrio
    tipo_vidrio = input("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ")
    esmerilado = input("¿El vidrio será esmerilado? (si/no): ").lower() == 'si'
    if tipo_vidrio == "Transparente":
        costo_cm2 = 8.25
    elif tipo_vidrio == "Bronce":
        costo_cm2 = 9.15
    elif tipo_vidrio == "Azul":
        costo_cm2 = 12.75
    else:
        print("Tipo de vidrio no válido, se asignará Transparente.")
        costo_cm2 = 8.25
    vidrio = Vidrio(tipo_vidrio, esmerilado, costo_cm2)
    
    # Información del aluminio
    tipo_acabado = input("Ingrese el tipo de acabado de aluminio (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ")
    if tipo_acabado == "Pulido":
        costo_cm_lineal = 50.7
    elif tipo_acabado == "Lacado Brillante":
        costo_cm_lineal = 54.2
    elif tipo_acabado == "Lacado Mate":
        costo_cm_lineal = 53.6
    elif tipo_acabado == "Anodizado":
        costo_cm_lineal = 57.3
    else:
        print("Tipo de acabado no válido, se asignará Pulido.")
        costo_cm_lineal = 50.7
    aluminio = Aluminio(tipo_acabado, costo_cm_lineal)

    # Información del descuento
    cantidad = int(input("Ingrese la cantidad de ventanas: "))
    descuento = Descuento(10, 100)  # Descuento del 10% si supera 100 ventanas

    total = calcular_total(ventana, vidrio, aluminio, descuento, cantidad)
    
    # Mostrar resultados
    print("\n===== Resumen de la Cotización =====")
    print(f"Cliente: {cliente.obtenerNombre()}")
    print(f"Dirección: {cliente.obtenerDireccion()}")
    print(f"Ventana: Estilo {ventana.obtenerEstilo()}, {ventana.obtenerAncho()} cm x {ventana.obtenerAlto()} cm")
    print(f"Vidrio: {vidrio.tipo}, Esmerilado: {'Sí' if vidrio.esmerilado else 'No'}")
    print(f"Aluminio: Acabado {aluminio.obtenerTipoAcabado()}")
    print(f"Cantidad de ventanas: {cantidad}")
    print(f"Total a pagar: ${total:.2f} COP")

if __name__ == "__main__":
    main()
