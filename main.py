def count_larger_than_previous(numbers):
    counter = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            counter += 1

    return counter

def main():

    input_str = input()
    numbers = list(map(int, input_str.split()))

    result = count_larger_than_previous(numbers)

    print(result)

if __name__ == "__main__":
    main()




