from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__)
app.secret_key = 'plutofuture'

username = ''
user = model.check_users()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if 'username' in session:
        g.user = session['username']
        return render_template('football.html')
    return render_template('homepage.html', message = 'log in to the page or sign up')


    """
    if request.method == 'GET':
        return render_template('index.html', message = 'Welcome to the index page')
    else:
        username = request.form['username']
        password = request.form['password']
        db_password = model.check_pw(username)

        if password == db_password:
            message = model.show_color(username)
            return render_template('football.html', message = message)
        else:
            error_message = 'Hint: He curses a lot'
            return render_template('index.html', message = error_message)
    """

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        areyouuser = rrequest.form['username']
        pwd = model.check_pw(areyouuser)
        if request.form['password'] == pwd:
            session['username'] = request.form['username']
            return redirect(url_for('home'))

@app.route('/football', methods = ['GET'])
def football():
    return render_template('football.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = 'Please sign up!'
        return render_template('signup.html', message = message)
    else:
        username = request.form['username']
        password = request.form['password']
        favorite_color = request.form['favorite_color']
        message = model.signup(username, password, favorite_color)
        return render_template('signup.html', message = message)



if __name__ == '__main__':
    app.run(port = 7000, debug = True)
