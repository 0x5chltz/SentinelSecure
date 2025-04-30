from flask import Flask, request, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key= 'hellno'

user = 'ujian'
passwd = 'qwertyuiop'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == user and password == passwd:   
            return redirect(url_for('success'))
        else:
            return redirect(url_for('invalid'))

    return render_template('login.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/invalid', methods=['GET', 'POST'])
def invalid():
    return render_template('invalid.html')

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, True)