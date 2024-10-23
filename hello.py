from flask import Flask, render_template,flash, redirect, url_for,session
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)



@app.route('/',methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        oldname = session.get('name')
        if oldname is not None and oldname != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    name=session.get('name')
    return render_template('index.html', form=form, name=name)
    

if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/user/<name>')
# def user(name):
#     print(f"User route accessed with name: {name}")
#     return render_template('user.html', name=name) 

# name = form.name.data
        # form.name.data = ''  # Clear the input field after submission
        # flash(f'Hello, {name}!')
        # return redirect(url_for('index'))

#  current_time = datetime.utcnow()
#     return render_template('index.html',current_time=current_time)

# @app.route('/user/<name>')
# def user(name):
#      return render_template('user.html', name=name)





# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500



# @app.route('/')
# def index():
#     return render_template('index.html',
#                            current_time=datetime.utcnow())








# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'

# @app.route('/user/<sapna>')
# def user(sapna):
#     return '<h1>Hello, {}!</h1>'.format(sapna)


