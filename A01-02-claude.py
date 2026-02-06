from datetime import datetime, timedelta

sessions = {
    1: ('LT', datetime(2025, 1, 1, 19, 0, 0), datetime(2025, 1, 1, 21, 0, 0)),
    2: ('TR', datetime(2025, 1, 8, 10, 30, 0), datetime(2025, 1, 8, 12, 30, 0)),
    3: ('TR', datetime(2025, 1, 12, 19, 0, 0), datetime(2025, 1, 12, 20, 0, 0)),
    4: ('LT', datetime(2025, 1, 15, 19, 0, 0), datetime(2025, 1, 15, 22, 0, 0)),
    5: ('TR', datetime(2025, 1, 16, 19, 0, 0), datetime(2025, 1, 16, 20, 0, 0)),
    10: ('AS', datetime(2025, 1, 21, 19, 0, 0), datetime(2025, 1, 21, 20, 0, 0)),
    11: ('AS', datetime(2025, 1, 22, 19, 0, 0), datetime(2025, 1, 22, 21, 0, 0)),
}

qr_scans = [
    (1, datetime(2025, 1, 1, 19, 1, 0), 'Alice'),
    (1, datetime(2025, 1, 1, 19, 8, 0), 'Bob'),
    (1, datetime(2025, 1, 1, 19, 35, 0), 'Charlie'),
    (2, datetime(2025, 1, 8, 10, 25, 0), 'Alice'),
]


def status(session_type, start, end, qr_time):
    # 【修改1】先检查是否扫描晚于session结束
    if qr_time > end:
        return 0

    minutes_late = (qr_time - start).total_seconds() / 60
    duration = (end - start).total_seconds() / 60

    if session_type == 'AS':
        if minutes_late > 60 or minutes_late > duration / 2:
            return 0
        elif minutes_late <= 15:
            return 1
        else:
            return 0.5
    else:  # LT or TR
        # 【修改2】LT/TR只要在结束前扫描就是present
        return 1


def attendance(query):
    if isinstance(query, str):
        # 【修改3】整个字符串查询部分重写，逻辑更清晰
        student_name = query
        student_scans = {}  # {session_id: earliest_qr_time}

        # 收集该学生所有扫描，每个session只保留最早的
        for session_id, qr_time, name in qr_scans:
            if name.upper() == student_name.upper():
                if session_id not in student_scans or qr_time < student_scans[session_id]:
                    student_scans[session_id] = qr_time

        # 计算分数
        history = []
        total_score = 0

        for session_id in sorted(student_scans.keys()):
            qr_time = student_scans[session_id]
            session_type, start, end = sessions[session_id]
            score = status(session_type, start, end, qr_time)
            history.append((session_id, qr_time, score))
            total_score += score

        return (total_score, history)

    elif isinstance(query, datetime):
        # 【修改4】datetime查询部分完全重写
        target_session_id = None

        # 找到覆盖该时间的session (start <= query <= end)
        for session_id, (session_type, start, end) in sessions.items():
            if start <= query <= end:
                target_session_id = session_id
                break

        if target_session_id is None:
            return []

        # 收集该session的所有学生（每个学生只保留最早扫描）
        student_scans = {}  # {name: earliest_qr_time}
        session_type, start, end = sessions[target_session_id]

        for session_id, qr_time, name in qr_scans:
            if session_id == target_session_id:
                if name not in student_scans or qr_time < student_scans[name]:
                    student_scans[name] = qr_time

        # 计算每个学生的分数
        result = []
        for name, qr_time in student_scans.items():
            score = status(session_type, start, end, qr_time)
            result.append((name, qr_time, score))

        # 按名字排序
        result.sort(key=lambda x: x[0])
        return result

    print(attendance('Alice'))
    print(attendance('ALice')[0])
    print(attendance(datetime(2025,1,8,10,30,0)))