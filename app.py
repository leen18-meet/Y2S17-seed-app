# flask imports
from flask import Flask, render_template, request, redirect, url_for

# SQLAlchemy
from model import Base, Users, Videos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup
app = Flask(__name__)
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/Register', methods=['GET','POST'])
def register():

    #If it's a simple get, return the wanted page.
    if request.method == 'GET':
        return render_template('register.html')
    
    #If the user pressing register button it will try to sign him up
    #and return "Login page".   
    else:
        username      = request.form.get('username')
        name          = request.form.get('fullname')
        password      = request.form.get('password')
        email         = request.form.get('email')
        country       = request.form.get('country')
        sing          = request.form.get('sing')
        guitar        = request.form.get('guitar')
        drums         = request.form.get('drums')
        flute         = request.form.get('flute')

        #If this username is already exists it will bring you back.
        if session.query(Users).filter_by(username = username).first():
            return redirect(url_for('Register'))
        
        #If it's a new one create a new user and go to the "Login" page
        else:            
            user = Users(username = username, name = name, password = password, email = email, country = country, sing = sing, guitar = guitar, drums = drums, flute = flute)
            session.add(user)
            session.submit(user)

            return redirect(url_for('Login'))

@app.route('/Login', methods=['GET','POST'])
def login():
    
    if request.method == 'GET':
        return render_template('login.html')

    #Checking if it's a real username and real password
    else:
        check_username      = request.form.get('check_username')
        check_password      = request.form.get('check_password')

        wanted_user         = session.query(Users).filter_by(username = check_username).first()

        #if it is correct continue to the homepage
        if wanted_user.password is check_password:
            return redirect(url_for('Home',user_id = wanted_user.id))
        #Ekse try again
        else:
            return redirect(url_for('Login'))

@app.route('/Home/<int:user_id>')
def home(user_id):

    #Publishing on the feed all the videos and also saving the user (NOTE : there is a need?)
    user = session.querry(Users).filter_by(id = user_id).first()

    videos = session.querry(Videos).all()

    return render_template('home.html', user = user, vidoes = videos)

@app.route('/Profile/<int:user_id>')
def profile(user_id):

    #Showing the whole videos of the current user and showing all the info about him.
    user = session.querry(Users).filter_by(id = user_id).first()

    videos = session.querry(Videos).filter_by(poster = user.name).all()

    return render_template('profile.html', user = user, videos = videos)

@app.route('/Friends/<int:user_id>')
def friends(user_id):

    #Showing the current user friend list
    user = session.querry(Users).filter_by(id = user_id).first()
    return render_template('friends.html', user = user)

@app.route('/Publish/<int:user_id>', methods=['GET','POST'])
def publish(user_id):
    user = session.querry(Users).filter_by(id = user_id).first()
    if request.method == 'GET':
        return render_template('publish.html', user = user)

    #Creare new video to publish
    else:
        video         = request.form.get('video')
        description   = request.form.get('description')
        comment       = request.form.get('comment')
        rating        = request.form.get('rating')
        poster        = request.form.get('poster')
        
        newVid = Videos(video = video, description = description, comment = comment, rating = rating, poster = poster)

        session.add(newVid)
        session.commit()
        return redirect_url('Home',user_id = user_id)

@app.route('/Add/<int:user_id>/<int:video_id>', methods=['GET','POST'])
def add(user_id, video_id):

    #Taking the old video ti present it to the user and also to mention the video last publisher to post it
    #Interactivly
    user = session.querry(Users).filter_by(id = user_id).first()
    video = session.querrt(Videos).filter_by(id = video_id).first()

    if request.method == 'GET':
        return render_template('add.html', user = user, video = video)

    #Adding the video with refrence to the old one
    else
        video         = request.form.get('video')
        description   = request.form.get('description')
        comment       = request.form.get('comment')
        rating        = request.form.get('rating')
        poster        = request.form.get('poster')

        otherVideo = video.id
        publish = false        

        newVid = Videos(video = video, description = description, publih = publish, otherVideo = otherVideo, comment = comment, rating = rating, poster = poster)
        session.add(newVid)
        session.commit()

        return redirect_url('Home',user_id = user_id)


                                                ############
                                                #          #
                                                #  NOTE'S  #
                                                #          #
                                                ############
#Ask an instructor if it's possible to create a linked list out of the friend list as a feature (MODEL).
#Ask an instructor how to present an actual video (FRONTEND).
#Think about a more efficiant way to store the data (MODEL).
#FEATURE : create out own icon's to put insted of boring button like a picture button(CSS).
#Ask an instructor to help backend team to debug and understand if the code is good.
#Ask an instructor if it's possible to make a kind of a "scroll".

