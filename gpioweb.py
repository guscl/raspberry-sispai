from flask import Flask, render_template
from request_maker import eventHandler
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)

#Initial setUp
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.IN)
GPIO.output(7, False)
GPIO.output(11, False)
now = datetime.datetime.now()
timeString = now.strftime("%Y-%m-%d %H:%M")

#Defining how the program will answers to requests 

@app.route("/")
def hello():
   templateData = {
      'title' : 'RPi GPIO Control',
      'time': timeString
      }
   return render_template('gpioweb.html', **templateData)


@app.route("/4/on")
def action4on():
    GPIO.output(7, True)
    message = "GPIO 4 was turned on."
    templateData = {
        'message' : message,
        'time' : timeString
    }
    return render_template('gpioweb.html', **templateData)
    
@app.route("/4/off")
def action4off():
    GPIO.output(7, False)
    message = "GPIO 4 was turned off."
    templateData = {
        'message' : message,
        'time' : timeString
    }
    return render_template('gpioweb.html', **templateData)

@app.route("/17/on")
def action17on():
    GPIO.output(11, True)
    message = "GPIO 17 was turned on."
    templateData = {
        'message' : message,
        'time' : timeString
    }
    return render_template('gpioweb.html', **templateData)

@app.route("/17/off")
def action17off():
    GPIO.output(11, False)
    message = "GPIO 17 was turned off."
    templateData = {
        'message' : message,
        'time' : timeString
    }
    return render_template('gpioweb.html', **templateData)


@app.route("/all/on")
def actionallon():
    GPIO.output(7, True)
    GPIO.output(11, True)
    GPIO.output(12, True)
      
    message = "All GPIO pins were turned on."
    templateData = {
        'message' : message,
        'time' : timeString
    }
    return render_template('gpioweb.html', **templateData)

@app.route("/all/off")
def actionalloff():
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(12, False)
   
  
    message = "All GPIO pins were turned off."
    templateData = {
        'message' : message,
        'time' : timeString
    }
    return render_template('gpioweb.html', **templateData)


#Creating the event and passing on the function it will call
GPIO.add_event_detect(13, GPIO.FALLING, callback=eventHandler, bouncetime=300)


if __name__ == "__main__":
     app.run(threaded=True,host="10.42.0.30")
  
