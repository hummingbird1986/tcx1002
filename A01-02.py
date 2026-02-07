from datetime import datetime, timedelta
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
    (1, datetime(2025,1,1,19,2,0),  'Alice'),
    (2, datetime(2025,1,8,10,30,0), 'Alice'),
]

def status(session_type, start, end, qr_time):
    if qr_time > end:
        return 0
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

        score_=1
    return score_

def attendance(query):
    student_score={}
    history=[]

    if isinstance(query, datetime): #判断是否为 datetime 的类
        for candidate in qr_scans:
            # query_time_ = candidate[1]
            if candidate[1] == query:
                session_id_= candidate_helper(candidate)[0]
                disc=query_time_name_helper(candidate[2])
                list=[]
                for iterm in disc:
                    if iterm[0]==session_id_:
                        list.append(iterm[1])
        history.append(list[0]) #这里是空的，因为 query 不在列表里。需要  start <=query <= end 来找到 session id
        return history
    elif isinstance(query, str): #判断是否为 String
        for candidate in qr_scans:
            student_name_=candidate[2]
            if student_name_.upper()==query.upper():
                session_id_, qr_time_, session_type_, start_time_, end_time_ ,score_ = candidate_helper(candidate)
                history.append((session_id_,qr_time_,score_))
                if student_name_ not in student_score:
                    student_score[student_name_]=0.0
                student_score[student_name_]+=score_
        return student_score[student_name_],history
    else:
        return None

def candidate_helper(candidate_):
    session_id_ = candidate_[0]
    qr_time_ = candidate_[1]
    session_type_ = sessions[session_id_][0].upper()
    start_time_ = sessions[session_id_][1]
    end_time_ = sessions[session_id_][2]
    score_ = status(session_type_, start_time_, end_time_, qr_time_)
    return session_id_, qr_time_, session_type_, start_time_, end_time_,score_

def query_time_name_helper(name_):
    same_name={}
    # name_list=[]
    for candidate in qr_scans:
        if candidate[2].upper()==name_.upper():
            score_=candidate_helper(candidate)[5]
            session_id_=candidate_helper(candidate)[0]
            name_tuple=(name_,candidate[1],int(score_))
            list_with_session=[session_id_,name_tuple]
            if name_ not in same_name:
                same_name[name_] = []
            same_name[name_].append(list_with_session)
    name_list=same_name[name_]
    name_list.sort()
    return name_list

print(attendance('alice'))
# print(attendance('ALice')[0]== 2.0)
print(attendance(datetime(2025,1,8,10,30,0)))