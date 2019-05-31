import pyperclip


def get_text_from_file():
    f = open("sql.txt", "r")
    sql = f.readlines()
    return sql


def write_output(result):
    print(result + "\n")
    output = open("output.txt", "w+")
    output.write(result)
    output.close()
