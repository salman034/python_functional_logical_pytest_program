def squar_root(n, l):
    x = n
    count = 0
    while 1:
        count += 1
        root = 0.5 * (x + (n / x))
        if abs(root - x) < l:
            break
        x = root
    return root


def test_square_root():
    result = squar_root(5, 6)
    assert result == 3
    print(result)
