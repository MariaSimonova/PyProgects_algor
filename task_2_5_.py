def ascii_tab(a, b, n):
    my_list = list(range(a, b))
    h = list(map(lambda x: f'{x} - {chr(x)}', my_list))
    i = " ".join(h)
    print(i)

    if n >= 9:
        print(" ".join(list(map(lambda x: f'{x} - {chr(x)}', [122, 123, 124, 125, 126, 127]))))
    else:
        ascii_tab(a + 10, b + 10, n + 1)


ascii_tab(32, 42, 1)
