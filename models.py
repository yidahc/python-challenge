from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Solution(db.Model):
    __tablename__ = 'solutions'
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.String(50))
    n = db.Column(db.Integer)
    total = db.Column(db.Integer)

#Defining the solution model, with columns storing solutions along with it's corresponding N and total amount of solutions for testing

#Defining how our data will be represented
 #   def __repr__(self):
  #      return "<Solution(id='%d', board='%s', n='%d', total='%d')>"\
   #         .format(self.id, self.board, self.n, self.total)
