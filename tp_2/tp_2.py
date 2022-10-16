def main_wrapper():
    file = input("Введите название файла: ")
    if __name__ == '__main__':
        main(file)


def main(file):
    filename = file
    try:
        num_list = get_num_base(filename)
    except(FileNotFoundError):
        print("Файл с таким именем не найден")
        exit()
    if _max(num_list) == '':
        print("Введите название не пустого файла")
        return ''
    print(f"Самое маленькое число: {_min(num_list)}\n"
          f"Самое большое число: {_max(num_list)}\n"
          f"Сумма всех чисел: {_sum(num_list)}\n"
          f"Произведение всех чисел: {_mult(num_list)}"
          )


def get_num_base(filename):
    with open(filename, "r") as file:
        num_list = [int(g) for g in file.readline().split()]
    return num_list


def _min(num_list):
    minimum = num_list[0]
    for now_num in num_list[1:]:
        if now_num < minimum:
            minimum = now_num
    return minimum


def _max(num_list):
    try:
        maximum = num_list[0]
        for now_num in num_list[1:]:
            if now_num > maximum:
                maximum = now_num
        return maximum
    except(IndexError):
        return ""



def _sum(num_list):
    amount = num_list[0]
    for now_num in num_list[1:]:
        amount += now_num
    return amount


def _mult(num_list):
    multiply = num_list[0]
    for now_num in num_list[1:]:
        multiply *= now_num
    return multiply


if __name__ == '__main__':
    main_wrapper()