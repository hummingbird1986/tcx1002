# 凡是在课程结束后才扫码的人员，均记为缺勤（0分）。
# 1. 对于测验/评估课 (AS - Assessments):
# 缺勤 (0分)：
# 在课程进行到一半时间之后才到达。
# 或者，在课程开始 1 小时之后才到达。
# 迟到 (0.5分)：
# 在课程开始后的 15 分钟至 1 小时内到达（即：过了 15 分钟但没过 1 小时）。
# 出勤 (1分)：
# 在课程开始后的 15 分钟之内到达。
# 2. 对于讲座 (LT - Lectures) 和 辅导课 (TR - Tutorials):
# 出勤 (1分)：只要学生在课程结束前完成扫码，即视为出勤。
# 缺勤 (0分)：课程结束后才扫码或未扫码。
from datetime import datetime, timedelta
from operator import truediv

from jupyter_server.auth import passwd

sessions = {
    1: ('LT', datetime(2025,1,1,19,0,0),  datetime(2025,1,1,21,0,0)),
    2: ('TR', datetime(2025,1,8,10,30,0), datetime(2025,1,8,12,30,0)),
    3: ('TR', datetime(2025,1,12,19,0,0), datetime(2025,1,12,20,0,0)),
    4: ('LT', datetime(2025,1,15,19,0,0), datetime(2025,1,15,22,0,0)),
    5: ('TR', datetime(2025,1,16,19,0,0), datetime(2025,1,16,20,0,0)),
    10: ('AS', datetime(2025,1,21,19,0,0), datetime(2025,1,21,20,0,0)),
    11: ('AS', datetime(2025,1,22,19,0,0), datetime(2025,1,22,21,0,0)),
}

qr_scans = [
    (1, datetime(2025,1,1,19,1,0),  'Alice'),
    (1, datetime(2025,1,1,19,8,0),  'Bob'),
    (1, datetime(2025,1,1,19,35,0), 'Charlie'),
    (2, datetime(2025,1,8,10,25,0), 'Alice'),
]

def status(session_type, start, end, qr_time):
    duration_ = (end - start).total_seconds()/60
    half_duration_ = duration_/2
    late_time_= (qr_time-start).total_seconds()/60
    # print(duration_,half_duration_,late_time_,session_type)

    if session_type == 'AS':
       if late_time_ >= 60.0 or late_time_ >= half_duration_:
            score_=0.0
       elif late_time_ <= 15.0:
            score_=1.0
       else:
            score_=0.5
    else:
       if late_time_< duration_:
            score_=1.0
       else:
            score_=0.0
    return score_

def attendance(query):
    student_score={}
    history=[]
    qr_time_list=[]
    if isinstance(query, datetime): #判断是否为 datetime 的类
        for candidate in qr_scans:
            # query_time_ = candidate[1]
            if candidate[1] == query:
                session_id_ = candidate[0]
                qr_time_ = candidate[1]
                session_type_ = sessions[session_id_][0].upper()
                start_time_ = sessions[session_id_][1]
                end_time_ = sessions[session_id_][2]
                score_ = status(session_type_, start_time_, end_time_, qr_time_)
                record_=(candidate[2],candidate[1],score_)
        qr_time_list.append(record_)

        return qr_time_list
        # return [(name, qr_time, score), (name, qr_time, score), ...]
    elif isinstance(query, str): #判断是否为 String
        for candidate in qr_scans:
            student_name_=candidate[2]
            if student_name_.upper()==query.upper():
                session_id_=candidate[0]
                qr_time_=candidate[1]
                session_type_=sessions[session_id_][0].upper()
                start_time_=sessions[session_id_][1]
                end_time_=sessions[session_id_][2]
                score_=status(session_type_,start_time_,end_time_,qr_time_)
                history.append((session_id_,qr_time_,score_))
                if student_name_ not in student_score:
                    student_score[student_name_]=0.0
                student_score[student_name_]+=score_
                # print(f'score_= {score_:.1f} and session_id_= {session_id_}')
                # print(student_score)
        return student_score[student_name_],history
        # return (total_score, [(session_id, qr_time, score), (session_id, qr_time, score)...])
    else:
        return False


print(attendance('alice'))
print(attendance('ALice')[0]== 2.0)
print(attendance(datetime(2025,1,1,19,1,0  )))