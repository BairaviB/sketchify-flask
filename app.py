from flask import Flask,render_template
from sketchify import sketch

  
app = Flask(__name__)
PORT = 3000
  
@app.route("/")
def startpy():
    
    sketch.normalsketch('/home/prawin/Desktop/tact/sketchify-flask/moth.jpg',
    '/home/prawin/Desktop/tact/sketchify-flask','mothdraw1')

    return render_template("index.html") 
    


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=PORT)