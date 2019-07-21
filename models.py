#We need to inherit Base in order to register models with SQA. Without this, SQA wouldn't know anything about our models.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

#Defining the solution model, with only primarmy key and solutions colum
class Solution(Base):
    __tablename__ = 'solutions'
    id = Column(Integer, primary_key=True)
    solution = Column(String)

#Defining how our data will be represented
    def __repr__(self):
        return "<Solution(solution='{}')>"\
            .format(self.solution)