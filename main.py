# Problema 6
def get_longest_div_k(lst, k):
    """
    Determina numere divizibile cu k dintr-o lista
    :param lst: lista de nr. intrego
    :param k: numar intreg
    :return: o lista continand toate elementele divizibile cu k din lst
    """
    rezultat = []
    for x in lst:
        if x % k == 0:
            rezultat.append(x)
    return rezultat


def test_get_longest_div_k():
    assert get_longest_div_k([18, 6, 25, 17, 32], 6) == [18, 6]
    assert get_longest_div_k([12, 85, 77, 15], 5) == [85, 15]
    assert get_longest_div_k([11, 77, 111, 89, 78, 121], 11) == [11, 77, 121]


# problema 18
def is_desc(x):
    """
    Determina daca cifrele unui numar se afala in ordine decrecatoare
    :param x: numar intreg
    :return: True, daca cifrele se alfa in ordine descrescatoare, False in caz contrar
    """
    while x > 9:
        if x % 10 > x // 10 % 10:
            return False
        x = x // 10
    return True


def get_longest_digit_count_desc(lst):
    """
    Deterina numerele care au cifrele in ordine descrescatoare
    :param lst: lista de nr. intregi
    :return: o lista continand toate numerele ce au cifrele in ordine descrecatoare
    """
    rezultat = []
    for i in lst:
        if is_desc(i):
            rezultat.append(i)
    return rezultat


def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([]) == []
    assert get_longest_digit_count_desc([121, 78, 98, 47, 51]) == [98, 51]
    assert get_longest_digit_count_desc([89, 754, 120, 65, 91, 857, 6310]) == [754, 65, 91, 6310]


# problema 7
def is_prime(x):
    """"
    Determina daca un numar este prim
    :param x: numar intreg
    :return: True daca numarul este prim, False in caz contrar
    """
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def get_longest_all_not_prime(lst):
    """
    Determina numerele care nu sunt prime
    :param lst: lista de numere intregi
    :return: lista care contine toate numerele neprime
    """
    rezultat = []
    for i in lst:
        if not is_prime(i):
            rezultat.append(i)
    return rezultat


def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([]) == []
    assert get_longest_all_not_prime([13, 25, 17, 81, 19, 32]) == [25, 81, 32]
    assert get_longest_all_not_prime([25, 82, 64, 26, 121, 1]) == [25, 82, 64, 26, 121, 1]
    assert get_longest_all_not_prime([17, 13]) == []


def print_menu():
    print("1.Citire lista")
    print("2.Afisare numere divizibile cu k")
    print("3.Afisare numere care au cifrele in ordine descrescatoare")
    print("4.Afisare numere neprime")
    print("5.Iesire")


def citire_lista():
    lst = []
    n = int(input("Dati numarul de valori din lista "))
    for i in range(n):
        lst.append(int(input("lst[" + str(i) + "]=")))
    return lst


def main():
    test_get_longest_div_k()
    test_get_longest_digit_count_desc()
    test_get_longest_all_not_prime()
    lst = []
    while True:
        print_menu()
        optiune = input("Alegeti optiunea ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            k = int(input("k="))
            print(get_longest_div_k(lst, k))
        elif optiune == "3":
            print(get_longest_digit_count_desc(lst))
        elif optiune == "4":
            print(get_longest_all_not_prime(lst))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita. Reincercati!")


main()
