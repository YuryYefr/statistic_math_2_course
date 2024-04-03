# 1)За вибіркою з нормальної генеральної сукупності критерієм
# перевірити гіпотезу про нормальний розподіл;
import math
from scipy.stats import chi2, norm, t
import numpy as np
import statsmodels.api as sm

TEXT_FILE = input("Введіть ім'я файлу з числами: ")


def shapir_wilk_test(data):
    n = len(data)
    sorted_data = sorted(data)

    # обчислення коефіцієнтів W та A
    a = [0] * n
    for i in range(n):
        a[i] = (2 * (i + 1) - 1) / (2 * n)

    w = sum([(a[i] * sorted_data[i]) ** 2 for i in range(n)])

    # обчислення статистики тесту
    numerator = (w - n) ** 2
    denominator = sum([(data[i] - sum(data) / n) ** 2 for i in range(n)])

    test_statistic = numerator / denominator

    # виведення результату тесту
    critical_value = 1. * (0.0037 * n + 0.002 * (n ** 2 - 3 * n + 3))  # для рівня значущості 0.05
    print("Test Statistic:", test_statistic)
    print("Critical Value:", critical_value)

    if test_statistic < critical_value:
        print("Гіпотеза про нормальний розподіл не відхиляється")
    else:
        print("Гіпотеза про нормальний розподіл відхиляється")


# Зчитування ім'я файлу введення з користувача
file_name = TEXT_FILE

try:
    # Зчитування даних з файлу
    with open(file_name, 'r') as file:
        data_sample = [float(line.strip()) for line in file]

    # Перевірка гіпотези про нормальний розподіл
    shapir_wilk_test(data_sample)

except Exception as e:  # так, broad exception у всій красі
    print(f"Виникла помилка: {e}")


# 2)Побудувати довірчі інтервали для: математичного сподівання при
# відомій дисперсії;


def confidence_interval_mean_known_variance(data, conf_level):
    n = len(data)
    x_bar = sum(data) / n
    sigma = float(input("Введіть відому дисперсію (σ²): "))  # введіть вручну

    z_critical = abs(norm.ppf((1 - conf_level) / 2))
    margin_of_error = z_critical * (sigma / math.sqrt(n))

    lower_bound = x_bar - margin_of_error
    upper_bound = x_bar + margin_of_error

    return lower_bound, upper_bound


# математичного сподівання при невідомій дисперсії;
def confidence_interval_mean_unknown_variance(data, conf_level):
    n = len(data)
    x_bar = sum(data) / n
    s = float(input("Введіть виправлену вибіркову стандартну відхиленість (s): "))  # введіть вручну

    t_critical = abs(t.ppf((1 - conf_level) / 2, n - 1))
    margin_of_error = t_critical * (s / math.sqrt(n))

    lower_bound = x_bar - margin_of_error
    upper_bound = x_bar + margin_of_error

    return lower_bound, upper_bound


# для дисперсії;
def confidence_interval_variance(data, conf_level):
    n = len(data)
    s_squared = float(input("Введіть виправлену вибіркову дисперсію (s²): "))  # введіть вручну

    chi2_lower = chi2.ppf((1 - conf_level) / 2, n - 1)
    chi2_upper = chi2.ppf(1 - (1 - conf_level) / 2, n - 1)

    lower_bound = (n - 1) * s_squared / chi2_upper
    upper_bound = (n - 1) * s_squared / chi2_lower

    return lower_bound, upper_bound


# Зчитування ім'я файлу введення з користувача
file_name = TEXT_FILE

try:
    # Зчитування даних з файлу
    with open(file_name, 'r') as file:
        data_sample = [float(line.strip()) for line in file]

    # Введення рівня значущості
    confidence_level = float(input("Введіть рівень значущості (від 0 до 1): "))

    # Довірчий інтервал для математичного сподівання при відомій дисперсії
    mean_known_variance_interval = confidence_interval_mean_known_variance(data_sample, confidence_level)
    print(f"Довірчий інтервал для математичного сподівання при відомій дисперсії: {mean_known_variance_interval}")

    # Довірчий інтервал для математичного сподівання при невідомій дисперсії
    mean_unknown_variance_interval = confidence_interval_mean_unknown_variance(data_sample, confidence_level)
    print(f"Довірчий інтервал для математичного сподівання при невідомій дисперсії: {mean_unknown_variance_interval}")

    # Довірчий інтервал для дисперсії
    variance_interval = confidence_interval_variance(data_sample, confidence_level)
    print(f"Довірчий інтервал для дисперсії: {variance_interval}")


except Exception as e:
    print(f"Виникла помилка: {e}")



# 3)Задати структуру та параметри (кожному індивідуально) ідеальної
# багатовимірної лінійної регресії, реалізувати віртуальний активний
# експеримент і за його результатами методом найменших квадратів
# знайти оцінки її коефіцієнтів.

# Задаємо параметри
np.random.seed(0)
beta_0 = 2
beta_1 = 3
beta_2 = 4

# Генеруємо незалежні змінні
X1 = np.random.rand(100)
X2 = np.random.rand(100)

# Генеруємо випадкову помилку
epsilon = np.random.normal(0, 1, 100)

# Задаємо ідеальну багатовимірну лінійну регресійну модель
Y = beta_0 + beta_1 * X1 + beta_2 * X2 + epsilon

# Додаємо константу для оцінки beta_0
X = sm.add_constant(np.column_stack((X1, X2)))

# Використовуємо метод найменших квадратів для оцінки коефіцієнтів
model = sm.OLS(Y, X).fit()

# Виводимо результати оцінки
print(model.summary())
