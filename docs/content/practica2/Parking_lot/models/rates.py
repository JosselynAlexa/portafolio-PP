from abc import ABC, abstractmethod
from models.vehicle import Vehicle


class RatePolicy(ABC):
    """
    Interfaz / abstracción para la política de cobro.
    Cualquier implementación concreta debe definir calculate().
    """

    @abstractmethod
    def calculate(self, hours: float, vehicle: Vehicle) -> float:
        """Calcula el costo dado el tiempo y el vehículo."""
        ...

    def __str__(self):
        return self.__class__.__name__


class HourlyRatePolicy(RatePolicy):
    """Cobra por hora según el tipo de vehículo."""

    def __init__(self, car_rate: float = 20.0, moto_rate: float = 10.0):
        if car_rate < 0 or moto_rate < 0:
            raise ValueError("Las tarifas no pueden ser negativas.")
        self._car_rate = car_rate
        self._moto_rate = moto_rate

    def calculate(self, hours: float, vehicle: Vehicle) -> float:
        from models.vehicle import VehicleType
        rate = (
            self._car_rate
            if vehicle.get_type() == VehicleType.CAR
            else self._moto_rate
        )
        return round(hours * rate, 2)

    def __str__(self):
        return f"HourlyRate(auto=${self._car_rate}/h, moto=${self._moto_rate}/h)"
