from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print("[이메일] " + message)

class SMSNotifier(Notifier):
    def send(self, message):
        print("[SMS] " + message)

class KakaoNotifier(Notifier):
    def send(self, message):
        print("[카카오톡] " + message)

def send_all(notifiers, msg):
    for notifier in notifiers:
        notifier.send(msg)

notifier_list = [EmailNotifier(), SMSNotifier(), KakaoNotifier()]
send_all(notifier_list, "다형성 Day 5 학습완료")