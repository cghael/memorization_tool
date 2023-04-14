from .state_class import State, StateClass


class WriteToDB(StateClass):
    def __init__(self):
        super().__init__()

    def handle(self) -> State:
        if self.get_context().flashcards:
            self.write_to_db()
        return State.MENU

    def write_to_db(self):
        ctx = self.get_context()
        for q, a in ctx.flashcards:
            ctx.db.add_data(q, a)
        ctx.flashcards = []
