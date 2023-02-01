class Grading:

    def __init__(self):
        self.score = 0
        self.grades = []
        self.onegrades = []
        self.twogrades = []
        self.threegrades = []
        self.one_units = []
        self.two_units = []
        self.three_units = []

    def collect_ones(self, *args):
        for i in args:
            a = int(i)
            self.one_units.append(a)

    def collect_twos(self, *args):
        for i in args:
            a = int(i)
            self.one_units.append(a)

    def collect_threes(self, *args):
        for i in args:
            a = int(i)
            self.one_units.append(a)

    def grade_points(self, *args):
        for i in args:
            if i >= 75:
                Grade = 5
                self.grades.append(Grade)
            elif i >= 60:
                Grade = 4
                self.grades.append(Grade)
            elif i >= 50:
                Grade = 3
                self.grades.append(Grade)
            elif i >= 40:
                Grade = 2
                self.grades.append(Grade)
            elif i >= 30:
                Grade = 1
                self.grades.append(Grade)
            elif i >= 0:
                Grade = 0
                self.grades.append(Grade)

    def grade_pointsno(self, *args):
        for i in args:
            if i >= 75:
                Grade = 5
                return Grade
            elif i >= 60:
                Grade = 4
                return Grade
            elif i >= 50:
                Grade = 3
                return Grade
            elif i >= 40:
                Grade = 2
                return Grade
            elif i >= 30:
                Grade = 1
                return Grade
            elif i >= 0:
                Grade = 0
                return Grade
