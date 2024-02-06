import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.


def f(arg):
    return 5 * arg ** 2 + 3 * arg + 1


def monte_carlo(func: callable(float), a: float, b: float, n: int) -> float:
    x = np.random.uniform(a, b, n)

    y = np.random.uniform(0, func(b), n)

    count = np.sum(y <= func(x))

    area = (b - a) * max(func(b), func(a))

    return area * count / n


if __name__ == "__main__":
    a = 0  # Нижня межа
    b = 2  # Верхня межа

    result, error = spi.quad(f, a, b)

    print("Інтеграл: ", result)

    area = monte_carlo(f, a, b, 10_000_000)

    print("Площа під графіком: ", area)

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')

    ax.set_title('Графік інтегрування f(x) = 5x^2 + 3x + 1 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()
