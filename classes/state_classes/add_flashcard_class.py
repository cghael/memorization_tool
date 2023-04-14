from enum import Enum

from .state_class import State, StateClass


class AddFlashcardClass(StateClass):
    def __init__(self):
        super().__init__()

    def handle(self) -> Enum:
        self.print_menu()
        user_input = self.handle_input()
        if user_input is None:
            return State.STAY
        if user_input == State.EXIT:
            return State.WRITE_TO_DB
        return self.add_flashcard()

    @staticmethod
    def print_menu():
        print(f"\n1. Add a new flashcard\n"
              f"2. Exit")

    def add_flashcard(self):
        question = ""
        answer = ""
        ctx = self.get_context()
        while not question:
            question = input("\nQuestion:\n").strip()
        while not answer:
            answer = input("\nAnswer:\n").strip()
        ctx.flashcards.append([question, answer])
        return State.STAY
