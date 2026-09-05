def greet(input: str) -> str:
# -> str means that the function will return a string
# if you were to write -> int, it would mean that the function will return an integer
    if "Hello" in input:
        return "Hello there!"
    if "Hi" in input:
        return "Hi there!"
    else:
        return "idk what you said"

# this is what the function does, it makes sure that the greetings contain either "Hello" or "Hi"
# if it doesn't contain either of those, it will return "idk what you said"



greeting = greet("How's the weather?")
print(greeting)
