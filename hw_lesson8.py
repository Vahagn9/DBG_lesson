def sum_of_2(sum_a, sum_b):
    """returns sum of 2 as string"""
    return str(sum_a + sum_b)


def mul_of_2(mul_a, mul_b):
    """multiplies 2 numbers and returns as string"""
    return str(mul_a * mul_b)


def a_pow_b(pow_a, pow_b):
    """returns a ** b as string"""
    return str(pow_a ** pow_b)


def try_open_file(def_name=""):
    """a module for safely opening a file, from the terminal"""
    fl = def_name != ""
    while True:
        f = def_name if fl else input("please input file name: ")
        print("Trying to open a file \"" + f + "\" for reading . . .")
        try:
            r = open(f, "r")
        except IOError:
            print("imputed wrong file name.\n Please try again ")
            fl = False
        else:
            print("The file \"" + f + "\" is successfully opened for reading\n")
            break
    return r


def get_a_b(file_name):
    """getting a and b from file"""
    next_a = file_name.readline()
    next_b = file_name.readline()
    try:
        return int(next_a), int(next_b)
    except ValueError:
        return None, None


def write_to_file(war_1, war_2, pair_num, write_file_name):
    """Writes the results to write_file_name."""
    write_file_name.write("Results for " + str(pair_num) + "-th pair:\n")
    write_file_name.write("a = " + str(war_1) + ", b = " + str(war_2) + "\n")
    write_file_name.write("a + b = " + sum_of_2(war_1, war_2) + "\n")
    write_file_name.write("a * b = " + mul_of_2(war_1, war_2) + "\n")
    write_file_name.write("a ** b = " + a_pow_b(war_1, war_2) + "\n\n")


# === main ===
print("Start\n")
# read_file = try_open_file() # use this instead of next line to input file name manually
read_file = try_open_file("in_hw8.txt")
write_file = open("results.txt", "w")
print("Created and opened a file \"results.txt\" for writing.\n")
n = 1
while True:
    a, b = get_a_b(read_file)
    if not a or not b:
        print("End of file reached or next line is not a number.")
        break
    print("Working on ", n, "-th pair ...", sep="")
    write_to_file(a, b, n, write_file)
    n += 1
print("\nClosing opened files . . .")
write_file.close()
read_file.close()
print("\nSuccessfully finished !!!\nResults are available in \"results.txt\"")
