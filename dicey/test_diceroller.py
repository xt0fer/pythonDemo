
import diceroller
def test_do_it_again():
    t = diceroller.do_it_again()
    print(t)


def test_randnum(n):
    for _ in range(n):
        t = diceroller.randnum()
        if not (t >= 1 and t <=6):
            print('FAILED')
            return
    print(f"Tested {n} times. Works!")

if __name__ == '__main__':
    print('testing diceroller')
    print('testing random100')
    test_randnum(100)
    print('testing do_it_again')
    test_do_it_again()