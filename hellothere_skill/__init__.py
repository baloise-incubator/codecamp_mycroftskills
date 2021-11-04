import random

from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number, match_one, extract_datetime
from mycroft.skills.audioservice import AudioService


class HelloThereSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.audio_service = AudioService(self.bus)

    soundsDict = {
        'musik': {
            'https://www.thesoundarchive.com/starwars/star-wars-theme-song.mp3',
            'https://www.thesoundarchive.com/starwars/star-wars-cantina-song.mp3'
        },
        'force': {
            'https://www.thesoundarchive.com/starwars/disturbence.mp3',
            'https://www.thesoundarchive.com/starwars/force.mp3',
            'https://www.thesoundarchive.com/starwars/forcestrong.mp3'
        }
    }

    @intent_file_handler('hello_there.intent')
    def handle_hello_there(self, message):
        self.speak_dialog('hello_there', wait='True')
        result = self.get_response('request')
        soundList, confidence = match_one(result, self.soundsDict)
        elementcount = len(soundList)
        elementToUse = random.randint(0, elementcount -1)
        self.audio_service.play(soundList[elementToUse])


def create_skill():
    return HelloThereSkill()
