# 输入数据：每一行格式为 (国家, 金牌, 银牌, 铜牌)。
#
# 排名优先级：金牌 > 银牌 > 铜牌（数量越多排名越靠前）。
#
# 排名规则：相同奖牌数的国家排名相同，且下一个排名的数字紧随其后（例如：1, 2, 2, 3... 而不是 1, 2, 2, 4）。
#
# 排序要求：如果排名相同，则按国家名称的字母顺序排序。
#
# 返回值：列表格式为 (排名, 国家, 金牌, 银牌, 铜牌)。
# 用sort 函数

rows = [
    ("CountryA", 1, 7, 0),
    ("CountryC", 2, 4, 1),
    ("CountryB", 2, 4, 1),
    ("CountryD", 4, 3, 5),
    ("CountryE", 1, 7, 2)
]

def rank_medals(rows):
    sort_name = sort_brown_medals().copy()
    # _sort_name=sort_name.copy()
    cold_list=[]
    silver_list=[]
    brown_list=[]
    length = len(sort_name)
    for i in range(length):
        for j in range(i + 1, length):
            if sort_name[j][1] == sort_name[i][1]:
                cold_list.append(sort_name[i])
                cold_list.append(sort_name[j])
    return cold_list, silver_list, brown_list

# def convert_list(rows):
#     rows_list = []
#     for i in rows:
#         rows_list.append(list(i))
#     return rows_list

def sort_gold_medals(rows):
    _converted_list = rows.copy()
    _medal_list = []
    length = len(_converted_list)
    for i in range(length):
        for j in range(i+1, length):
            if _converted_list[j][1]>_converted_list[i][1]:
                _converted_list[i], _converted_list[j] = _converted_list[j], _converted_list[i]

    # print(_medal_list)
    # for k in range(length):
    #     for l in range(k+1, length):
    #         if _converted_list[k][1] == _converted_list[j][1]:
    #             _medal_list.append(_converted_list[k])
    # print(_converted_list)
    return _converted_list
#
def sort_silver_medals():
    _converted_list = sort_gold_medals(rows).copy()
    for i in range(len(_converted_list)):
        for j in range(i+1, len(_converted_list)):
            if _converted_list[i][1] == _converted_list[j][1]:
                if _converted_list[j][2] > _converted_list[i][2]:
                    _converted_list[i],_converted_list[j] = _converted_list[j],_converted_list[i]
    # print(_converted_list)
    return _converted_list

def sort_brown_medals():
    _converted_list = sort_silver_medals().copy()
    for i in range(len(_converted_list)):
        for j in range(i+1, len(_converted_list)):
            if _converted_list[i][2] == _converted_list[j][2]:
                if _converted_list[j][3] > _converted_list[i][3]:
                    _converted_list[i],_converted_list[j] = _converted_list[j],_converted_list[i]
    # print(_converted_list)
    return _converted_list


print(sort_brown_medals())
print(rank_medals(rows))
#[(1, 'CountryD', 4, 3, 5), (2, 'CountryB', 2, 4, 1), (2, 'CountryC', 2, 4, 1), (3, 'CountryE', 1, 7, 2), (4, 'CountryA', 1, 3, 0)]


