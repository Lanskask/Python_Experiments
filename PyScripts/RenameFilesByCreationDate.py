# RenameFilesByCreationDate

from sys import argv as sys_argv
from os import rename as os_rename, chdir as os_chdir, listdir as os_listdir
from os.path import join as path_join, isfile as path_isfile, getmtime as path_getmtime

from typing import List


class RenameFilesByCreationDate(object):
    @staticmethod
    def main(command: str, search_dir: str):
        full_path_init_files = RenameFilesByCreationDate.get_files_in_dir(search_dir)

        if command == "rename":
            RenameFilesByCreationDate.rename_files_array(full_path_init_files)
        elif command == "rename_back":
            RenameFilesByCreationDate.cut_back_files_array(full_path_init_files)
        else:
            print("""
                First parameter - commands:
                    "rename" - for rename
                    "rename_back" - for rename back
                Second parameter - folder where you want to rename files ordered by creation date
            """)

    @staticmethod
    def get_files_in_dir(init_dir):
        os_chdir(init_dir)
        init_files = filter(path_isfile, os_listdir(init_dir))  # get init files
        return sorted([path_join(init_dir, f) for f in init_files],
                      key=lambda x: path_getmtime(x))  # add path to each file

    # rename with numbers
    @staticmethod
    def rename_files_array(full_path_init_files):
        for idx, init_file_path in enumerate(full_path_init_files):
            # print(init_file_path, get_renamed_path_to_with_numbers(init_file_path, idx))
            os_rename(init_file_path,
                      RenameFilesByCreationDate.get_renamed_path_to_with_numbers(init_file_path, idx))

    @staticmethod
    def get_renamed_path_to_with_numbers(init_full_path: str, i: int) -> str:
        return "/".join(init_full_path.split("/")[:-1]) \
               + "/" \
               + '{:02d}'.format(i) \
               + " " \
               + init_full_path.split("/")[-1]

    # cut back
    @staticmethod
    def cut_back_files_array(files_array: List[str]):
        for init_file_path in files_array:
            print(init_file_path + "\n\t" + RenameFilesByCreationDate.get_cutted_path(init_file_path))
            os_rename(init_file_path,
                      RenameFilesByCreationDate.get_cutted_path(init_file_path))

    @staticmethod
    def get_cutted_path(file_path: str) -> str:
        return "/".join(file_path.split("/")[:-1]) + "/" + file_path.split("/")[-1].split(" ", 1)[-1]


if __name__ == "__main__":
    this_search_dir = sys_argv[2]
    RenameFilesByCreationDate.main(command, this_search_dir)
