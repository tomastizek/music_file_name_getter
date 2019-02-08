import mutagen
import os
import pathlib
from tqdm import tqdm
import argparse


def parse_args():
    """
        Parse and return arguments.
    """
    arg_parser = argparse.ArgumentParser(prog="music_file_name_getter")
    arg_parser.add_argument("--folder", help="source path")

    return arg_parser.parse_args()


def rename_files(source):

    list_of_files = [file for file in os.listdir(source) if os.path.isfile(os.path.join(source, file))]

    for f in tqdm(list_of_files):
        type = pathlib.Path("{}/{}".format(source, f)).suffix
        metadata = mutagen.File("{}/{}".format(source, f))
        if metadata is not None:

            dest_dir = "{}".format(str(metadata["artist"])
                                   .replace("[", "").replace("]", "").replace("'", ""))

            if not os.path.isdir("{}/{}".format(source, dest_dir)):
                os.mkdir("{}/{}".format(source, dest_dir))
            else:
                new_name = "{} - {}" .format(str(metadata["artist"])
                                             .replace("[", "")
                                             .replace("]", "")
                                             .replace("'", ""),
                                  str(metadata["title"])
                                             .replace("[", "")
                                             .replace("]", "")
                                             .replace("'", ""))

                os.rename("{}/{}".format(source, f), "{}/{}/{}{}".format(source, dest_dir,
                                                                     new_name, type))
        else:
            print("meta are not avalaible for this file")
            continue


def main():

    args = parse_args()

    rename_files(args.folder)


if __name__ == "__main__":
    main()