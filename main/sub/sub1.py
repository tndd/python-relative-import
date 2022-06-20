from main.utils.greet import greet


def greet_sub1():
    greet('sub1')


if __name__ == '__main__':
    greet('sub1 direct')
    # python3 -m main.sub.sub1
