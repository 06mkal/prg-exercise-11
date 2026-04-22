class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, hledane_score):
        seznam_indexu = []
        for index, score in enumerate(self.scores):
            if score == hledane_score:
                seznam_indexu.append(index)
        return seznam_indexu

    def get_sorted(self):
        scores = list(self.scores)
        for j in range(len(scores)):
            for i in range(len(scores) - 1):
                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]

        return (scores)


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    count = len(results)
    for index, score in enumerate(results):




if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny