files = [
    "report.pdf",
    "setup.exe",
    "image.png",
    "virus.exe",
    "note.txt"
]

def filter_keyword(files, keyword):
    for f in files:
        if keyword in f:
            print(f"'{keyword}' 포함됨:", f)

filter_keyword(files, "hack")