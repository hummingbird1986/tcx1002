import math

def get_deans_list(Sem2_results):
    def calc_gpa(letters):
        gp = {'A+':5.0, 'A':5.0, 'A-':4.5, 'B+':4.0, 'B':3.5, 'B-':3.0, 'C+':2.5,
              'C':2.0, 'D+':1.5, 'D':1.0, 'F':0.0}
        points = [gp[x] for x in letters]
        return sum(points)/len(points)

    eligibles = [s for s in Sem2_results if len(s)>=4]
    student_gpa = [(s[0], calc_gpa(s[1:])) for s in eligibles]
    student_gpa.sort(key=lambda x:-x[1])
    n = math.ceil(len(eligibles) * 0.2)

    # res = [s[0] for s in student_gpa[:n]]
    res = list(map(lambda x:x[0], student_gpa[:n]))
    for s in student_gpa[n:]:
        if s[1] == student_gpa[n-1][1]:
            res.append(s[0])
        else:
            break

    return res