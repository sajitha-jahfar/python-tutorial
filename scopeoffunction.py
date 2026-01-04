x=10
def outer():
    x=5
    print(x)
    def inner():
        x=2
        print(x)
    inner()
outer()
# print(x)