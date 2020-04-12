from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods =["GET","POST"])
def main():
  if request.method == "GET":
    return render_template("index.html")

  
    
  else: #post
    '''
    qn = request.form.get('q')
    if qn =="how":
      a = "good morning!"
    else:
      a = "yo!"
    return render_template("index.html", a=a)
    '''
    A = request.form.get('a')
    B = request.form.get('b')
    C = request.form.get('c')
    D = request.form.get('d')
    E = request.form.get('e')
    F = request.form.get('f')
    G = request.form.get('g')
    H = request.form.get('h')

    condition2 = 0
    for i in range(3):
      if D == "No":
        condition2 +=1
      if E == "Sometimes":
        condition2 +=1

      if G == "Yes":
        condition2 += 1


    if A == "No" or B=="No" :
      msg = "Failed the vibe check. Take care of your personal hygene!" 
    elif condition2 >1:
      msg = " You can do better! Reminder to be socially responsible in these trying times"
    else:
      msg = " You passed the vibe check! Congratulations! "
      

    return render_template("return.html", A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, msg=msg, condition2=condition2)

 

@app.route('/e')
def main2():     
   return render_template('easter.html')

app.run(host='0.0.0.0', port=8080)