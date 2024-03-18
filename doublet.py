def swap_character(word: str, where: int, updated: str) -> str:
    word = word[:where] + updated + word[where+1:]
    print(word)
    print("a")
    return word
def main():
    a = swap_character("cat", 3, "r")
    print(a)
    return a