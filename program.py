from turtle import delay
from PyQt6 import QtWidgets, QtGui, QtCore

import sys
import time
import random


class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Pasare")
        self.setFixedSize(800,580)
        self.pozitie_curenta = 220
        self.viteza = 0
        self.isrunning = False
        self.stalp_miscat = 1000
        self.stalp_miscat_2 = 1500
        self.score = 0

        self.fundal = QtWidgets.QLabel(self)
        self.fundal.setScaledContents(True)
        self.fundal.resize(800, 600)
        fundal_pix_map = QtGui.QPixmap("fundal.jpeg")
        self.fundal.setPixmap(fundal_pix_map)

        self.stalp1 = tunel(self)
        self.stalp1.random_shape()
        self.stalp1.move(self.stalp_miscat, 0)

        self.stalp2 = tunel(self)
        self.stalp2.random_shape()
        self.stalp2.move(self.stalp_miscat_2, 0)


        self.pasare = QtWidgets.QLabel(self)
        self.pasare.move(40, self.pozitie_curenta)
        self.pasare.setScaledContents(True)
        self.pasare.resize(50, 50)
        pasare_pix_map = QtGui.QPixmap("pasare.gif")
        self.pasare.setPixmap(pasare_pix_map)

        self.timer = QtCore.QTimer() 
        self.timer.timeout.connect(self.miscare_pasare)
        

        self.mesaj = QtWidgets.QLabel("Press Space to start the game",self ) 
        self.mesaj.move(350,290)

        self.score_label = QtWidgets.QLabel("Scor: 0",self )
        self.score_label.move(700, 560)
        self.score_label.resize(100, 20)


    def miscare_pasare(self):   
        self.viteza += 0.7 
        self.pozitie_curenta += self.viteza 
        self.pasare.move(40, self.pozitie_curenta) 

        self.stalp_miscat -= 10
        self.stalp1.move(self.stalp_miscat, 0)

        if  self.stalp_miscat > - 60 and self.stalp_miscat < 90:
            if self.pozitie_curenta < self.stalp1.pct_sus() or self.pozitie_curenta > self.stalp1.pct_jos():
                self.timer.stop()
                self.mesaj.setText("Game over!")
                self.mesaj.show()

        if self.stalp_miscat < -100:
            self.score += 1
            self.score_label.setText(f'Scor:{self.score}')
            self.stalp_miscat = 1000
            self.stalp1.move(self.stalp_miscat, 0)
            self.stalp1.random_shape()
        
        self.stalp_miscat_2 -= 10
        self.stalp2.move(self.stalp_miscat_2, 0)

        if  self.stalp_miscat_2 > - 60 and self.stalp_miscat_2 < 90:
            if self.pozitie_curenta < self.stalp2.pct_sus() or self.pozitie_curenta > self.stalp2.pct_jos():
                self.timer.stop()
                self.mesaj.setText("Game over!")
                self.mesaj.show()

        if self.stalp_miscat_2 < -100:
            self.score += 1
            self.score_label.setText(f'Scor:{self.score}')
            self.stalp_miscat_2 = 1000
            self.stalp2.move(self.stalp_miscat_2, 0)
            self.stalp2.random_shape()
        

        if self.pozitie_curenta > 450:
            self.timer.stop()
            self.mesaj.setText("Game over!")
            self.mesaj.show()
            
            


    def keyPressEvent(self, event): 
        if event.key() == QtCore.Qt.Key.Key_Space:
            if self.isrunning == False:
                self.isrunning = True
                self.mesaj.hide()
                self.timer.start(25)
            self.viteza = -9 
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.timer.stop()
            self.mesaj.setText("Game over!")
            self.mesaj.show()
        
    

class tunel(QtWidgets.QWidget):
    def __init__(self, window = None):
        super().__init__(window) 
        self.setWindowTitle("tunel")
        self.max_size = 499
        self.setFixedSize(100,self.max_size)
        self.center = 0
        self.distance = 100


        self.trunchi_jos = QtWidgets.QLabel(self)
        self.trunchi_jos.move(0,400)
        self.trunchi_jos.setScaledContents(True)
        self.trunchi_jos.resize(100, 100) 
        trunchi_jos_pix_map = QtGui.QPixmap("corp_tunel.png")
        self.trunchi_jos.setPixmap(trunchi_jos_pix_map)

        self.trunchi_sus = QtWidgets.QLabel(self)
        self.trunchi_sus.move(0,0)
        self.trunchi_sus.setScaledContents(True)
        self.trunchi_sus.resize(100, 100)
        trunchi_sus_180_pix_map = QtGui.QPixmap("corp_tunel.png")
        self.trunchi_sus.setPixmap(trunchi_sus_180_pix_map)

        self.cap_tunel_sus = QtWidgets.QLabel(self)
        self.cap_tunel_sus.setScaledContents(True)
        self.cap_tunel_sus.resize(100, 40)
        self.cap_tunel_sus_pix_map = QtGui.QPixmap("cap_tunel.png")
        self.cap_tunel_sus.setPixmap(self.cap_tunel_sus_pix_map)

        self.cap_tunel_jos = QtWidgets.QLabel(self)
        self.cap_tunel_jos.setScaledContents(True)
        self.cap_tunel_jos.resize(100, 40)
        self.cap_tunel_jos_pix_map = QtGui.QPixmap("cap_tunel.png")
        self.cap_tunel_jos.setPixmap(self.cap_tunel_jos_pix_map)


    def pct_sus(self):
        return self.center - self.distance/2 - 10


    def pct_jos(self):
        return self.center + self.distance/2 - 30


    def update_shape(self, center):
        self.center = center
        trunchi_sus_dimension = self.center - self.distance/2 - 40
        self.trunchi_sus.resize(100, trunchi_sus_dimension)
        self.cap_tunel_sus.move(0, trunchi_sus_dimension)

        trunchi_jos_dimension = self.center + self.distance/2 + 40
        self.trunchi_jos.resize(100, self.max_size - trunchi_jos_dimension)
        self.trunchi_jos.move(0, trunchi_jos_dimension)
        self.cap_tunel_jos.move(0, self.center + self.distance/2)

    def random_shape(self):
        ##minim 60 maxim 380
        x = random.random()
        pozitie = 320 * x + 60
        self.update_shape(pozitie)



        

app = QtWidgets.QApplication(sys.argv) 

w1 = window()
w1.show()

#w2 = widow_1()
#w2.show()
#w2.random_shape()
print("se va apela exec")
app.exec()
print("exec s-a terminat de apelat")


