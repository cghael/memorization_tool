from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class DBHandler:
    def __init__(self):
        self.session = Session()
        Base.metadata.create_all(engine)

    def add_data(self, question, answer, box_id=1):
        new_data = Data(box_id=box_id, question=question, answer=answer)
        self.session.add(new_data)
        self.session.commit()

    def get_data(self, box_id=None):
        query = self.session.query(Data)
        if box_id is not None:
            data = query.filter(Data.box_id <= box_id)
        else:
            data = query.all()
        return data

    def update_entity(self, update_entity, new_box_id=None, new_question=None, new_answer=None):
        if new_box_id is not None:
            update_entity.box_id = new_box_id
        if new_question is not None:
            update_entity.question = new_question
        if new_answer is not None:
            update_entity.answer = new_answer
        self.session.commit()

    def delete_entity(self, delete_entity):
        self.session.delete(delete_entity)
        self.session.commit()


class Data(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    box_id = Column(Integer)
    question = Column(String)
    answer = Column(String)
