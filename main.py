def say_something(number: int, word: str) -> str:
    word = word.capitalize()
    return word * number


hi = say_something(2, 'hi')
print(hi)


if __name__ == "__main__":
    print(say_something(2, 'hi'))