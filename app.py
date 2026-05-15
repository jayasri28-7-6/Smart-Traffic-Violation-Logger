from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import qrcode
import os
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Violation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle = db.Column(db.String(20))
    vehicle_type = db.Column(db.String(20))
    violation = db.Column(db.String(100))
    location = db.Column(db.String(100))
    date = db.Column(db.String(20))
    fine = db.Column(db.Integer)
    status = db.Column(db.String(10))


@app.route('/')
def home():

    search = request.args.get("search")

    if search:
        records = Violation.query.filter(Violation.vehicle.contains(search)).all()
    else:
        records = Violation.query.all()

    total = len(records)
    paid = len([r for r in records if r.status=="Paid"])
    unpaid = len([r for r in records if r.status=="Unpaid"])

    return render_template("index.html",
                           records=records,
                           total=total,
                           paid=paid,
                           unpaid=unpaid)


@app.route('/add', methods=['GET','POST'])
def add():

    if request.method == 'POST':

        vehicle = request.form['vehicle']
        vehicle_type = request.form['vehicle_type']
        violation = request.form['violation']

        if violation == "custom":
            violation = request.form['customViolation']

        location = request.form['location']
        date = request.form['date']
        fine = request.form['fine']

        new_record = Violation(
            vehicle=vehicle,
            vehicle_type=vehicle_type,
            violation=violation,
            location=location,
            date=date,
            fine=fine,
            status="Unpaid"
        )

        db.session.add(new_record)
        db.session.commit()

        url = f"http://127.0.0.1:5000/status/{new_record.id}"

        if not os.path.exists("static/qr"):
            os.makedirs("static/qr")

        img = qrcode.make(url)
        img.save(f"static/qr/{new_record.id}.png")

        return redirect('/')

    today = datetime.now().strftime("%Y-%m-%d")

    return render_template("add_violation.html",today=today)


@app.route('/status/<int:id>')
def status(id):

    record = Violation.query.get(id)

    return render_template("status.html",record=record)


@app.route('/pay/<int:id>')
def pay(id):

    record = Violation.query.get(id)
    record.status="Paid"

    db.session.commit()

    return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):

    record = Violation.query.get(id)

    db.session.delete(record)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)