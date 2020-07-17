from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yryxpejb:D-gAIpda9X7ANuob2dp-FjFFc9jbdQV5@ruby.db.elephantsql.com:5432/yryxpejb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
 
class Email(db.Model):
  __tablename__ = 'maillist'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)

  def __init__(self, email):
    self.email = email


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
      email = request.form['email']

      if db.session.query(Email).filter(Email.email == email).count() == 0:
        data = Email(email)
        db.session.add(data)
        db.session.commit()

        return render_template("index.html", message="You having been added to our mailing list")
      
      return render_template("index.html", message="We are really excited too but you're already on our mailing list!")
      



if __name__ == '__main__':
  app.run()