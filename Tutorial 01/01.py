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

def door_open(position, direction, ext_requests, int_requests):
    position =0
    direction =0
    ext_requests = [False, False, False, False, False]
    int_requests = []

def move(position, direction, ext_requests, int_requests):
    pass


door_open(1, 1, [False, True, True, True, False], [1, 2])
#([False, False, True, True, False], [2])
move(2, 1, [False, False, False, True, False], [0, 1])
#(1, 3)