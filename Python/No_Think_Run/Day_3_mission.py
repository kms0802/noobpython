class Notifier:
    def notify(self):
        print("알림")

class SlackNotifier(Notifier):
    def notify(self):
        print("슬랙 메시지 전송!")

class KakaoNotifier(Notifier):
    def notify(self):
        print("카카오톡 메시지 전송!")

notices = [Notifier(), SlackNotifier(), KakaoNotifier()]
for notice in notices:
    notice.notify()