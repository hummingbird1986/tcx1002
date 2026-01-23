##按照CAP进行排名前 20% 排名
#小于12个积分的不能排名，每一科目4分
#在20%界限CAP一样，所有的相同的都纳入名单。
#1-2-2-4 规则
#2.2 个学生向上去整学生
import math
Sem2_results = [["Aaron", "A", "B+", "B"], ["Ben", "B", "B+", "C"], ["Carol", "A", "A", "A"],
                ["David", "B", "B", "B"], ["Eve", "A", "A", "A-"], ["Fen", "A", "B", "C"],
                ["Gordon", "B", "C", "D"], ["Hannah", "C", "C","C"], ["Ian", "A", "A"], ["John", "A","A","A-"]]


def get_deans_list(Sem2_results):
    name_list = []
    unsort_list = get_gpa(Sem2_results)
    sorted=sorting(unsort_list)
    # print(sorted)
    list_length = len(sorted)
    top_list=math.ceil(list_length*0.2)
    # print(top_list)
    left_list=sorted[:top_list]
    # print(left_list)
    right_list=sorted[top_list:]
    for i in right_list:
        if left_list[top_list-1][0]==i[0]:
           left_list.append(i)
    # print(left_list)
    for j in left_list:
        name_list.append(j[1])
    # print(name_list)
    return name_list

def sorting(unsort):
    sorted_list = unsort.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(i+1,n):
            if sorted_list[i] < sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    # for i in sorted_list:
    #     i_index=sorted_list.index(i)
    #     j_index=i_index+1
    #     for j in sorted_list[j_index:]:
    #         if i>j:
    #             sorted_list[i_index],sorted_list[j_index]=sorted_list[j_index],sorted_list[i_index]
    return sorted_list


def get_gpa(Sem2_results_list):
    score_name_list=[]
    for s in Sem2_results_list:
        student_score=0.0
        modual_unit=len(s)-1
        if modual_unit >= 3:
           for i in s[1:]:
             student_score+=float(convert_grade(i))
           gpa=student_score/modual_unit
           score_name_list.append([gpa,s[0]])
    return score_name_list

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
    score_point =float(grade_point[score])
    return score_point
get_deans_list(Sem2_results)

#Sem2_results = [ ["Aaron", "A", "B+", "B"], ["Ben", "B", "B+", "C"], ... ].输出 ['Carol', 'Eve', 'John'].