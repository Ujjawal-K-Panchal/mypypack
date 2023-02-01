import math #unused dependency.

def sayHi():
    return "Hi!"


def sayHello():
    return "Hello!"


def sayHiTo(name: str = ""):
    if name == "":
        return sayHi()
    return f"Hi {name}!"


def sayHelloTo(name: str = ""):
    if name == "":
        return sayHello()
    return f"Hello {name}!"
