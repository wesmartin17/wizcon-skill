from mycroft import MycroftSkill, intent_file_handler


class Wizcon(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wizcon.intent')
    def handle_wizcon(self, message):
        self.speak_dialog('wizcon')


def create_skill():
    return Wizcon()

