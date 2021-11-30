import pysubs2
import os


class Processor:
    def __init__(self):
        extensions_tuple = (".ass", ".txt")
        self.in_folder = os.path.join(os.getcwd(), "in_subs")
        in_files = Processor.list_files(self.in_folder)
        self.in_sub_files = Processor.list_sub_files(in_files, extensions_tuple)

    @staticmethod
    def check_input(value):
        shift_val = float(value)
        return shift_val

    @staticmethod
    def get_input():
        in_val = input("=== Podaj wartosc przesuniecia w sekundach np 2.5 ===\n")
        # print("Konwertuje")
        return in_val

    @staticmethod
    def list_files(in_dir):
        files_list = os.listdir(in_dir)
        return files_list

    @staticmethod
    def list_sub_files(files_list, extensions):
        final_list = []
        for file in files_list:
            if file.endswith(extensions):
                final_list.append(file)

        return final_list

    def get_paths(self, in_file):
        subs_file = os.path.join(self.in_folder, in_file)
        out_file_path = os.path.join(os.getcwd(), "NEW_{}".format(in_file))
        return subs_file, out_file_path

    @staticmethod
    def load_subs(in_file):
        subs = pysubs2.load(in_file, encoding="utf-8")
        return subs

    @staticmethod
    def process_subs(subs, shift_val, out_file):
        subs.shift(s=shift_val)
        subs.save(out_file)


def main():
    try:
        prc = Processor()
        shift_in = prc.get_input()
        shift_val = prc.check_input(shift_in)

        for in_file in prc.in_sub_files:
            in_sub_file, out_file_path = prc.get_paths(in_file)
            subs = prc.load_subs(in_sub_file)
            prc.process_subs(subs, shift_val, out_file_path)

        input("===Koniec. Nacisnij ENTER aby zamknac. ===")

    except Exception:
        # error = traceback.print_exc()
        input("!!! Nie dziala !!!\nNacisnij ENTER aby zamknac")


if __name__ == "__main__":
    main()
