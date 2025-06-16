from dataclasses import dataclass
from typing import Any


@dataclass
class Car:
    _characteristics_of_the_car: dict[str, Any]

    def brand_car(self) -> str:
        return self._characteristics_of_the_car["brand"]

    def fuel_consumption(self) -> float:
        return self._characteristics_of_the_car["fuel_consumption"]

    def road_price(self, distance: float, fuel_price: float) -> float:
        amount_of_fuel = (distance / 100) * self.fuel_consumption()
        return (amount_of_fuel * fuel_price) * 2
