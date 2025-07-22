answer = input(
    "What is the answer to the Great Question of Life, the Universe, and Everything? ")
if answer == "42" or str(answer).lower() in ["forty-two", "forty two"]:
    print("Yes")
else:
    print("No")
