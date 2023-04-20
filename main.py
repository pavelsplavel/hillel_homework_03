from pympler import asizeof

FIND_WORD = input("Find word: ")

number_of_lines = 0


def find_in_file(filename, word):

    file = open(filename, "r")

    while True:

        line = file.readline()

        if not line:
            break

        if word in line:
            global number_of_lines
            number_of_lines += 1
            yield line

    file.close()


def write_to_file(words):
    with open("results.txt", "w") as file:
        for word in words:
            file.write(word)


results = find_in_file("rockyou.txt", FIND_WORD)

with open("results.txt", "r") as file_to_read:
    file_size = file_to_read.readlines()

write_to_file(results)

print("Process has finished!")
print(
    f"Result:\nNumber of lines: {number_of_lines}\nThe total size of created file: {asizeof.asizeof(file_size)} bytes."
)
