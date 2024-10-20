from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 3,
    'title': 'Developer',
    'location': 'Delhi, India',
    'salary': 'Rs. 14,00,000'
}, {
    'id': 1,
    'title': 'Devops Engineer',
    'location': 'Delhi, India'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
