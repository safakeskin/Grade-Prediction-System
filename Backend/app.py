from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS


mysql = MySQL()
app = Flask(__name__)
CORS(app)
app.config['MYSQL_DATABASE_USER'] = 'GradePredictor'
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
        resp = jsonify({"success": False, "message": e})
        return resp

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
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/person/list', methods=['GET', 'OPTIONS'])
def GetPersonList():
    try:
        cursor = db.cursor()
        query = "SELECT * FROM Person"
        cursor.execute(query)
        data = cursor.fetchall()
        # resp = jsonify(data)
        resp = jsonify({"success": True, "exam": data})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/semester/list', methods=['GET', 'OPTIONS'])
def GetSemesterList():
    try:
        cursor = db.cursor()
        query = "SELECT term FROM Semester"
        cursor.execute(query)
        data = cursor.fetchall()
        # resp = jsonify(data)
        resp = jsonify({"success": True, "exam": data})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/lecture/list', methods=['GET', 'OPTIONS'])
def GetLectureList():
    try:
        cursor = db.cursor()
        query = "SELECT lectureName, semester, year FROM Lecture"
        cursor.execute(query)
        data = cursor.fetchall()
        # resp = jsonify(data)
        resp = jsonify({"success": True, "exam": data})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/exam_type/list', methods=['GET', 'OPTIONS'])
def GetExamTypeList():
    try:
        cursor = db.cursor()
        query = "SELECT examType FROM ExamType"
        cursor.execute(query)
        data = cursor.fetchall()
        # resp = jsonify(data)
        resp = jsonify({"success": True, "exam_types": data})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

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
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/answer/<question_id>/<student_id>', methods=['GET', 'OPTIONS'])
def GetAnswer(question_id, student_id):
    try:
        cursor = db.cursor()
        query = "SELECT content FROM Answer WHERE (question = %s AND student = %s)"
        cursor.execute(query, (question_id, student_id))
        data = cursor.fetchall()
        resp = jsonify({"success": True, "answer": data})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/answer/list', methods=['GET', 'OPTIONS'])
def GetAnswerList():
    try:
        cursor = db.cursor()
        query = "SELECT * FROM Answer"
        cursor.execute(query)
        data = cursor.fetchall()
        resp = jsonify({"success": True, "answer": data})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/question/count/<lecture_id>/<exam_id>', methods=['GET', 'OPTIONS'])
def QuestionCount(lecture_id, exam_id):
    try:
        cursor = db.cursor()
        query = "SELECT COUNT(*) FROM Question WHERE lecture = %s AND exam = %s"
        cursor.execute(query, (lecture_id, exam_id))
        data = cursor.fetchall()
        resp = jsonify({"success": True, "count": data[0][0]})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/lecture/select/<lecture_name>/<semester>/<year>', methods=['GET', 'OPTIONS'])
def SelectLecture(lecture_name, semester, year):
    try:
        cursor = db.cursor()
        query = "SELECT id FROM Lecture WHERE lectureName = %s AND semester = %s AND year = %s"
        cursor.execute(query, (lecture_name, semester, year))
        data = cursor.fetchall()
        if (data):
            resp = jsonify({"success": True, "lecture_id": data[0][0]})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"success": False, "message": "There is no lecture."})
            resp.status_code = 200      # TODO: change status code
            return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/exam/select/<lecture_name>/<exam_type>', methods=['GET', 'OPTIONS'])
def SelectExam(lecture_name, exam_type):
    try:
        cursor = db.cursor()
        query = "SELECT id FROM Exam WHERE lecture = %s AND examType = %s"
        cursor.execute(query, (lecture_name, exam_type))
        data = cursor.fetchall()
        if (data):
            resp = jsonify({"success": True, "exam_id": data[0][0]})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"success": False, "message": "There is no exam."})
            resp.status_code = 200      # TODO: change status code
            return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/question/select/<lecture_id>/<exam_id>/<question_no>', methods=['GET', 'OPTIONS'])
