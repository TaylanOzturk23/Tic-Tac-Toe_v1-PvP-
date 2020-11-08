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
        
       
        self.Reset_Scores.pressed.connect(self.resetting_scores)
        # # # # top

        self.left_top_block.textChanged.connect(self.control1)
        self.top_middle_block.textChanged.connect(self.control2)
        self.top_right_block.textChanged.connect(self.control3)
        self.left_top_block.textEdited.connect(self.playing1)
        self.left_top_block.textEdited.connect(self.bot_to_top) #   second connection
        self.top_middle_block.textEdited.connect(self.playing1)
        self.top_middle_block.textEdited.connect(self.bot_to_top2) # third connection
        self.top_right_block.textEdited.connect(self.playing1)
        self.top_right_block.textEdited.connect(self.bot_to_top3) # forth connection
        
        # cross connection
        self.top_right_block.textEdited.connect(self.cross) 
        self.left_top_block.textEdited.connect(self.cross2)
        
        # cluster connection
        self.left_top_block.textEdited.connect(self.draw)
        self.top_middle_block.textEdited.connect(self.draw)
        self.top_right_block.textEdited.connect(self.draw)
        
        
        
        
        # # # # middle
        
        self.middle_left_block.textChanged.connect(self.control4)
        self.middle_middle_block.textChanged.connect(self.control5)
        self.middle_right_block.textChanged.connect(self.control6)
        self.middle_left_block.textEdited.connect(self.playing2) 
        self.middle_left_block.textEdited.connect(self.bot_to_top) # second connection
        self.middle_middle_block.textEdited.connect(self.playing2)
        self.middle_middle_block.textEdited.connect(self.bot_to_top2) # third connection
        self.middle_right_block.textEdited.connect(self.playing2)
        self.middle_right_block.textEdited.connect(self.bot_to_top3) # forth  connection
        
         # cross connection
        self.middle_middle_block.textEdited.connect(self.cross)
        self.middle_middle_block.textEdited.connect(self.cross2)
        
        # cluster connection
        self.middle_left_block.textEdited.connect(self.draw)
        self.middle_middle_block.textEdited.connect(self.draw)
        self.middle_right_block.textEdited.connect(self.draw)
        
        
        
        
        # # # # bottom
        
        self.bot_left_block.textChanged.connect(self.control7)
        self.bot_middle_block.textChanged.connect(self.control8)
        self.bot_right_block.textChanged.connect(self.control9)
        self.bot_left_block.textEdited.connect(self.playing3)
        self.bot_left_block.textEdited.connect(self.bot_to_top) # second connection
        self.bot_middle_block.textEdited.connect(self.playing3)
        self.bot_middle_block.textEdited.connect(self.bot_to_top2) # third connection
        self.bot_right_block.textEdited.connect(self.playing3)
        self.bot_right_block.textEdited.connect(self.bot_to_top3) # forth connection
        
         # cross connection
        self.bot_left_block.textEdited.connect(self.cross)
        self.bot_right_block.textEdited.connect(self.cross2)
        
        # Cluster Connection
        self.bot_left_block.textEdited.connect(self.draw)
        self.bot_middle_block.textEdited.connect(self.draw)
        self.bot_right_block.textEdited.connect(self.draw)
        
      
    
    
    def resetting_scores(self):
        self.player1_score = "0"
        self.label_4.setText(self.player1_score)
        
        self.player2_score = "0"
        self.label_6.setText(self.player2_score)
    
            
    
    
    def draw(self):
        if (
            self.left_top_block.text() != "" and self.top_middle_block.text() != "" and 
            self.top_right_block.text() != "" and self.middle_left_block.text() != "" and 
            self.middle_middle_block.text() != "" and self.middle_right_block.text() != "" and 
            self.bot_left_block.text() != "" and self.bot_middle_block.text() != "" and 
            self.bot_right_block.text() != ""
        ):
            self.messagebox_scoreless()
    
    
    def messagebox_player1(self):
        
        self.msgbox.setStyleSheet(self,"QMessageBox{font-size:20px; background-color:rgb(168, 188, 254)}")
        self.msgbox.information(self,"Birinci Oyuncu (X) Kazandı !",
                                    "Bloklarınız silindi. Tekrar oynayabilirsiniz !")
        self.left_top_block.clear()
        self.top_middle_block.clear()
        self.top_right_block.clear()
            
        self.middle_left_block.clear()
        self.middle_middle_block.clear()
        self.middle_right_block.clear()
            
        self.bot_left_block.clear()
        self.bot_middle_block.clear()
        self.bot_right_block.clear()
        
        f = int(self.player1_score) + 1
        self.player1_score = str(f)
        self.label_4.setText(self.player1_score)
        
        
        
    def messagebox_player2(self):
        self.msgbox.setStyleSheet(self,"QMessageBox{font-size:20px; background-color:rgb(168, 188, 254)}")
        self.msgbox.information(self,"İkinci Oyuncu (O) Kazandı !",
                                    "Bloklarınız silindi. Tekrar oynayabilirsiniz !")
        self.left_top_block.clear()
        self.top_middle_block.clear()
        self.top_right_block.clear()
            
        self.middle_left_block.clear()
        self.middle_middle_block.clear()
        self.middle_right_block.clear()
            
        self.bot_left_block.clear()
        self.bot_middle_block.clear()
        self.bot_right_block.clear()
        
        t = int(self.player2_score) + 1
        self.player2_score = str(t)
        self.label_6.setText(self.player2_score)
        
        
    def messagebox_scoreless(self):
        self.msgbox.setStyleSheet(self,"QMessageBox{font-size:20px; background-color:rgb(168, 188, 254)}")
        self.msgbox.information(self,"BERABERE !",
                                    "Bloklarınız silindi. Tekrar oynayabilirsiniz !")
        self.left_top_block.clear()
        self.top_middle_block.clear()
        self.top_right_block.clear()
            
        self.middle_left_block.clear()
        self.middle_middle_block.clear()
        self.middle_right_block.clear()
            
        self.bot_left_block.clear()
        self.bot_middle_block.clear()
        self.bot_right_block.clear()
        
        
        q = int(self.player1_score) + 1
        self.player1_score = str(q)
        
        u = int(self.player2_score) + 1
        self.player2_score = str(u)
        
        self.label_4.setText(self.player1_score)
        self.label_6.setText(self.player2_score)
        
    
    
    
    
    
    
    def cross2(self):
        if (
            self.left_top_block.text() == "X" and self.middle_middle_block.text() == "X" and
            self.bot_right_block.text() == "X"
        ):
            self.messagebox_player1()
            
        elif (
            self.left_top_block.text() == "O" and self.middle_middle_block.text() == "O" and
            self.bot_right_block.text() == "O"
        ):
            self.messagebox_player2()
    
    
    
    
    
    def cross(self):
        if (
            self.top_right_block.text() == "X" and self.middle_middle_block.text() == "X" and
            self.bot_left_block.text() == "X"
        ):
            self.messagebox_player1()
        
        elif (
            self.top_right_block.text() == "O" and self.middle_middle_block.text() == "O" and
            self.bot_left_block.text() == "O"
        ):
            self.messagebox_player2()
    
    
     
    def bot_to_top3(self):
        if (
            self.top_right_block.text() == "X" and self.middle_right_block.text() == "X" and
            self.bot_right_block.text() == "X"
        ):
            
            self.messagebox_player1()
            
        elif (
            self.top_right_block.text() == "O" and self.middle_right_block.text() == "O" and
            self.bot_right_block.text() == "O"
        ):
            self.messagebox_player2()
    
    
    
    
    def bot_to_top2(self):
        if (
            self.top_middle_block.text() == "X" and self.middle_middle_block.text() == "X" and
            self.bot_middle_block.text() ==  "X"
        ):
            self.messagebox_player1()
            
        elif (
            self.top_middle_block.text() == "O" and self.middle_middle_block.text() == "O" and
            self.bot_middle_block.text() ==  "O"
        ):
            self.messagebox_player2()
    
        
    def bot_to_top(self):
        if (
           self.left_top_block.text() == "X" and self.middle_left_block.text() == "X"
           and self.bot_left_block.text() == "X"
          
        ):
            self.messagebox_player1()
            
        elif(
            
            self.left_top_block.text() == "O" and self.middle_left_block.text() == "O" and
            self.bot_left_block.text() == "O"
        ):
            self.messagebox_player2()
        
        
    def playing1(self):
        if (
            self.left_top_block.text() == "X" and self.top_middle_block.text() == "X"
            and self.top_right_block.text() == "X"
         
   
        ):
            self.messagebox_player1()
            
        elif(
            self.left_top_block.text() == "O" and self.top_middle_block.text() == "O"
            and self.top_right_block.text() == "O"
        ):
            self.messagebox_player2()
            
    def playing2(self):
        if (
            self.middle_left_block.text() == "X" and self.middle_middle_block.text() == "X"
            and self.middle_right_block.text() == "X"     
        ):
            self.messagebox_player1()
            
        elif (
            self.middle_left_block.text() == "O" and self.middle_middle_block.text() == "O"
            and self.middle_right_block.text() == "O"  
            
        ):
           
            self.messagebox_player2()
            
           
            
       

    def playing3(self):
        
        if (
            self.bot_left_block.text() == "X" and self.bot_middle_block.text() == "X"
            and self.bot_right_block.text() == "X" 
        ):
            self.messagebox_player1()
            
        elif (
            self.bot_left_block.text() == "O" and self.bot_middle_block.text() == "O"
            and self.bot_right_block.text() == "O"
        ):
            self.messagebox_player2()
        
            
            
        
        
    
    
        
            
        
        
    def control1 (self):
       
        if self.left_top_block.text() != "X" and self.left_top_block.text() != "O":
            self.left_top_block.clear()
        

        
    def control2 (self):
        if self.top_middle_block.text() != "X" and self.top_middle_block.text() != "O":
            self.top_middle_block.clear()
            
    def control3 (self):
       
        if self.top_right_block.text() != "X" and self.top_right_block.text() != "O":
            self.top_right_block.clear()
            
            
            
            
            
    def control4 (self):
        if self.middle_left_block.text() != "X" and self.middle_left_block.text() != "O":
            self.middle_left_block.clear()
            
    def control5 (self):
       
        if self.middle_middle_block.text() != "X" and self.middle_middle_block.text() != "O":
            self.middle_middle_block.clear()
            
    def control6 (self):
        if self.middle_right_block.text() != "X" and self.middle_right_block.text() != "O":
            self.middle_right_block.clear()
            
            
            
            
            
    def control7 (self):
       
        if self.bot_left_block.text() != "X" and self.bot_left_block.text() != "O":
            self.bot_left_block.clear()
            
    def control8 (self):
        if self.bot_middle_block.text() != "X" and self.bot_middle_block.text() != "O":
            self.bot_middle_block.clear()
            
    def control9 (self):
       
        if self.bot_right_block.text() != "X" and self.bot_right_block.text() != "O":
            self.bot_right_block.clear()
            
  
        
        
app = QApplication(sys.argv)
pencere = window()
pencere.setWindowTitle("Tic Tac Toe")
pencere.show()
sys.exit(app.exec_())
        
    
    