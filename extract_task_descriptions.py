import argparse
import glob
import os
from os import path
from pathlib import Path
from shutil import rmtree


def extract_description_from(file_path: str) -> str:
    with open(file_path) as f:
        file_text = f.read()
        split_text = file_text.split('"""')
        if len(split_text) < 2:
            print(f"{file_path} has no comment at the beginning")
        return '"""' + file_text.split('"""')[1] + '"""'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='ExtractTaskDescription',
        description='This programm extracts the task descriptions of all the problems'
                    ' and exports them with the same structure in a folder next to the original one.')
    parser.add_argument("problem_folder")
    parser.add_argument('-r', '--remove', action='store_true')
    args = parser.parse_args()
    problem_folder = Path(args.problem_folder)

    descriptions_folder = problem_folder.parent / "descriptions"
    if args.remove:
        rmtree(descriptions_folder)
    if descriptions_folder.is_dir():
        print(f"{descriptions_folder} already exists. \n Start program with -r to remove the folder first")

    for file in glob.glob(path.join(args.problem_folder, "**"), recursive=True, ):
        if path.isfile(file):
            rel_problem_path = Path(path.relpath(file, args.problem_folder))
            description_file_path = descriptions_folder / rel_problem_path
            description = extract_description_from(file)
            description_file_path.parent.mkdir(exist_ok=True, parents=True)
            with open(description_file_path, "w") as new_file:
                new_file.write(description)

