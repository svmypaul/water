from flask import Flask, render_template,request
import pickle
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',val1='0',val2='0',val3='0',val4='0',val5='0',val6='0',val7='0',val8='0',val9='0')


@app.route('/view',methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
      name_of_slider = request.form["name"]
      name_of_slider1 = request.form["name1"]
      name_of_slider2 = request.form["name2"]
      name_of_slider3 = request.form["name3"]
      name_of_slider4 = request.form["name4"]
      name_of_slider5 = request.form["name5"]
      name_of_slider6 = request.form["name6"]
      name_of_slider7 = request.form["name7"]
      name_of_slider8 = request.form["name8"]
      result=[int(name_of_slider), int(name_of_slider1), int(name_of_slider2), int(name_of_slider3), int(name_of_slider4), int(name_of_slider5), int(name_of_slider6), int(name_of_slider7), int(name_of_slider8)]
      pickle_file = open("water.pkl", "rb")
      model=pickle.load(pickle_file)
      view=model.predict([[ int(name_of_slider), int(name_of_slider1), int(name_of_slider2), int(name_of_slider3), int(name_of_slider4), int(name_of_slider5), int(name_of_slider6), int(name_of_slider7), int(name_of_slider8)]])
      pickle_file.close()

      return render_template('index.html',result=result,view=view,val1=name_of_slider,val2=name_of_slider1,val3=name_of_slider2,val4=name_of_slider3,val5=name_of_slider4,val6=name_of_slider5,val7=name_of_slider6,val8=name_of_slider7,val9=name_of_slider8)

if __name__ == "__main__":  
    app.run(debug=True)