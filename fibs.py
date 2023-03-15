from simple import Hello
from zero import zzero


def fibonacci(n: int) -> int:
    if n == 0:
        zzero()
    elif n == 1:
        x = Hello()
        x.one()
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(0))
print(fibonacci(4))
# print(fibonacci(30))
