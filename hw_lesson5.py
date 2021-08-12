# made by Vahagn Vardanyan
def count_words_from_file(file_name: str, output_name: str = "statistics.txt"):
    """
    Calculate number of "the", "if" words and the number of "e" letter in the given text
    Create a statistics.txt file in which we can see the statistics of "the if" and "e"
    Do not use With open formation

    """
    print("reading a file: \"" + file_name + "\" . . .")
    read_file = open(file_name, "r", encoding="utf-8-sig")
    print("start counting . . .")
    count_the = count_if = count_e = 0
    for line in read_file:
        for char in line:
            if char == "e":
                count_e += 1
        word_list = line.split()
        for word in word_list:
            if word == "the" or word == "The":
                count_the += 1
            elif word == "if" or word == "If":
                count_if += 1
    print("Counting successfully completed\nClosing the file: \"" + file_name + "\"")
    read_file.close()
    print("Writing the results to the file: \"" + output_name + "\" . . .")
    write_file = open(output_name, "w")
    write_file.write("Found \"e\" in the \"" + file_name + "\" : " + str(count_e))
    write_file.write("\nFound \"the\" in the \"" + file_name + "\" : " + str(count_the))
    write_file.write("\nFound \"if\" in the \"" + file_name + "\" : " + str(count_if))
    write_file.close()
    print("Writing successfully completed ")


# === main ===
f_name = "how to turn dirt into gold.txt"
# f_name = input("please input the text file name: ")
count_words_from_file(f_name)
