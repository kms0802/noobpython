class Logger:
    def log(self):
        print("기록 시작")

class FireLogger(Logger):
    def log(self):
        super().log()
        print("파일에 기록")

fire = FireLogger()
fire.log()