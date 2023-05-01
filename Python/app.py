from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('status.html')

@app.route('/vaccination-status', methods=['POST'])
def get_vaccination_status():
    data = request.form.to_dict()
    reg_no = data['registration_no']

    db = mysql.connector.connect(
        host='127.0.0.1',
        port="3307",
        user="root",
        password="password",
        database="student_db"
    )
     
         

    cursor = db.cursor()
    cursor.execute(f"SELECT vaccination_status FROM students WHERE reg_no='{reg_no}'")
    result = cursor.fetchone()

    if result:
        return render_template('output.html', vaccination_status=result[0])
    else:
        return render_template('output.html', error='Invalid registration number')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
