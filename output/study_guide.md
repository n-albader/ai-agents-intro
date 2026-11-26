# Topic: Python Decorators

## Simple Explanation
In Python, decorators are special functions that can modify or enhance the behavior of other functions or methods. Think of them as wrappers that add something extra to a function without changing its actual code.

## Key Concepts
- **Function:** A block of code that performs a specific task when called.
- **Decorator:** A function that takes another function as an argument and extends or modifies its behavior.
- **@ symbol:** This is used to apply a decorator to a function.
- **Higher-Order Function:** A function that can take another function as an argument or return a function.

## Example
Here's a simple example of a decorator that prints a message before and after a function call:

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

# Call the decorated function
say_hello()
```

### Output:
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

## Practice Exercise
Create a decorator called `repeat`, which takes a function and a number `n` as arguments. The decorator should call the function `n` times. Then, apply the decorator to a simple function that prints "Hi!".

### Example Function:
```python
def print_hi():
    print("Hi!")
```

## Common Mistakes
1. **Forgetting to Return the Wrapper:** Always remember to return the wrapper function inside the decorator.
2. **Using the Wrong Number of Arguments:** If the function you are decorating takes parameters, ensure your wrapper can handle them.
3. **Not Applying the Decorator:** Make sure to use the `@decorator_name` syntax to apply your decorator.

## Review Comments
- Decorators are a great way to enhance your functions.
- They help keep your code clean and reusable.
- Understanding decorators is key to mastering advanced Python topics.

## Final Summary
Python decorators allow you to modify the behavior of functions easily. They act as a wrapper that can add additional functionality without altering the original function’s code. Practice creating your own decorators to get more comfortable with this concept!