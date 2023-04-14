from ..state_classes.state_class import State
from ..state_classes.menu_class import MenuClass
from ..state_classes.add_flashcard_class import AddFlashcardClass
from ..state_classes.practice_class import PracticeClass
from ..state_classes.write_to_db_state import WriteToDB
from ..state_classes.read_from_db_state import ReadFromDB
from ..state_classes.update_class import UpdateClass
from ..database.db import DBHandler


class ContextClass:

    _state = None
    _state_object = None

    def __init__(self) -> None:
        self._orchestrator = {
            State.MENU: MenuClass,
            State.ADD_FLASHCARD: AddFlashcardClass,
            State.PRACTICE: PracticeClass,
            State.STAY: self.get_state_object,
            State.EXIT: self.exit,
            State.WRITE_TO_DB: WriteToDB,
            State.READ_FROM_DB: ReadFromDB,
            State.UPDATE: UpdateClass
        }
        self.db = None
        self.practice_card = 0
        self.practice_box = 1
        self.flashcards = []
        self.update_cards = {}
        self.delete_cards = []

    def set_state(self, state: State) -> None:
        if state != State.STAY:
            self._state = state
        self._state_object = self._orchestrator[state]()
        if self._state_object:
            self._state_object.set_context(self)

    def get_state(self):
        return self._state

    def get_state_object(self):
        return self._state_object

    @staticmethod
    def exit():
        print("Bye!")

    def request(self) -> State:
        return self._state_object.handle()

    def start(self):
        current_state = State.MENU
        self.db = DBHandler()
        while current_state != State.EXIT:
            self.set_state(current_state)
            current_state = self.request()
        self.exit()

