print("hello world")
def main():
    with open("/root/workspace/github.com/itshigo/bookbot/book/frankenstein.txt", "r") as f:
        file_contents = f.read()
    print(file_contents)

if __name__ == "__main__":
    main()
