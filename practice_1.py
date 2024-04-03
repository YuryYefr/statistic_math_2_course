from collections import Counter
from statistics import mode, median, variance, stdev
import matplotlib.pyplot as plt

# 1. Побудувати таблицю частот та сукупних частот для переглянутих фільмів.
# Визначити фільм, який був переглянутий частіше за інші.

# Припустимо, що у вас є вибірка фільмів
views = input("Введіть ім'я файлу з числами: ")


def read_file(file_name):
    try:
        # Зчитування даних з файлу
        with open(file_name, 'r') as file:
            res = [round(float(line.strip())) for line in file]   # no floats for movie counts
            return res

    except Exception as e:  # так, broad exception у всій красі
        print(f"Виникла помилка: {e}")


data_sample = read_file(views)
# Побудова таблиці частот
frequency_table = Counter(data_sample)

# Сукупні частоти
cumulative_frequency = 0
cumulative_frequencies = {}
for value, frequency in sorted(frequency_table.items()):
    cumulative_frequency += frequency
    cumulative_frequencies[value] = cumulative_frequency

print("Таблиця частот:")
for value, frequency in frequency_table.items():
    print(f"Фільм {value}: {frequency} разів")

print("\nСукупні частоти:")
for value, cumulative_frequency in cumulative_frequencies.items():
    print(f"Фільм {value}: {cumulative_frequency}")
# 2. Знайти Моду та Медіану заданої вибірки.

# Знайти моду
mode_value = mode(data_sample)
print(f"Мода: {mode_value}")

# Знайти медіану
median_value = median(data_sample)
print(f"Медіана: {median_value}")
# 3. Порахувати Дисперсію та Середнє квадратичне відхилення розподілу.


# Знайти дисперсію
variance_value = variance(data_sample)
print(f"Дисперсія: {variance_value}")

# Знайти середнє квадратичне відхилення
stdev_value = stdev(data_sample)
print(f"Середнє квадратичне відхилення: {stdev_value}")
# 4. Побудувати гістограму частот для даного розподілу.


# Побудова гістограми
plt.hist(views, bins=max(data_sample) - min(data_sample) + 1, edgecolor='black', alpha=0.7)
plt.title('Гістограма частот')
plt.xlabel('Кількість переглядів')
plt.ylabel('Частота')
plt.show()

# 5. Запис результатів у файл
with open("output_data.txt", 'w') as output_file:
    output_file.write("Таблиця частот:\n")
    for value, frequency in frequency_table.items():
        output_file.write(f"Фільм {value}: {frequency} разів\n")

    output_file.write("\nСукупні частоти:\n")
    for value, cumulative_frequency in cumulative_frequencies.items():
        output_file.write(f"Фільм {value}: {cumulative_frequency}\n")

    output_file.write(f"\nМода: {mode_value}\n")
    output_file.write(f"Медіана: {median_value}\n")
    output_file.write(f"Дисперсія: {variance_value}\n")
    output_file.write(f"Середнє квадратичне відхилення: {stdev_value}\n")

print("Результати записані у файл output_data.txt.")