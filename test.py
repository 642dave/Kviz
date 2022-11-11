class Robot:
    
    # constructor
    def __init__(self, baterie, delka_rukou):
        self.bat = baterie
        self.del_ruk = delka_rukou
        self.ukony_do_kontroly= 1000

    def krok_vpred(self):
        print("Robot udelal krok vpred")
        self.ukony_do_kontroly -= 1
        print(f"Ukonu do kontroly: { self.ukony_do_kontroly}") # atribut v metode

    def krok_vzad(self):
        print("Robot udelal krok vzad")
        self.ukony_do_kontroly -= 1
        print(f"Ukonu do kontroly: { self.ukony_do_kontroly}") # atribut v metode



robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(15, 0.8)
robot_4 = Robot(18, 0.4)

robot_1.krok_vpred()
robot_1.krok_vzad()
robot_1.krok_vpred()
robot_1.krok_vzad()
robot_1.krok_vpred()
robot_1.krok_vzad()
robot_1.krok_vpred()
robot_1.krok_vzad()
robot_1.krok_vpred()
robot_1.krok_vzad()





# commit atributy v metodach