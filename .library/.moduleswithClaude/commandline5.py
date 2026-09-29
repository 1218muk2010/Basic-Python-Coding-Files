import sys

# argv[0] = "greet.py", argv[1] = first name you type
if len(sys.argv) < 2:
    sys.exit("Usage: python greet.py <your name>")

names = sys.argv[1:]  # slice off the filename, keep everything else
for name in names:
    print(f"What's good, {name}!")
