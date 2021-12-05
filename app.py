from flask import Flask, request, render_template
from firebase import firebase  
from flask import Response
import pickle


app = Flask(__name__)






model = pickle.load(open('model.sav', 'rb'))
cropl = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas','mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate','banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple','orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
p1 = [20, 11,  3,  9, 18, 13, 14,  2, 10, 19,  1, 12,  7, 21, 15,  0, 16, 17,  4,  6,  8,  5]

model2 = pickle.load(open('fert_pred.sav', 'rb'))
fertl = ['Urea', 'DAP', '14-35-14', '28-28', '17-17-17', '20-20','10-26-26']
p2 = [6, 5, 1, 4, 2, 3, 0]
cropmatterenglish = [ "All white rice starts to brown. White rice is just brown rice that's been rid of its outer bran layer and polished. Rice plants grow to a height of 3 to 4 feet over an average of 120 days after planting. During this time, farmers irrigate the rice fields using the method that best fits that field or farm.","Maize, also known as corn, is a cereal grain first domesticated by indigenous peoples in southern Mexico about 10,000 years ago. Maize can take from 60 to 100 days to reach harvest depending upon plant variety and the amount of heat during the growing season.","Eating Chickpeas Regularly Can Lower Your Bad Cholesterol. The chickpea or garbanzo bean is a cool-season annual that requires about 100 days to reach harvest.  ","Kidney beans are an excellent plant-based source of protein. These beans may aid weight loss, promote colon health, and moderate blood sugar levels. Kidney Beans are ready to harvest within about 100 to 140 days.","Pigeon peas are most nutritious and easy to digest in their green stage, just before they become dry and lose their color. Pigeon peas Plants will germinate in 10 to 15 days & pods will appear in 4 months.","Moth beans contain calcium which is the mineral vital for maintaining stronger bones and preventing the risk of osteoporosis. Moth beans take 75 to 90 days to mature, and they are frequently planted at the end of the rainy season.","The major health benefit of the mung beans or green gram is their rich source of cholesterol reducing fibre. Mung beans are a warm-season crop and take between 90-120 days to mature.","It is one of the important pulse crops grown throughout India. Generally it is consumed in the form of ‘Dal’. It is the chief constituent of ‘papad, idli and dosa’. It takes around 70-75 days duration & its production will be around 10-12 days.","Lentils are rich in fibre, folate and potassium making them a great choice for the heart and for managing blood pressure and cholesterol. Lentils require 80 to 110 days to come to harvest.","The word pomegranate means apple with many seeds. Pomegranates are native to the Middle East. They belong to the berry family & are classified as a super fruit. Pomegranate trees can take up to 7 months for their fruit to fully mature. The tree itself will only bear fruit after two to three years of hearty growth.","About 5.6 million hectares of land are used for banana production around the globe. Bananas generally take four to six months for fruit to reach full size after flowering, depending on temperature, variety, moisture and culture practices.","Mangos are also rich in vitamin C, which is important for forming blood vessels and healthy collagen, as well as helping you heal. A mango tree requires 5-8 years before it will bear fruit; a nursery sapling should produce fruit in about four years. The mango fruit takes three to five months to ripen after the tree has flowered.","A grape is still defined as a type of berry in botanical terms. This means that each fruit comes from a single flower on the grapevine. Grape plant begins to grow 10-15 days after planting. ","August 3 is National Watermelon Day, & throughout summer, the backyard mainstay is added to drinks and served as dessert at barbecues across the country. Watermelons require 80-90 days from seed sowing to grow a full-size watermelon. Some smaller-sized watermelons (like Sugar Baby) can reach maturity in closer to 70 days.","Muskmelon has high fiber and water content, which makes it a great natural healer for people suffering from indigestion, constipation, and other digestive system issues. Muskmelon fruits take 35 to 45 days to ripen after the flower has been pollinated.","Apples are 25'%' air. Apples float in water because a whopping 25'%' of their volume is actually air. Apples are less dense than water, making them the perfect fruit for apple bobbing. Standard or full-sized apple trees can grow up to 30 feet tall and can take six years to bear their first fruit.","Oranges are the largest citrus fruit in the world. Orange juice is the most popular fruit juice in America. It can take 3-5 years for an orange tree to produce fruit, depending on how old the tree is when purchasing. Once the tree finally begins producing fruit, they take 7 to 8 months to ripen.","The papaya is botanically a berry. It may look like it grows from a tree, but the papaya is actually the fruit of an herb. It takes 6-12 months to grow papaya from seed to fruit.","On average a coconut tree produces 30 fruits each year, but a tree can produce up to 75 coconuts per year with optimal weather conditions, which is rare. About 61 million tons of coconuts are produced each year. The coconut tree grows from a single seed, which is an entire coconut, taking between 3 and 8 years to bear fruit, and living between 60 and 100 years.","Cotton is one of the most important fiber and cash crops of India and plays a dominant role in the industrial and agricultural economy of the country. It provides the basic raw material (cotton fibre) to the cotton textile industry. Cotton is fully mature and ready for harvesting approximately 160 days after being planted. Once the bolls have burst open, the farmers can prepare the cotton plants for harvesting.","Jute is the second most important vegetable fiber after cotton due to its versatility. Jute is used chiefly to make cloth for wrapping bales of raw cotton, and to make sacks and coarse cloth.  To grow jute, farmers scatter the seeds on cultivated soil. When the plants are about 15–20 cm tall, they are thinned out. About 4 months after planting, harvesting begins.","Coffee is consumed in great quantities, it is the world’s 2nd largest traded commodity, surpassed only by crude oil. Depending on the variety, it will take approximately 3 to 4 years for the newly planted coffee trees to bear fruit."]
@app.route('/')
def home():
    return render_template('login.html')



def cropfertpred(cl,fl):
    prediction1 = model.predict([cl])
    output1 = round(prediction1[0], 2)
    crpn = cropl[p1.index(output1)] + ".jpg"
    prediction2 = model2.predict([fl])
    output2 = round(prediction2[0], 2)
    fern = fertl[p2.index(output2)] + ".png"
    ol1 = cropl.index(cropl[p1.index(output1)])
    ol2 = fertl.index(fertl[p2.index(output2)])
    return crpn, fern, cropl[p1.index(output1)], fertl[p2.index(output2)], ol1, ol2

@app.route('/table')
def table():
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
    predv = cropfertpred(cl,fl)
    return render_template('table.html',nl=nl,pl=pl,kl=kl,templ=templ,huml=huml,moistl=moistl,phl=phl, predv = predv, cropeng=cropmatterenglish )

@app.route('/predplot')
def predplot():
    return render_template('check.html')


@app.route('/loginto',methods=['POST'])
def loginto():
    features = [x for x in request.form.values()]
    usern = features[0]
    passw =features[1]
    if usern == "9014361324" and passw== "farmer123":
        return render_template('indexmine.html')
    else:
        return render_template('login.html', prediction_text="Invalid username and password")





if __name__ == "__main__":
    app.run(debug=False)
