from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    # current_files = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(current_files)
    # print("")

    # pkg_files = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(pkg_files)
    # print("")

    # bin_files = get_files_info("calculator", "/bin")
    # print("Result for '/bin' directory:")
    # print(bin_files)
    # print("")

    # back_files = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(back_files)
    # print("")

    # main_content = get_file_content("calculator", "main.py")
    # print("Result for 'main.py' file:")
    # print(main_content)
    # print("")

    # pkg_content = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for 'pkg/calculator.py' file:")
    # print(pkg_content)
    # print("")

    # bin_content = get_file_content("calculator", "bin/cat")
    # print("Result for 'bin/cat' file:")
    # print(bin_content)
    # print("")

    # doesnt_exist_content = get_file_content("calculator", "pkg/does_not_exist.py")
    # print("Result for 'pkg/does_not_exist.py' file:")
    # print(doesnt_exist_content)
    # print("")

    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print(result)

    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print(result)

    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print(result)

    result = run_python_file("calculator", "main.py")
    print(result)
    
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)


if __name__ == "__main__":
    main()