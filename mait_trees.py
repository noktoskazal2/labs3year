from trees import TreeContainer, TreeType

if __name__ == "__main__":
    container = TreeContainer()

    container.load_from_file("trees.txt")

    print("ИСХОДНЫЙ СПИСОК ДЕРЕВЬЕВ В КОНТЕЙНЕРЕ")
    container.print_all()

    print("Статистика")
    print(f"Лиственных деревьев: {container.count_by_tree_type(TreeType.DECIDUOUS)}")
    print(f"Хвойных деревьев:    {container.count_by_tree_type(TreeType.CONIFEROUS)}")
    print(f"Лесных деревьев:     {container.count_forest_trees()}")
    print(f"Плодовых деревьев:    {container.count_fruit_trees()}")
    container.print_sorted()