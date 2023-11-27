from game_v2 import score_game
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    # Имрорт библиотеки 'numpy' в переменную 'np'
    import numpy as np
    # Объявляем счетчик итераций
    count = 0
    # Объявляем переменную для поиска загаданного числа. Значение - случайное число из диапазона от 0 до 100, тип int
    predict = np.random.randint(1, 101)
    # Задаем диапазон значений загаданного числа от 0 до 100
    min_predict, max_predict = 0, 100
    # Выполняем цикл пока не выччислим загаданное число
    while number != predict:
        # Запускаем счетчик итераций
        count += 1
        # Если 'predict' больше загаданного
        if predict > number:
            # Заменяем верхнюю границу диапазона на 'predict'
            max_predict = predict
            # Присваеваем 'predict' значение середины нового диапазона
            predict = round((min_predict + max_predict)/2)
        # Если 'predict' меньше загаданного
        elif predict < number:
            # Заменяем нижнюю границу диапазона на 'predict'
            min_predict = predict
            # Присваеваем 'predict' значение середины нового диапазона
            predict = round((min_predict + max_predict)/2)
            
    # Ваш код заканчивается здесь

    return count

if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)