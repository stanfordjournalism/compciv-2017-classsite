


.. code-block:: python

    x = input("Enter one number: ")
    y = input("Enter another number: ")
    z = x + y
    print("Answer is:", z)



... code-block:: python


    def foo(x, y):
        return x + y

    x = input("Enter one number: ")
    y = input("Enter another number: ")
    z = foo(x, y)
    print("Answer is: ", z)



    from sys import argv

    def foo(x, y):
        return x + y

    x = argv[1]
    y = argv[2]

    z = foo(x, y)
    print("Answer is: z)

