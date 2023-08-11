def say_something(number: int, word: str) -> str:
    word = word.capitalize()
    return word * number


def some_function(number: int | float) -> None:
    pass


def another_some_function(number: int | float | complex = 0) -> None:
    pass


def get_tuple(lst: list[float | bool]) -> tuple[int]:
    return tuple(int(num) for num in lst)


def do_something(arg: dict[int, str | bool]) -> None:
    pass


hi = say_something(2, 'hi')
print(hi)

lst = [3.099, True]


if __name__ == "__main__":
    print(say_something(2, 'hi'))

    print(get_tuple(lst))