def SelectQuestion(lecture_id, exam_id, question_no):
    try:
        cursor = db.cursor()
        query = "SELECT question FROM Question WHERE lecture = %s AND exam = %s AND questionNo = %s"
        cursor.execute(query, (lecture_id, exam_id, question_no))
        data = cursor.fetchall()
        if (data):
            resp = jsonify({"success": True, "question": data[0][0]})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"success": False, "message": "There is no question."})
            resp.status_code = 200      # TODO: change status code
            return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/answer/submit/<question_id>/<student_id>/<content>', methods=['POST', 'OPTIONS'])
def SubmitAnswer(question_id, student_id, content):
    try:
        success, q_id = ExistAnswer(question_id, student_id)
        if (not success):
            cursor = db.cursor()
            query = "INSERT INTO Answer (question, student, content) VALUES (%s, %s, %s)"
            cursor.execute(query, (question_id, student_id, content))
            db.commit()
            resp = jsonify({'success': True})
            resp.status_code = 200
            return resp
        else:
            cursor = db.cursor()
            query = "UPDATE Answer SET content = %s WHERE id = %s"
            cursor.execute(query, (content, q_id))
            db.commit()
            resp = jsonify({'success': True, "message": "Answer is updated."})
            resp.status_code = 200
            return resp
    except Exception as e: 
        resp = jsonify({"success": False, "message": e})
        return resp   

@app.route('/person/create/<first_name>/<last_name>/<student_id>', methods=['POST', 'OPTIONS'])
def CreatePerson(first_name, last_name, student_id):
    try:
        cursor = db.cursor()
        query = "INSERT INTO Person (firstName, lastName, studentID) VALUES (%s, %s, %s)"
        cursor.execute(query, (first_name, last_name, student_id))
        db.commit()
        resp = jsonify({'success': True})
        resp.status_code = 200
        return resp
    except Exception as e: 
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/lecture/create/<crn>/<lecture_name>/<semester>/<year>', methods=['POST', 'OPTIONS'])
def CreateLecture(crn, lecture_name, semester, year):
    try:
        success = ExistLecture(lecture_name, semester, year)
        if (not success):
            cursor = db.cursor()
            query = "INSERT INTO Lecture (crn, lectureName, semester, year) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (crn, lecture_name, semester, year))
            db.commit()
            resp = jsonify({'success': True})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"success": False, "message": "Lecture already exists."})
            return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/exam/create/<lecture_id>/<exam_type>/<is_active>', methods=['POST', 'OPTIONS'])
def CreateExam(lecture_id, exam_type, is_active):
    try:
        success = HaveThatExam(lecture_id, exam_type)
        if (not success):
            cursor = db.cursor()
            query = "INSERT INTO Exam (lecture, examType, isActive) VALUES (%s, %s, %s)"
            cursor.execute(query, (lecture_id, exam_type, is_active))
            db.commit()
            resp = jsonify({'success': True})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"success": False, "message": "Lecture already have same exam."})
            return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/question/create/<lecture_id>/<exam_id>/<question_no>/<question>', methods=['POST', 'OPTIONS'])
def CreateQuestion(lecture_id, exam_id, question_no, question):
    try:
        cursor = db.cursor()
        query = "INSERT INTO Question (lecture, exam, questionNo, question) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (lecture_id, exam_id, question_no, question))
        db.commit()
        resp = jsonify({'success': True})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/lecture/delete/<lecture_id>', methods=['POST', 'OPTIONS'])
def DeleteLecture(lecture_id):
    try:
        cursor = db.cursor()
        query = "DELETE FROM Lecture WHERE (id = %s)"
        cursor.execute(query, (lecture_id))
        db.commit()
        resp = jsonify({'success': True})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/exam/delete/<lecture_id>/<exam_type>', methods=['POST', 'OPTIONS'])
