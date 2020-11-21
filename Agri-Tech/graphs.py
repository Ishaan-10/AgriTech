import matplotlib.pyplot as p
def maitreyib():
          crp=["rice","wheat","ragi","barley"]
          yld=[1000,1000,440,560]
          p.bar(crp,yld,color='red')
          p.title("Maitreyi's Crops vs Average Yield")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def maitreyip():
          crp=["rice","wheat","ragi","barley"]
          area=[0.9,0.4,0.2,0.5]
          p.pie(area,labels=crp)
          p.title("Maitreyi's Crops per unit Land area")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def maitreyil():
          yr=[2020,2019,2018,2017,2016]
          yl=[3030,2700,2200,3100,3970]
          p.plot(yr,yl,color='red',marker='d')
          p.title("Maitreyi's Yield per Year")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()          

def shreyab():
          crp=["rice","wheat","jute","sugarcane"]
          yld=[1100,1400,300,700]
          p.bar(crp,yld,color='green')
          p.title("Shreya's Crops vs Average Yield")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def shreyap():
          crp=["rice","wheat","jute","sugarcane"]
          area=[1.1,0.8,0.6,0.5]
          p.pie(area,labels=crp)
          p.title("Shreya's Crops per unit Land area")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def shreyal():
          yr=[2020,2019,2018,2017,2016]
          yl=[3800,4000,2900,3300,3500]
          p.plot(yr,yl,color='green',marker='d')
          p.title("Shreya's Yield vs Year")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()          

def kartikb():
          crp=["wheat","cashew","bajra","jute"]
          yld=[700,600,400,300]
          p.bar(crp,yld,color='yellow')
          p.title("Kartik's Crops vs Average Yield")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def kartikp():
          crp=["wheat","cashew","bajra","jute"]
          area=[1,0.2,0.4,0.4]
          p.pie(area,labels=crp)
          p.title("Kartik's Crops per unit Land area")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def kartikl():
          yr=[2020,2019,2018,2017,2016]
          yl=[2200,2000,1700,1800,2300]
          p.plot(yr,yl,color='yellow',marker='d')
          p.title("Kartik's Yield vs Year")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()


def ishanb():
          crp=["cotton","jute","tea","coffee"]
          yld=[900,800,540,760]
          p.bar(crp,yld,color='blue')
          p.title("Ishan's Crops vs Average Yield")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def ishanp():
          crp=["cotton","jute","tea","coffee"]
          area=[1.3,1.1,0.8,0.8]
          p.pie(area,labels=crp)
          p.title("Ishan's Crops per unit Land area")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def ishanl():
          yr=[2020,2019,2018,2017,2016]
          yl=[4000,3000,2600,2400,3000]
          p.plot(yr,yl,color='blue',marker='d')
          p.title("Ishan's Yield vs Year")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()          

def chiragb():
          crp=["bajra","cotton","corn","rice"]
          yld=[1000,800,700,1300]
          p.bar(crp,yld,color='cyan')
          p.title("Chirag's Crops vs Average Yield")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def chiragp():
          crp=["bajra","cotton","corn","rice"]
          area=[1.7,1.2,0.7,0.5]
          p.pie(area,labels=crp)
          p.title("Chirag's Crops per unit Land area")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def chiragl():
          yr=[2020,2019,2018,2017,2016]
          yl=[3500,4200,3400,3600,4300]
          p.plot(yr,yl,color='cyan',marker='d')
          p.title("Chirag's Yield vs Year")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def gurditb():
          crp=["wheat","jowar","bajra","corn"]
          yld=[700,600,500,700]
          p.bar(crp,yld,color='white')
          p.title("Gurdit's Crops vs Average Yield")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def gurditp():
          crp=["wheat","jowar","bajra","corn"]
          area=[1,0.2,0.4,0.4]
          p.pie(area,labels=crp)
          p.title("Gurdit's Crops per unit Land area")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()

def gurditl():
          yr=[2020,2019,2018,2017,2016]
          yl=[1900,2800,2800,1900,3100]
          p.plot(yr,yl,color='white',marker='d')
          p.title("Gurdit's Yield vs Year")
          ax = p.gca()
          ax.set_facecolor('black')
          p.show()
