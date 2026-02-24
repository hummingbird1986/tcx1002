def calc_gpa(input):
    if input ==[]:
        return (0.0, 0)
    input=input.copy()
    def total_grade_mc(input, grade_sum=0.0, mc_sum=0):
        score_ = input[0][2]
        mc_=input[0][1]
        grade_=convert_grade(score_)
        grade_total=grade_*mc_
        grade_sum+=grade_total
        mc_sum+=mc_
        gpa=round(grade_sum/mc_sum,1)
        # print(list)
        if input[1:]:
           return total_grade_mc(input[1:],grade_sum, mc_sum)
        else:
           return gpa, mc_sum
    return total_grade_mc(input)
    

def convert_grade(score):
    grade_point = {
        "A+": 5.0,
        "A": 5.0,
        "A-": 4.5,
        "B+": 4.0,
        "B": 3.5,
        "B-": 3.0,
        "C+": 2.5,
        "C": 2.0,
        "D+": 1.5,
        "D": 1.0,
        "F": 0.0
    }
    grade=float(grade_point[score])
    return grade

print(calc_gpa([('TCX1001', 4, 'A-'), ('TCX1002', 4, 'B+'), ('TCX1003', 2, 'A')]))