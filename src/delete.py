import os

DEST_FILE = ".summary.md"

def delete(path):
    if os.path.isfile(path):
        root = os.path.dirname(path)
        fname = os.path.basename(path)

        if fname == DEST_FILE:
            os.remove(path)
            print(f"Removed {path}")

    elif os.path.isdir(path):
        for subpath in os.listdir(path):
            delete(os.path.join(path, subpath))


if __name__ == '__main__':
    delete('.')