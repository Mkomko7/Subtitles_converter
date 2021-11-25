import pysubs2, os, traceback

def list_files(in_dir):
    final_list = []
    files_list = os.listdir(in_dir)
    for file in files_list:
        if file.endswith('.ass'):
            final_list.append(file)

    return final_list

def main():
    try:
        shift_val = float(input("=== Podaj wartosc przesuniecia w sekundach np 2.5\n"))
        print("Konwertuje")
        
        in_folder = "in_subs"
        in_sub_files = list_files(os.path.join(os.getcwd(), in_folder))

        for in_file in in_sub_files:

            in_sub_file = os.path.join(os.getcwd(), in_folder, in_file)
            out_file = os.path.join(os.getcwd(), "NEW_{}".format(in_file))
            subs = pysubs2.load(in_sub_file, encoding="utf-8")
            subs.shift(s=shift_val)
            subs.save(out_file)
        input("===Koniec. Nacisnij ENTER aby zamknac. ===")
    except Exception:
        error = traceback.print_exc()
        print("!!! Nie dziala !!!")
        input("Nacisnij ENTER aby zamknac")
    
if __name__ == "__main__":
    main()
