import openai
import os

from summarize import summarize_file

DEST_FILE = ".summary.md"
IGNORE_DIRS = ["__pycache__", ".git", ".venv", "venv", "node_modules"]
IGNORE_FILES = ["README.md", ".gitignore"]


def crawl(path: str, overwrite: bool = True):
   
    #file - check if its in ignore list
    #     - check if its executable, ignore if so
    #     - also ignore if we dont want to overwrite, or in ignore list
    #     - otherwise, summarize the file
    if os.path.isfile(path):
        if os.access(path, os.X_OK): 
            return
        
        root = os.path.dirname(path)
        fname = os.path.basename(path)
        if fname == DEST_FILE and not overwrite:
            return
        
        if fname in IGNORE_FILES:
            return

        print("Generating summary for: ", path)
        summarize_file(root, fname, debug=False)

    #directory - check if its in ignore list
    #          - check if it already contains a .summary.md file, ignore if overwrite is false
    #          - otherwise, crawl the directory
    elif os.path.isdir(path):
        if os.path.basename(path) in IGNORE_DIRS:
            print(f"Skipping {path} because it is in the ignore list")
            return
        
        if DEST_FILE in os.listdir(path) and not overwrite:
            print(f"Skipping {path} because {DEST_FILE} already exists")
            return
        
        for subpath in os.listdir(path):
            crawl(os.path.join(path, subpath), overwrite=overwrite)
    
    elif os.path.islink(path):
        return
    else:
        print(f"Unknown file type: {path}")
        return
        
def main():
    #walk the dir
    crawl('.', overwrite=True)


if __name__ == '__main__':
    main()