import os
import sys


def mkproject(lang, name):

    relative_path = os.path.dirname(__file__)
    gitignore_path = relative_path + "/templates/" + lang + ".gitignore"

    try:
        gitignore_template = open(gitignore_path, "r")
        gitignore_txt = gitignore_template.read()
        gitignore_template.close()

        if os.path.exists("./" + name):
            raise NameError(
                name + " is already a directory. Try choosing another name.")

        os.makedirs(name)

        cd_path = "cd ./" + name + " && "
        project_path = "./" + name +"/"
        os.system(cd_path + "git init")
        os.system(cd_path + "touch .gitignore")

        gitignore = open(project_path + ".gitignore", "w")
        gitignore.write(gitignore_txt)
        gitignore.close()

    except FileNotFoundError:
        raise FileNotFoundError(
            lang + ".gitignore file not found, consider adding " + os.path.abspath(gitignore_path))


if __name__ == "__main__":
    args = sys.argv
    mkproject(args[1], args[2])
