from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class TreeType(Enum):
    DECIDUOUS = "Лиственное"
    CONIFEROUS = "Хвойное"

class Tree(ABC):
    def __init__(self, name: str, age: int, tree_type: TreeType):
        self.name = name
        self.age = age
        self.tree_type = tree_type

    @abstractmethod
    def get_info(self) -> str:
        pass

    def __str__(self) -> str:
        return self.get_info()

class ForestTree(Tree):
    def __init__(self, name: str, age: int, tree_type: TreeType, wood_volume: float):
        super().__init__(name, age, tree_type)
        self.wood_volume = wood_volume

    def get_info(self) -> str:
        return (f"[Лесное] {self.name:<12} | Возраст: {self.age:>3} лет | "
                f"Тип: {self.tree_type.value:<10} | Древесина: {self.wood_volume:>6.1f} м³")

class FruitTree(Tree):
    def __init__(self, name: str, age: int, tree_type: TreeType, yield_mass: float, shelf_life_days: int):
        super().__init__(name, age, tree_type)
        self.yield_mass = yield_mass
        self.shelf_life_days = shelf_life_days

    def get_info(self) -> str:
        return (f"[Плодовое] {self.name:<11} | Возраст: {self.age:>3} лет | "
                f"Тип: {self.tree_type.value:<10} | Урожай: {self.yield_mass:>5.1f} кг | "
                f"Хранение: {self.shelf_life_days:>3} дн.")

class TreeContainer:
    def __init__(self):
        self._trees: List[Tree] = []

    def add_tree(self, tree: Tree):
        self._trees.append(tree)

    def print_all(self):
        if not self._trees:
            print("Контейнер пуст.")
            return
        for tree in self._trees:
            print(tree)

    def count_by_tree_type(self, tree_type: TreeType) -> int:
        return sum(1 for t in self._trees if t.tree_type == tree_type)

    def count_forest_trees(self) -> int:
        return sum(1 for t in self._trees if isinstance(t, ForestTree))

    def count_fruit_trees(self) -> int:
        return sum(1 for t in self._trees if isinstance(t, FruitTree))

    def print_sorted(self):
        sorted_trees = sorted(self._trees, key=lambda t: (t.name.lower(), -t.age))
        print("Деревья (Отсортированы: Название, Возраст)")
        for tree in sorted_trees:
            print(tree)

    def load_from_file(self, filename: str):
        self._trees.clear()
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                parts = [p.strip() for p in line.split(';')]
                kind = parts[0].upper()

                # Распознаем Enum типа дерева
                type_str = parts[3].upper()
                if type_str in ("ЛИСТВЕННОЕ", "DECIDUOUS"):
                    t_type = TreeType.DECIDUOUS
                elif type_str in ("ХВОЙНОЕ", "CONIFEROUS"):
                    t_type = TreeType.CONIFEROUS
                else:
                    raise ValueError(f"Строка {line_num}: Неизвестный тип дерева '{parts[3]}'")

                name = parts[1]
                age = int(parts[2])

                if kind == "FOREST":
                    wood_vol = float(parts[4])
                    self.add_tree(ForestTree(name, age, t_type, wood_vol))

                elif kind == "FRUIT":
                    yield_mass = float(parts[4])
                    shelf_life = int(parts[5])
                    self.add_tree(FruitTree(name, age, t_type, yield_mass, shelf_life))