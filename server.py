from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'darksecret'


@app.route("/")
def root():
    if 'visits' not in session:
        session['visits'] = 0
    session['visits'] += 1
    return render_template("checker.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/twice")
def twice():
    session['visits']+=1
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
