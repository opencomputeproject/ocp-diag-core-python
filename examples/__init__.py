import collections.abc as abc

DEMOS = {}


def demo(func) -> abc.Callable[[], None]:
    def w(banner=True) -> None:
        if banner:
            print("-" * 80)
            print(func.__name__)
            print("-" * 80)
        func()
        if banner:
            print()

    DEMOS[func.__name__] = w
    return w
