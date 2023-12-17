from flask import Flask, request, redirect, url_for, render_template, session
import os


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = os.urandom(24)  # Replace with a random key

UPLOAD_FOLDER = '/tmp/userdata/roms'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024  # 64MB max file size
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict' # SameSite cookie policy
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Enable HttpOnly flag

@app.route('/')
def dashboard():
    session['loggedin'] = True
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if not session.get('loggedin'):
        # If the user is not logged in, redirect to the home page
        return redirect('/') 
    file = request.files['file']
    if file.filename == '':
        msg = "Something went wrong, please try again!"
        return render_template('index.html', msg=msg)
    if file:
        msg = "Your rom has been uploaded and is ready to be played!"
        filename = file.filename
        console_value = request.form['console']
        file.save(os.path.join(app.config['UPLOAD_FOLDER']+"/"+console_value, filename))
        # Kill EmulationStation to force reload games
        os.system("sudo killall emulationstation")
        return render_template('index.html', msg=msg)
    
if __name__ == '__main__':
   app.run(debug=True)