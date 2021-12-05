from flask import Flask, request, render_template
from firebase import firebase  
from flask import Response
import pickle

app = Flask(__name__)
@app.route('/')
def home():
    firebase1 = firebase.FirebaseApplication('https://icps-9cc0a.firebaseio.com/', None)
    nl=[]
    pl=[]
    kl=[]
    templ=[]
    huml=[]
    moistl=[]
    phl=[]
    for i in range(5):
        result = firebase1.get('/cropnew/'+str(i+1), '')
        nl.append(result['n'])
        pl.append(result['p'])
        kl.append(result['k'])
        templ.append(result['temp'])
        huml.append(result['temp'])
        moistl.append(result['hum'])
        phl.append(result['ph'])
    print(nl,pl,kl,templ,huml,moistl,phl)
    cl = [nl[4],pl[4],kl[4],templ[4],huml[4],phl[4],71.4]
    fl = [templ[4], huml[4], moistl[4], nl[4],pl[4],kl[4], 9, 3]
    return render_template('login.html',nl=nl,pl=pl,kl=kl,templ=templ,huml=huml,moistl=moistl,phl=phl)

if __name__ == "__main__":
    app.run_server(debug=False)
