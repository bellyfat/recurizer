import openai
import os

from summarize import summarize_file

IGNORE_DIRS = ["__pycache__", ".git", ".venv", "venv", "node_modules"]
IGNORE_FILES = [".summary.md"]

def crawl(path: str, overwrite: bool = True):

    #file - check if its in ignore list
    #     - check if its executable, ignore if so
    #     - otherwise, summarize the file
    if os.path.isfile(path):
        if os.access(path, os.X_OK):
            return #ignore executable files
    
        root = os.path.dirname(path)
        fname = os.path.basename(path)
        summarize_file(root, fname, debug=True)

    #directory - check if its in ignore list
    #          - check if it already contains a .summary.md file, ignore if overwrite is false
    #          - otherwise, crawl the directory
    elif os.path.isdir(path):
        if os.path.basename(path) in IGNORE_DIRS:
            return
        
        if ".summary.md" in os.listdir(path) and not overwrite:
            print(f"Skipping {path} because it already contains a .summary.md file")
            return
        
        for subpath in os.listdir(path):
            crawl(os.path.join(path, subpath))

    #symlinks are ignored
    elif os.path.islink(path):
        return
    else:
        print(f"Could not resolve file: {path}")

        
        
def main():
    #walk the dir
    crawl('src', overwrite=False)


if __name__ == '__main__':
    main()