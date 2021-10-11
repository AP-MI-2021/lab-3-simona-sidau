# Problema 6
def get_longest_div_k(lst: object, k: object) -> object:
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


def print_menu():
    print("1.Citire lista")
    print("2.Afisare numere divizibile cu k")
    print("3.Afisare numere care au cifrele in ordine descrescatoare")
    print("4.Iesire")


def citire_lista():
    lst = []
    n = int(input("Dati numarul de valori din lista "))
    for i in range(n):
        lst.append(int(input("lst[" + str(i) + "]=")))
    return lst


def main():
    test_get_longest_div_k()
    test_get_longest_digit_count_desc()
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
            break
        else:
            print("Optiune gresita. Reincercati!")


main()