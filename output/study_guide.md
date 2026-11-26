# Python Decorators

## 1. Explanation
A decorator in Python is a special function that can modify or enhance another function. You can think of it as a wrapper that adds extra functionality to an existing function without changing its code.

## 2. Key Concepts
- **Functions as First-Class Citizens**: In Python, functions can be passed around as arguments, returned from other functions, or assigned to variables. This is important for decorators because they take functions as input.
  
- **Nested Functions**: A decorator often uses a nested function (a function defined inside another function) to create the wrapper that adds new behavior to the original function.

- **@ Syntax**: Decorators are commonly applied to functions using the "@" symbol followed by the decorator name above the function definition. This is a shorthand way to use decorators.

## 3. Simple Example
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### Explanation of the Code
1. **my_decorator**: This is the decorator function. It takes a function `func` as an argument and defines a nested function called `wrapper`.
2. **wrapper**: This function is where we add extra behavior. It prints a message before and after calling the original function `func()`.
3. **@my_decorator**: This line applies the `my_decorator` to the `say_hello` function.
4. **say_hello**: This is the original function that prints "Hello!".
5. **say_hello()**: When we call `say_hello()`, it actually runs the `wrapper()` function, which adds the extra printing before and after the hello message.

When you run the code, the output will show messages before and after "Hello!", demonstrating how the decorator works.