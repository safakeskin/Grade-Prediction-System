from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS


mysql = MySQL()
app = Flask(__name__)
CORS(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '456'
app.config['MYSQL_DATABASE_DB'] = 'GradePrediction'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
db = mysql.connect()
parser = reqparse.RequestParser()

BACKEND_HOST = '0.0.0.0'
BACKEND_PORT = 5000

@app.route('/lecture/<lecture_id>', methods=['GET', 'OPTIONS'])
def GetLectureName(lecture_id):
    try:
        cursor = db.cursor()
        query = "SELECT lectureName, crn FROM Lecture WHERE id = %s"
        cursor.execute(query, (lecture_id))
        data = cursor.fetchall()
        resp = jsonify({"success": True, "lecture": data[0][0], "crn": data[0][1]})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": e})

@app.route('/exam/<exam_id>', methods=['GET', 'OPTIONS'])
def GetExamName(exam_id):
    try:
        cursor = db.cursor()
        query = "SELECT examType FROM ExamType WHERE id = %s"
        cursor.execute(query, (exam_id))
        data = cursor.fetchall()
        resp = jsonify({"success": True, "exam": data[0][0]})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": e})

@app.route('/exam/list', methods=['GET', 'OPTIONS'])
def GetExamList():
    try:
        cursor = db.cursor()
        query = "SELECT examType FROM ExamType"
        cursor.execute(query)
        data = cursor.fetchall()
        # resp = jsonify(data)
        resp = jsonify({"success": True, "exam": data})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": e})

@app.route('/lecture/exam/<lecture_id>', methods=['GET', 'OPTIONS'])
def GetLectureExam(lecture_id):
    try:
        cursor = db.cursor()
        query = "SELECT ExamType.examType FROM ExamType, Exam WHERE ExamType.id = Exam.examType AND Exam.lecture = %s"
        cursor.execute(query, (lecture_id))
        data = cursor.fetchall()
        # resp = jsonify(data)
        resp = jsonify({"success": True, "exam": data})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": e})


@app.route('/question/count/<lecture_id>/<exam_id>', methods=['GET', 'OPTIONS'])
def QuestionCount(lecture_id, exam_id):
    try:
        cursor = db.cursor()
        query = "SELECT COUNT(*) FROM Question WHERE lecture = %s AND exam = %s"
        cursor.execute(query, (lecture_id,exam_id))
        data = cursor.fetchall()
        resp = jsonify({"success": True, "count": data[0][0]})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": e})

@app.route('/question/select/<lecture_id>/<exam_id>/<question_no>', methods=['GET', 'OPTIONS'])
def SelectQuestion(lecture_id, exam_id, question_no):
    try:
        cursor = db.cursor()
        query = "SELECT question FROM Question WHERE lecture = %s AND exam = %s AND questionNo = %s"
        cursor.execute(query, (lecture_id,exam_id,question_no))
        data = cursor.fetchall()
        if (data):
            resp = jsonify({"success": True, "question": data[0][0]})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"success": False, "message": "There is no question."})
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/question/create/<lecture_id>/<exam_id>/<question_no>/<question>', methods=['POST', 'OPTIONS'])
def CreateQuestion(lecture_id, exam_id, question_no, question):
    try:
        cursor = db.cursor()
        query = "INSERT INTO Question (lecture, exam, questionNo, question) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (lecture_id,exam_id,question_no,question))
        db.commit()
        resp = jsonify({'success': True})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/question/delete/<lecture_id>/<exam_id>/<question_no>', methods=['POST', 'OPTIONS'])
def DeleteQuestion(lecture_id, exam_id, question_no):
    try:
        cursor = db.cursor()
        query = "DELETE FROM Question  WHERE (lecture = %s AND exam = %s AND questionNo = %s)"
        cursor.execute(query, (lecture_id,exam_id,question_no))
        db.commit()
        resp = jsonify({'success': True})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": e})
        return resp

if __name__ == '__main__':
    app.run(debug=True,host=BACKEND_HOST, port=BACKEND_PORT)