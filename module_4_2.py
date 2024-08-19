def test_function():

    def inner_function():
        inner_ = "Я в области видимости функции test_function"
        print(inner_)

    inner_function()

test_function()
