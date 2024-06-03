from Linker import Linker, FileResource


Resources = {"Hashes": FileResource(r"data/hashes.py"),
             "Indices": FileResource(r"data/indices.py")}
ScriptFixFile = r"../../Fix-Raiden-Boss 2.0 (for all user )/src/FixRaidenBoss2/FixRaidenBoss2.py"


def main():
    linker = Linker(Resources)
    linker.link(ScriptFixFile)


if __name__ == "__main__":
    main()