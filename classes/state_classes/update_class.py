from .state_class import State, StateClass


class UpdateClass(StateClass):
    def __init__(self):
        super().__init__()

    def handle(self) -> State:
        ctx = self.get_context()
        for k, v in ctx.update_cards.items():
            update_entity = ctx.query[k]
            box_id = v.get("box_id")
            if box_id is not None:
                ctx.db.update_entity(update_entity, new_box_id=box_id)
            else:
                question = v.get("question")
                answer = v.get("answer")
                ctx.db.update_entity(
                    update_entity,
                    new_question=question,
                    new_answer=answer
                )

        for entity_id in ctx.delete_cards:
            ctx.db.delete_entity(ctx.query[entity_id])

        ctx.query = None
        ctx.update_cards = {}
        ctx.delete_cards = []
        ctx.practice_box = ctx.practice_box + 1 if ctx.practice_box < 3 else 1

        return State.MENU
