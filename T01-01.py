#################电梯模拟程序############################333
#position 当前楼成号，从0开始
#direction 1上移动，-1下移动，0没有移动
#ext_requests(external requests) 是一个列表， [False, True, False, True, False] 1楼和3楼有人按电梯们
#int_requests (internal requests) [1,2] 代表有人要在 1楼和2楼下。也可能是[2,1]
#door_open(...) 是一个函数，停止以后清空当前楼成。返回一个元组。例如 door_open(2, 1, [False, True, True, True, False], [2, 1])
# 返回 ([Fa1lse, True, False, True, False], [1])
#move(...) 函数在电梯关门时被调用，它会返回一个包含运行方向和下一个停靠楼层号的元组 (tuple)。当前运行方的请求（无论是梯内还是梯外请求）
#应被赋予更高的优先级。执行 move(2, 1, [False, False, False, True, False], [0, 1]) 应该返回 (1, 3)。
#这是因为在当前的运行方向上，3 楼有一个请求。
#如果没有任何请求，则返回 (0, position)（即：方向为 0，停留在当前位置）。
#如果输入的初始方向为 0（静止状态），则由你决定如何排列请求的优先级。

position=0
direction=0
ext_requests=[]
int_requests=[]

def door_open(position, direction, ext_requests, int_requests):
    a=0
    num_ext_requests = []
    for i in ext_requests:
        if i == True:
            num_ext_requests.append(a)
        a +=1
    set_ext_floor=set(num_ext_requests)
    set_int_floor=set(int_requests)
    total_floor=set_ext_floor | set_int_floor
    total_floor_list=list(total_floor)
    # print(total_floor_list)
    for j in total_floor_list:
        _index_ext=0
        _index_int=0
        _distance=j-position
        if _distance==0:
            if position in int_requests:
                int_requests.remove(position)
            position+=1
            break
        elif _distance > 0:
            if j in num_ext_requests:
                _index_ext=total_floor_list.index(j)
            if position in int_requests:
                int_requests.remove(position)
            total_floor_list.pop(_index_ext)
            position=position+_distance
            #print(j)

    ext_requests[position-1]=False

    #print("position ",position)
    # print("distance ",_distance)
    # print(ext_requests)
    # print(int_requests)
    return (ext_requests,int_requests)

def move(position, direction, ext_requests, int_requests):
    _current_floor=[position]
    a = 0
    num_ext_requests = []
    for i in ext_requests:
        if i == True:
            num_ext_requests.append(a)
        a += 1
    set_ext_floor = set(num_ext_requests)
    set_int_floor = set(int_requests)
    set_current_floor = set(_current_floor)
    total_floor = set_ext_floor | set_int_floor
    total_floor_list = list(total_floor|set_current_floor)
    # print(total_floor_list)
    _current_floor_index = total_floor_list.index(position)
    # print(_current_floor)
    for j in total_floor_list[_current_floor_index::direction]:

        if j not in total_floor:
            j+=1
        # print("j",j)
        _distance = j - position
        # print("distance",_distance)
        if direction < 0:
            position = position - _distance
            break
        elif direction > 0:
            position=position+ _distance
            break
        else:
            direction =0
            break

    tuple=(direction,position)
    return tuple


# print(position)
print(door_open(4,-1, [False,False, True, True, False], [2,1]))
#([False, False, True, True, False], [2])
print(move(3, 1, [False, False, False, False, False], []))
print(move(3, -1, [True, False, False, False, False], [1]))