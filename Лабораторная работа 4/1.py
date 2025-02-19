from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Базовый класс для всех транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int):
        self._brand = brand  # Инкапсуляция, так как изменять бренд после создания объекта не имеет смысла
        self._model = model  # Инкапсуляция, аналогично с моделью
        self.year = year

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r})"

    @abstractmethod
    def start_engine(self) -> None:
        """
        Абстрактный метод для запуска двигателя.
        """
        pass


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int):
        super().__init__(brand, model, year)
        self.doors = doors

    def start_engine(self) -> None:
        """
        Перегруженный метод запуска двигателя.
        У легкового автомобиля может быть бесключевой доступ.
        """
        print(f"{self.brand} {self.model}: Двигатель запущен с кнопки.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, doors={self.doors!r})"


class Truck(Vehicle):
    """
    Дочерний класс для грузовых автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int, load_capacity: float):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def start_engine(self) -> None:
        """
        Перегруженный метод запуска двигателя.
        Грузовики обычно требуют механический запуск двигателя.
        """
        print(f"{self.brand} {self.model}: Двигатель запущен ключом.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, load_capacity={self.load_capacity!r})"


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 4)
    truck = Truck("Volvo", "FH16", 2020, 25.0)

    print(car)
    print(repr(car))
    car.start_engine()

    print(truck)
    print(repr(truck))
    truck.start_engine()
