class STudent:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alife = True

        def to_study(self):
            print("Time to study!")
            self.gladness -= 5
            self.progress += 0.12

        def to_sleep(self):
            print("TIME TO SLEEEEEEEEEEEEEEEEEEEEEP!")
            self.gladness += 3

        def to_chill(self):
            print("Time to  chilling")
            self.gladness += 5
            self.progress -= 0.1

def end_of_day(self):
    print("========== Congrutulate day done ======= \n")

    print(f"Gladness ={self.gladness}")
    print(f"progress ={self.progress}")

    def is_alive(self):
        if self.progress < - 0.5:
            print("No cash ........")
            self.alive = False

        elif self.gladness < 0:
            print("Depression no")


student_Maksim = STudent("Maksim")