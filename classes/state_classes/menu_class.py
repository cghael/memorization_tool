from enum import Enum

from .state_class import State, StateClass


class MenuClass(StateClass):
    def __init__(self):
        super().__init__()

    def handle(self) -> Enum:
        self.print_menu()
        user_input = self.handle_input()
        if user_input is None:
            return State.STAY
        return user_input

    @staticmethod
    def print_menu():
        print(f"\n1. Add flashcards\n"
              f"2. Practice flashcards\n"
              f"3. Exit\n")