def DeleteExam(lecture_id, exam_type):
    try:
        success = HaveThatExam(lecture_id, exam_type)
        if (success):
            cursor = db.cursor()
            query = "DELETE FROM Exam WHERE (lecture = %s AND examType = %s)"
            cursor.execute(query, (lecture_id, exam_type))
            db.commit()
            resp = jsonify({'success': True})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"success": False, "message": "Lecture does not have that exam."})
            return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/question/delete/<lecture_id>/<exam_id>/<question_no>', methods=['POST', 'OPTIONS'])
def DeleteQuestion(lecture_id, exam_id, question_no):
    try:
        cursor = db.cursor()
        query = "DELETE FROM Question WHERE (lecture = %s AND exam = %s AND questionNo = %s)"
        cursor.execute(query, (lecture_id, exam_id, question_no))
        db.commit()
        resp = jsonify({'success': True})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/student/add/<lecture_id>/<student_id>', methods=['POST', 'OPTIONS'])
def AddStudent2Lecture(lecture_id, student_id):
    try:
        success = isAddedStudent(lecture_id, student_id)
        if (not success):
            cursor = db.cursor()
            query = "INSERT INTO LectureStudent (lecture, student) VALUES (%s, %s)"
            cursor.execute(query, (lecture_id, student_id))
            db.commit()
            resp = jsonify({'success': True})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"success": False, "message": "Student is already added to lecture."})
            return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/student/remove/<lecture_id>/<student_id>', methods=['POST', 'OPTIONS'])
def RemoveStudentFromLecture(lecture_id, student_id):
    try:
        success = isAddedStudent(lecture_id, student_id)
        if (success):
            cursor = db.cursor()
            query = "DELETE FROM LectureStudent WHERE (lecture = %s AND student = %s)"
            cursor.execute(query, (lecture_id, student_id))
            db.commit()
            resp = jsonify({'success': True})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"success": False, "message": "There is no student in the lecture."})
            return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/exam/activate/<exam_id>', methods=['POST', 'OPTIONS'])
def ActivateExam(exam_id):
    try:
        cursor = db.cursor()
        query = "UPDATE Exam SET isActive = 1 WHERE id = %s"
        cursor.execute(query, (exam_id))
        db.commit()
        resp = jsonify({'success': True})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

@app.route('/exam/deactivate/<exam_id>', methods=['POST', 'OPTIONS'])
def DeactivateExam(exam_id):
    try:
        cursor = db.cursor()
        query = "UPDATE Exam SET isActive = 0 WHERE id = %s"
        cursor.execute(query, (exam_id))
        db.commit()
        resp = jsonify({'success': True})
        resp.status_code = 200
        return resp
    except Exception as e:
        resp = jsonify({"success": False, "message": e})
        return resp

def ExistLecture(lecture_name, semester, year):
    try:
        cursor = db.cursor()
        query = "SELECT id FROM Lecture WHERE (lectureName = %s AND semester = %s AND year = %s)"
        cursor.execute(query, (lecture_name, semester, year))
        data = cursor.fetchall()
        if (data):
            return True
        else:
            return False
    except:
        return False   

def HaveThatExam(lecture_id, exam_type):
    try:
        cursor = db.cursor()
        query = "SELECT id FROM Exam WHERE (lecture = %s AND examType = %s)"
        cursor.execute(query, (lecture_id, exam_type))
        data = cursor.fetchall()
        if (data):
            return True
        else:
            return False
    except:
        return False

def isAddedStudent(lecture_id, student_id):
    try:
        cursor = db.cursor()
        query = "SELECT id FROM LectureStudent WHERE (lecture = %s AND student = %s)"
        cursor.execute(query, (lecture_id, student_id))
        data = cursor.fetchall()
        if (data):
            return True
        else:
            return False
    except:
        return False

def ExistAnswer(question_id, student_id):
    try:
        cursor = db.cursor()
        query = "SELECT id FROM Answer WHERE (question = %s AND student = %s)"
        cursor.execute(query, (question_id, student_id))
        data = cursor.fetchall()
        if (data):
            return True, data
        else:
            return False, 0
    except:
        return False, 0

        
if __name__ == '__main__':
    app.run(debug=True, host=BACKEND_HOST, port=BACKEND_PORT)
