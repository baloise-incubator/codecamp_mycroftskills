from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number, match_one, extract_datetime
from mycroft.skills.audioservice import AudioService


class HelloThereSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.audio_service = AudioService(self.bus)

    location = 'https://www.thesoundarchive.com/play-wav-files.asp?sound=starwars/disturbence.mp3'

    @intent_file_handler('hello_there.intent')
    def handle_hello_there(self, message):
        self.audio_service.play(self.location)
        self.speak('und tschüss')


def create_skill():
    return HelloThereSkill()
