from .state_class import State, StateClass


class PracticeClass(StateClass):
    def __init__(self):
        super().__init__()

    def handle(self) -> State:
        ctx = self.get_context()
        if ctx.query.first() is None:
            print("There is no flashcard to practice!")
            return State.MENU
        return self.practice(ctx)

    def practice(self, ctx) -> State:
        while ctx.practice_card < ctx.query.count():
            data = ctx.query[ctx.practice_card]
            print(f"Question: {data.question}")
            user_input = input('press "y" to see the answer:\n'
                               'press "n" to skip:\n'
                               'press "u" to update:\n')

            if user_input not in ("y", "n", "u"):
                print(f"{user_input} is not an option\n")
                continue

            if user_input == "y":
                print(f"Answer: {data.answer}")
                self.handle_memory_status(ctx, data)

            if user_input == "u":
                self.handle_update_status(ctx, data)

            ctx.practice_card += 1

        ctx.practice_card = 0
        return State.UPDATE

    @staticmethod
    def handle_memory_status(ctx, data):
        is_correct = ""
        while True:
            is_correct = input('press "y" if your answer is correct:\n'
                               'press "n" if your answer is wrong:\n')
            if is_correct in ("y", "n"):
                break
            print(f"{is_correct} is not an option\n")

        if is_correct == "y":
            if data.box_id < 3:
                ctx.update_cards[ctx.practice_card] = {"box_id": data.box_id + 1}
            else:
                ctx.delete_cards.append(ctx.practice_card)

    def handle_update_status(self, ctx, data):
        while True:
            user_input = input('press "d" to delete the flashcard:\n'
                               'press "e" to edit the flashcard:\n')
            if user_input in ("e", "d"):
                break
            print(f"{user_input} is not an option\n")

        if user_input == "e":
            self.update_card(ctx, data)
        if user_input == "d":
            ctx.delete_cards.append(ctx.practice_card)

    @staticmethod
    def update_card(ctx, data):
        print(f"current question: {data.question}")
        question = input("please write a new question:\n")
        print(f"current answer: {data.answer}")
        answer = input("please write a new answer:\n")

        ctx.update_cards[ctx.practice_card] = {"question": question,
                                               "answer": answer}
