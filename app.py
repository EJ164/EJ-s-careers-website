from flask import Flask, render_template
from flask.json import jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$50,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Remote',
    'salary': '$80,000'
  },
  {
    'id': 3,
    'title': 'Computer Scientist',
    'location': 'Berea Kentucky',
    'salary': '$45,000'
  },
  {
    'id': 4,
    'title': 'Data Analyst',
    'location': 'Berea Kentucky',
    'salary': '$45,000'
  }
]


@app.route("/")
def hello_EJ():
    return render_template('home.html', jobs=JOBS)
                        
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)