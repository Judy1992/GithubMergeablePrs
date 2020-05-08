from dingtalkchatbot.chatbot import DingtalkChatbot

class DingdingBot:

    @property
    def xiaoding(self):
        return self._xiaoding

    def __init__(self, webhook):
        self._xiaoding = DingtalkChatbot(webhook)

    def sendMsg(self, msg, atPerson):
        """
        :param msg: string
        :param atPerson: List of String, people's mobile phone number
        """
        self._xiaoding.send_text(msg= msg, is_at_all=False, at_mobiles=list(atPerson))