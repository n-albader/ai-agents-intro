# Topic: Python Decorators

## Simple Explanation
A decorator in Python is a special type of function that can modify the behavior of another function. Think of it as a way to "wrap" a function with additional features, such as logging, access control, or modification of outputs. Decorators allow you to add functionality to existing code in a clean and readable way.

## Key Concepts
1. **Function as First-Class Object**: In Python, functions can be passed around as arguments, returned from other functions, and assigned to variables.
   
2. **Higher-Order Functions**: A decorator is a higher-order function, meaning it takes another function as an argument and returns a new function.
   
3. **@ Symbol**: The `@decorator_name` syntax conveniently applies a decorator to a function without explicitly having to call it.

4. **Nesting Functions**: Inside a decorator, you can define an inner function that wraps the original function, allowing modifications before or after its execution.

## Example
Here’s a simple example of a decorator that logs the execution of a function:

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

## Common Mistakes
1. **Forgetting to use the `@` symbol**: If you forget the `@decorator` line, the function won’t be decorated and will behave normally.
   
2. **Not returning the inner function**: Always return the inner function from the decorator to ensure modified behavior is preserved.
   
3. **Using the wrong number of arguments**: If the original function takes arguments, make sure the inner function in the decorator can accept those arguments, often using `*args` and `**kwargs`.

## Review Comments
- Decorators can help keep your code organized and reusable.
- They are widely used in frameworks like Flask and Django for adding functionality to route handlers.
- Always remember to test your decorated functions to ensure the desired behavior is achieved.

## Final Summary
Python decorators are a powerful feature that allows you to wrap a function with additional behavior. By learning how to create and use them, you can enhance the functionality of your code effectively. Just remember to handle functions and their arguments carefully, and utilize the `@` symbol to apply decorators smoothly.

## Practice Exercise
Create a decorator that adds the functionality of timing a function execution. The decorator should print how long the function took to run.

1. Write a decorator named `time_decorator`.
2. Inside this decorator, use the `time` module to measure the time before and after the function call.
3. The decorator should return the original function's result after printing the time taken.

## Expected Input
Not applicable.

## Expected Output
When you apply `@time_decorator` to a sample function (e.g., a function that sleeps for a few seconds), it should print the time taken in seconds to execute that function, similar to this:

```
Function took X seconds to complete.
```

## Hints
1. Use `time.time()` to get the current time before and after the function execution.
2. Don't forget to return the result of the original function in your inner wrapper function.