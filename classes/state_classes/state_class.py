from abc import ABC, abstractmethod
from enum import Enum


class State(Enum):
    MENU = 0
    ADD_FLASHCARD = 1
    PRACTICE = 2
    EXIT = 3
    STAY = 4
    WRITE_TO_DB = 5
    READ_FROM_DB = 6
    ADD = 7
    UPDATE = 8


TRANSITIONS = {
        State.MENU: {
            1: State.ADD_FLASHCARD,
            2: State.READ_FROM_DB,
            3: State.EXIT
        },
        State.ADD_FLASHCARD: {
            1: State.ADD,
            2: State.EXIT
        },
        State.ADD: {
            1: State.STAY
        },
        State.WRITE_TO_DB: {
            1: State.MENU
        },
        State.READ_FROM_DB: {
            1: State.PRACTICE
        },
        State.PRACTICE: {
            1: State.MENU,
            2: State.UPDATE
        },
        State.UPDATE: {
            1: State.MENU
        }
    }


class StateClass(ABC):

    def __init__(self):
        self._context = None

    def set_context(self, context) -> None:
        self._context = context

    def get_context(self):
        return self._context

    def handle_input(self):
        user_input = None
        try:
            user_input = input()
            int_input = int(user_input)
            return TRANSITIONS[self._context.get_state()][int_input]
        except ValueError:
            print(f"{user_input} is not an option")
            return None
        except KeyError:
            print(f"{user_input} is not an option")
            return None

    @abstractmethod
    def handle(self) -> State:
        pass
