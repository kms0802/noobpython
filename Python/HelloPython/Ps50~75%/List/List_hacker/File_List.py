files = [
    "report.pdf",
    "setup.exe",
    "image.png",
    "virus.exe",
    "note.txt"
]

def filter_exe(files):
    for f in files:
        if f.endswith(".exe"):
            print("실행 파일 발견:", f)

filter_exe(files)