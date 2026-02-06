#prev_cap (float) 是之前的cap
#prev_mc (int):sem2 的 MC
#sem_results: ["ID1234A", ("A", 4), ("B", 4)]

this_sem_mc=0.0
this_sem_grade=[]
def updated_cap(prev_cap, prev_mc, sem_results):
    _this_sem_mc = 0
    _this_sem_point = 0.0
    _this_sem_grade = 0.0
    prev_sem_mc = prev_mc
    total_point = 0.0
    total_mc = 0.0
    sem_results.pop(0)
    for course in sem_results:
        _this_sem_mc = float(course[1])
        _this_sem_grade = float(convert_grade(course[0]))
        _this_sem_point = _this_sem_mc * _this_sem_grade
        total_point += _this_sem_point
        total_mc += _this_sem_mc
    total_point += prev_sem_mc * prev_cap
    total_mc += prev_mc
    new_cap = total_point / total_mc
    return (round(new_cap, 1), int(total_mc))
# def cap_calc(sem_results, this_sem_mc, this_sem_grade):
#    _this_sem_mc =0
#    _this_sem_point=0.0
#    _this_sem_grade=0.0
#    prev_sem_mc = this_sem_mc
#    total_point=0.0
#    total_mc=0.0
#    this_sem_grade.pop(0)
#    for course in this_sem_grade:
#       _this_sem_mc=float(course[1])
#       _this_sem_grade=float(convert_grade(course[0]))
#       _this_sem_point=_this_sem_mc*_this_sem_grade
#       total_point += _this_sem_point
#       total_mc += _this_sem_mc
#    total_point += prev_sem_mc*sem_results
#    total_mc += this_sem_mc
#    new_cap=total_point/total_mc
#    return (round(new_cap,1), int(total_mc))


      # _this_sem_grade+=(convert_grade(course[0]))

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

print(updated_cap(3.8, 20, ["ID1234A", ("A", 4), ("B", 4)]))
#updated_cap(3.8, 20, ["ID1234A", ("A", 4), ("B", 4)]) return (3.9, 28)