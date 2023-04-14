from .state_class import State, StateClass


class ReadFromDB(StateClass):
    def __init__(self):
        super().__init__()

    def handle(self) -> State:
        ctx = self.get_context()
        ctx.query = ctx.db.get_data(box_id=ctx.practice_box)
        return State.PRACTICE
