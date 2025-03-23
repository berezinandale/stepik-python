def josephus(n, k):
    last_person = 0  # Начальное значение для круга из 1 человека
    for i in range(2, n + 1):
        last_person = (last_person + k) % i
    return last_person + 1  # Приводим к 1-индексации

def main():
    # Ввод данных
    n = int(input())
    k = int(input())

    # Вычисление номера последнего оставшегося человека
    last_person = josephus(n, k)

    # Вывод результата
    print(last_person)

if __name__ == "__main__":
    main()
