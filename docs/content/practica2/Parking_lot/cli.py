"""
cli.py  –  Menú de consola para el Simulador de Estacionamiento
Sesión 1: operaciones básicas (entrada, salida, ocupación, tickets activos)
"""
from datetime import datetime
from models.vehicle import Car, Motorcycle, VehicleType
from models.parking_lot import ParkingLot


# ── Helpers de presentación ────────────────────────────────────────────────────

def _separador(char="─", n=55):
    print(char * n)

def _titulo(texto: str):
    _separador()
    print(f"  {texto}")
    _separador()

def _menu():
    _titulo("🅿  SIMULADOR DE ESTACIONAMIENTO")
    print("  1. Registrar entrada")
    print("  2. Registrar salida")
    print("  3. Ver ocupación")
    print("  4. Ver tickets activos")
    print("  5. Salir")
    _separador()

def _pedir_tipo_vehiculo() -> VehicleType | None:
    print("  Tipo de vehículo:")
    print("    1. Auto (Car)")
    print("    2. Motocicleta (Motorcycle)")
    opcion = input("  Elige (1/2): ").strip()
    if opcion == "1":
        return VehicleType.CAR
    elif opcion == "2":
        return VehicleType.MOTORCYCLE
    else:
        print("  ⚠  Tipo inválido.")
        return None


# ── Operaciones ────────────────────────────────────────────────────────────────

def registrar_entrada(lot: ParkingLot):
    _titulo("REGISTRAR ENTRADA")
    placas = input("  Placas del vehículo: ").strip()
    if not placas:
        print("  ⚠  Las placas no pueden estar vacías.")
        return

    tipo = _pedir_tipo_vehiculo()
    if tipo is None:
        return

    try:
        vehicle = Car(placas) if tipo == VehicleType.CAR else Motorcycle(placas)
        ticket = lot.enter(vehicle, datetime.now())
        print(f"\n  ✅  Entrada registrada:")
        print(f"      Ticket  : #{ticket.get_id()}")
        print(f"      Vehículo: {vehicle}")
        print(f"      Spot    : {ticket.get_spot().get_id()}")
        print(f"      Hora    : {ticket.get_entry_time().strftime('%H:%M:%S')}")
    except ValueError as e:
        print(f"\n  ❌  Error: {e}")


def registrar_salida(lot: ParkingLot):
    _titulo("REGISTRAR SALIDA")
    try:
        ticket_id = int(input("  Número de ticket: ").strip())
    except ValueError:
        print("  ⚠  ID de ticket inválido.")
        return

    try:
        costo = lot.exit(ticket_id, datetime.now())
        print(f"\n  ✅  Salida registrada:")
        print(f"      Ticket  : #{ticket_id}")
        print(f"      Costo   : ${costo:.2f}")
        print(f"      Total recaudado: ${lot.get_total_revenue():.2f}")
    except ValueError as e:
        print(f"\n  ❌  Error: {e}")


def ver_ocupacion(lot: ParkingLot):
    _titulo("OCUPACIÓN DEL ESTACIONAMIENTO")
    occ = lot.get_occupancy()
    print(f"  Total  : {occ['total']} lugares")
    print(f"  Libres : {occ['free']}")
    print(f"  Ocupados: {occ['occupied']}")
    _separador("·")
    print("  Detalle de spots:")
    for spot in lot.get_spots():
        icono = "🔴" if spot.is_occupied() else "🟢"
        print(f"    {icono}  {spot}")


def ver_tickets_activos(lot: ParkingLot):
    _titulo("TICKETS ACTIVOS")
    tickets = lot.get_active_tickets()
    if not tickets:
        print("  (No hay vehículos en el estacionamiento)")
        return
    for t in tickets:
        print(f"  • {t}")


# ── Bucle principal ────────────────────────────────────────────────────────────

def run():
    lot = ParkingLot.create_default()
    print("\n  Estacionamiento inicializado con 10 spots (A1-A5, M1-M3, X1-X2).")
    print(f"  Política de cobro: {lot.get_policy()}")

    while True:
        print()
        _menu()
        opcion = input("  Elige una opción: ").strip()

        if opcion == "1":
            registrar_entrada(lot)
        elif opcion == "2":
            registrar_salida(lot)
        elif opcion == "3":
            ver_ocupacion(lot)
        elif opcion == "4":
            ver_tickets_activos(lot)
        elif opcion == "5":
            print("\n  ¡Hasta luego! 👋\n")
            break
        else:
            print("  ⚠  Opción no válida. Elige entre 1 y 5.")

        input("\n  [Enter para continuar...]")


if __name__ == "__main__":
    run()
