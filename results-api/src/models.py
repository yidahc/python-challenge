#We need to inherit Base in order to register models with SQA. Without this, SQA wouldn't know anything about our models.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Defining the solution model, with only primarmy key and solutions colum
class Solution(db.Model):
    __tablename__ = 'solutions'
    id = db.Column(db.Integer, primary_key=True)
    array = db.Column(db.String(50))
    n = db.Column(db.Integer)
    total = db.Column(db.Integer)

#Defining how our data will be represented
 #   def __repr__(self):
  #      return "<Solution(id='{}', array='{}', n='{}', total='{}')>"\
   #         .format(self.id, self.array, self.n, self.total)

# sqlalchemy & postgress learned from https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/?fbclid=IwAR2YYvFgPMvGfEIeFPSVsZ0XvIQCWpvzAWhcMr0lU-9jNL9ndvbbU3pPluQ