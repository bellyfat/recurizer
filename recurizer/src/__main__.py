import openai
import os

from summarize import summarize_file

IGNORE_DIRS = ["__pycache__", ".git", ".venv", "venv", "node_modules"]
IGNORE_FILES = [".summary.md"]

def crawl(dir: str):
    for root, dirs, files in os.walk(dir):
        for d in dirs:
            if d in IGNORE_DIRS: continue
            print(d)
            crawl(d)
        for f in files:
            if os.access(
                os.path.join(root, f), 
                os.X_OK
            ): continue
            if f in IGNORE_FILES: continue
            print(f)
            summarize_file(root, f)
        
        
            


def main():
    #walk the dir
    crawl('recurizer/src/')


if __name__ == '__main__':
    main()