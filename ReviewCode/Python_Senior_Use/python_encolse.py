def curve_pre():
    a = 1
    b = 2
    c = 3

    def curve(x):
        return a * x * x + b * x + c

    return curve


def run():
    origin = 0

    def go(step):
        nonlocal origin
        new_pos = origin + step
        origin = new_pos
        return new_pos

    return go


if __name__ == '__main__':
    fun = curve_pre()
    print(fun(1))
    origin = run()
    step1 = origin(2)
    step2 = origin(3)
