DEMOS = {}


def demo(func):
    def w(banner=True):
        if banner:
            print("-" * 80)
            print(func.__name__)
            print("-" * 80)
        func()
        if banner:
            print()

    DEMOS[func.__name__] = w
    return w
