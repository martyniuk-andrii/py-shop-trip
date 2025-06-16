from dataclasses import dataclass

from app.car import Car


@dataclass
class Customer:
    _name: str
    _product_cart: dict[str, int]
    _location: list[int]
    _money: int | float
    _car: Car

    @property
    def name(self) -> str:
        return self._name

    @property
    def product_cart(self) -> dict[str, int]:
        return self._product_cart

    @property
    def location(self) -> list[int]:
        return self._location

    @location.setter
    def location(self, new_location: list[int]) -> None:
        if (
                len(new_location) == 2
                and all(isinstance(x, int) for x in new_location)
        ):
            self._location = new_location

    @property
    def money(self) -> int | float:
        return round(self._money, 2)

    @property
    def car(self) -> Car:
        return self._car

    def spend(self, amount: float) -> None:
        if amount > self._money:
            raise ValueError("Not enough money")
        self._money -= amount
