#!/usr/bin/env python3

from os import walk, makedirs
from shutil import copy


def main() -> None:
    # path containing all aar/jar files, must end with a forward slash (/)
    PATH_INPUT = ""

    # output path, must end with a forward slash (/)
    PATH_OUT = ""

    for (dirpath, dirnames, filenames) in walk(PATH_INPUT):
        for file in filenames:
            name, version = file[:-4].split("_")
            out = PATH_OUT + name + "/" + version + "/"
            makedirs(out, exist_ok=True)
            copy(PATH_INPUT + file, out)
            write_to_file(out + "library.xml", name, version)


def write_to_file(fileName: str, libName: str, version: str) -> None:
    with open(fileName, "w") as desc:
        desc.write('<?xml version="1.0"?>\n')
        desc.write("<library>\n")
        desc.write("    <!-- library name -->\n")
        desc.write("    <name>{}</name>\n".format(libName))
        desc.write("\n")
        desc.write(
            "    <!-- Advertising, Analytics, Android, SocialMedia, Cloud, Utilities -->\n"
        )
        desc.write("    <category>{}</category>\n".format("Android"))
        desc.write("\n")
        desc.write("    <!-- optional: version string -->\n")
        desc.write("    <version>{}</version>\n".format(version))
        desc.write("\n")
        desc.write(
            "    <!-- optional: date (format: dd.MM.yyyy  example: 21.05.2017) -->\n"
        )
        desc.write("    <releasedate>{}</releasedate>\n".format(""))
        desc.write("\n")
        desc.write("    <!-- optional: comment -->\n")
        desc.write("    <comment>{}</comment>\n".format(""))
        desc.write("</library>\n")


if __name__ == "__main__":
    main()
