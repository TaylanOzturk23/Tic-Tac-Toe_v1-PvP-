from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import ttt_ui
import sys

class window(QMainWindow,ttt_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.msgbox = QMessageBox
        self.bot_right_block = self.bot_left_block_2
        self.player1_score = "0"
        self.player2_score = "0"
        self.label_4.setText(self.player1_score)
        self.label_6.setText(self.player2_score)
        self.table = [
            [self.left_top_block, self.top_middle_block, self.top_right_block],          # row 1
            [self.middle_left_block, self.middle_middle_block, self.middle_right_block], # row 2
            [self.bot_left_block, self.bot_middle_block, self.bot_right_block]           # row 3
        ]
       
        self.Reset_Scores.pressed.connect(self.resetting_scores)
        # # # # top

        self.table[0][0].textChanged.connect(self.control1)
        self.table[0][1].textChanged.connect(self.control2)
        self.table[0][2].textChanged.connect(self.control3)
        self.table[0][0].textEdited.connect(self.playing1)
        self.table[0][0].textEdited.connect(self.bot_to_top) #   second connection
        self.table[0][1].textEdited.connect(self.playing1)
        self.table[0][1].textEdited.connect(self.bot_to_top2) # third connection
        self.table[0][2].textEdited.connect(self.playing1)
        self.table[0][2].textEdited.connect(self.bot_to_top3) # forth connection
        
        # cross connection
        self.table[0][2].textEdited.connect(self.cross) 
        self.table[0][0].textEdited.connect(self.cross2)
        
        # cluster connection
        self.table[0][0].textEdited.connect(self.draw)
        self.table[0][1].textEdited.connect(self.draw)
        self.table[0][2].textEdited.connect(self.draw)
        
        
        
        
        # # # # middle
        
        self.table[1][0].textChanged.connect(self.control4)
        self.table[1][1].textChanged.connect(self.control5)
        self.table[1][2].textChanged.connect(self.control6)
        self.table[1][0].textEdited.connect(self.playing2) 
        self.table[1][0].textEdited.connect(self.bot_to_top) # second connection
        self.table[1][1].textEdited.connect(self.playing2)
        self.table[1][1].textEdited.connect(self.bot_to_top2) # third connection
        self.table[1][2].textEdited.connect(self.playing2)
        self.table[1][2].textEdited.connect(self.bot_to_top3) # forth  connection
        
         # cross connection
        self.table[1][1].textEdited.connect(self.cross)
        self.table[1][1].textEdited.connect(self.cross2)
        
        # cluster connection
        self.table[1][0].textEdited.connect(self.draw)
        self.table[1][1].textEdited.connect(self.draw)
        self.table[1][2].textEdited.connect(self.draw)
        
        
        
        
        # # # # bottom
        
        self.table[2][0].textChanged.connect(self.control7)
        self.table[2][1].textChanged.connect(self.control8)
        self.table[2][2].textChanged.connect(self.control9)
        self.table[2][0].textEdited.connect(self.playing3)
        self.table[2][0].textEdited.connect(self.bot_to_top) # second connection
        self.table[2][1].textEdited.connect(self.playing3)
        self.table[2][1].textEdited.connect(self.bot_to_top2) # third connection
        self.table[2][2].textEdited.connect(self.playing3)
        self.table[2][2].textEdited.connect(self.bot_to_top3) # forth connection
        
         # cross connection
        self.table[2][0].textEdited.connect(self.cross)
        self.table[2][2].textEdited.connect(self.cross2)
        
        # Cluster Connection
        self.table[2][0].textEdited.connect(self.draw)
        self.table[2][1].textEdited.connect(self.draw)
        self.table[2][2].textEdited.connect(self.draw)
        
      
    
    
    def resetting_scores(self):
        self.player1_score = "0"
        self.label_4.setText(self.player1_score)
        
        self.player2_score = "0"
        self.label_6.setText(self.player2_score)
    
            
    
    
    def draw(self):
        if (
            self.table[0][0].text() != "" and self.table[0][1].text() != "" and 
            self.table[0][2].text() != "" and self.table[1][0].text() != "" and 
            self.table[1][1].text() != "" and self.table[1][2].text() != "" and 
            self.table[2][0].text() != "" and self.table[2][1].text() != "" and 
            self.table[2][2].text() != ""
        ):
            self.messagebox_scoreless()
    
    
    def messagebox_player1(self):
        
        self.msgbox.setStyleSheet(self,"QMessageBox{font-size:20px; background-color:rgb(168, 188, 254)}")
        self.msgbox.information(self,"Birinci Oyuncu (X) Kazandı !",
                                    "Bloklarınız silindi. Tekrar oynayabilirsiniz !")
        self.table[0][0].clear()
        self.table[0][1].clear()
        self.table[0][2].clear()
            
        self.table[1][0].clear()
        self.table[1][1].clear()
        self.table[1][2].clear()
            
        self.table[2][0].clear()
        self.table[2][1].clear()
        self.table[2][2].clear()
        
        f = int(self.player1_score) + 1
        self.player1_score = str(f)
        self.label_4.setText(self.player1_score)
        
        
        
    def messagebox_player2(self):
        self.msgbox.setStyleSheet(self,"QMessageBox{font-size:20px; background-color:rgb(168, 188, 254)}")
        self.msgbox.information(self,"İkinci Oyuncu (O) Kazandı !",
                                    "Bloklarınız silindi. Tekrar oynayabilirsiniz !")
        self.table[0][0].clear()
        self.table[0][1].clear()
        self.table[0][2].clear()
            
        self.table[1][0].clear()
        self.table[1][1].clear()
        self.table[1][2].clear()
            
        self.table[2][0].clear()
        self.table[2][1].clear()
        self.table[2][2].clear()
        
        t = int(self.player2_score) + 1
        self.player2_score = str(t)
        self.label_6.setText(self.player2_score)
        
        
    def messagebox_scoreless(self):
        self.msgbox.setStyleSheet(self,"QMessageBox{font-size:20px; background-color:rgb(168, 188, 254)}")
        self.msgbox.information(self,"BERABERE !",
                                    "Bloklarınız silindi. Tekrar oynayabilirsiniz !")
        self.table[0][0].clear()
        self.table[0][1].clear()
        self.table[0][2].clear()
            
        self.table[1][0].clear()
        self.table[1][1].clear()
        self.table[1][2].clear()
            
        self.table[2][0].clear()
        self.table[2][1].clear()
        self.table[2][2].clear()
        
        
        q = int(self.player1_score) + 1
        self.player1_score = str(q)
        
        u = int(self.player2_score) + 1
        self.player2_score = str(u)
        
        self.label_4.setText(self.player1_score)
        self.label_6.setText(self.player2_score)
        
    
    
    
    
    
    
    def cross2(self):
        if (
            self.table[0][0].text() == "X" and self.table[1][1].text() == "X" and
            self.table[2][2].text() == "X"
        ):
            self.messagebox_player1()
            
        elif (
            self.table[0][0].text() == "O" and self.table[1][1].text() == "O" and
            self.table[2][2].text() == "O"
        ):
            self.messagebox_player2()
    
    
    
    
    
    def cross(self):
        if (
            self.table[0][2].text() == "X" and self.table[1][1].text() == "X" and
            self.table[2][0].text() == "X"
        ):
            self.messagebox_player1()
        
        elif (
            self.table[0][2].text() == "O" and self.table[1][1].text() == "O" and
            self.table[2][0].text() == "O"
        ):
            self.messagebox_player2()
    
    
     
    def bot_to_top3(self):
        if (
            self.table[0][2].text() == "X" and self.table[1][2].text() == "X" and
            self.table[2][2].text() == "X"
        ):
            
            self.messagebox_player1()
            
        elif (
            self.table[0][2].text() == "O" and self.table[1][2].text() == "O" and
            self.table[2][2].text() == "O"
        ):
            self.messagebox_player2()
    
    
    
    
    def bot_to_top2(self):
        if (
            self.table[0][1].text() == "X" and self.table[1][1].text() == "X" and
            self.table[2][1].text() ==  "X"
        ):
            self.messagebox_player1()
            
        elif (
            self.table[0][1].text() == "O" and self.table[1][1].text() == "O" and
            self.table[2][1].text() ==  "O"
        ):
            self.messagebox_player2()
    
        
    def bot_to_top(self):
        if (
           self.table[0][0].text() == "X" and self.table[1][0].text() == "X"
           and self.table[2][0].text() == "X"
          
        ):
            self.messagebox_player1()
            
        elif(
            
            self.table[0][0].text() == "O" and self.table[1][0].text() == "O" and
            self.table[2][0].text() == "O"
        ):
            self.messagebox_player2()
        
        
    def playing1(self):
        if (
            self.table[0][0].text() == "X" and self.table[0][1].text() == "X"
            and self.table[0][2].text() == "X"
         
   
        ):
            self.messagebox_player1()
            
        elif(
            self.table[0][0].text() == "O" and self.table[0][1].text() == "O"
            and self.table[0][2].text() == "O"
        ):
            self.messagebox_player2()
            
    def playing2(self):
        if (
            self.table[1][0].text() == "X" and self.table[1][1].text() == "X"
            and self.table[1][2].text() == "X"     
        ):
            self.messagebox_player1()
            
        elif (
            self.table[1][0].text() == "O" and self.table[1][1].text() == "O"
            and self.table[1][2].text() == "O"  
            
        ):
           
            self.messagebox_player2()
            
           
            
       

    def playing3(self):
        
        if (
            self.table[2][0].text() == "X" and self.table[2][1].text() == "X"
            and self.table[2][2].text() == "X" 
        ):
            self.messagebox_player1()
            
        elif (
            self.table[2][0].text() == "O" and self.table[2][1].text() == "O"
            and self.table[2][2].text() == "O"
        ):
            self.messagebox_player2()
        
            
            
        
        
    
    
        
            
        
        
    def control1 (self):
       
        if self.table[0][0].text() != "X" and self.table[0][0].text() != "O":
            self.table[0][0].clear()
        

        
    def control2 (self):
        if self.table[0][1].text() != "X" and self.table[0][1].text() != "O":
            self.table[0][1].clear()
            
    def control3 (self):
       
        if self.table[0][2].text() != "X" and self.table[0][2].text() != "O":
            self.table[0][2].clear()
            
            
            
            
            
    def control4 (self):
        if self.table[1][0].text() != "X" and self.table[1][0].text() != "O":
            self.table[1][0].clear()
            
    def control5 (self):
       
        if self.table[1][1].text() != "X" and self.table[1][1].text() != "O":
            self.table[1][1].clear()
            
    def control6 (self):
        if self.table[1][2].text() != "X" and self.table[1][2].text() != "O":
            self.table[1][2].clear()
            
            
            
            
            
    def control7 (self):
       
        if self.table[2][0].text() != "X" and self.table[2][0].text() != "O":
            self.table[2][0].clear()
            
    def control8 (self):
        if self.table[2][1].text() != "X" and self.table[2][1].text() != "O":
            self.table[2][1].clear()
            
    def control9 (self):
       
        if self.table[2][2].text() != "X" and self.table[2][2].text() != "O":
            self.table[2][2].clear()
            
  
        
        
app = QApplication(sys.argv)
pencere = window()
pencere.setWindowTitle("Tic Tac Toe")
pencere.show()
sys.exit(app.exec_())
        
    
    
