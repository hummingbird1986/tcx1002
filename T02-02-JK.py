rows = [
    ("CountryA", 1, 3, 0),
    ("CountryC", 2, 4, 1),
    ("CountryB", 2, 4, 1),
    ("CountryD", 4, 3, 5),
    ("CountryE", 1, 7, 2)
]

def rank_medals(rows):
    if len(rows) == 0:
        return []
    rows.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
    # sort_rows=sorted(rows,key=lambda x: (-x[1], -x[2], -x[3], x[0]))
    rank, res = 1, [(1, ) + rows[0]]
    for i in range(1, len(rows)):
        if rows[i][1:] != rows[i-1][1:]:
            rank += 1
        res.append((rank,) + rows[i])
    return res

assert set(rank_medals(rows)) == {(1, 'CountryD', 4, 3, 5), (2, 'CountryC', 2, 4, 1), (4, 'CountryA', 1, 3, 0), (3, 'CountryE', 1, 7, 2), (2, 'CountryB', 2, 4, 1)}
assert set(rank_medals([("ZED", 0, 0, 0), ("ALB", 0, 0, 0), ("MEX", 0, 0, 0)])) == {(1, 'MEX', 0, 0, 0), (1, 'ZED', 0, 0, 0), (1, 'ALB', 0, 0, 0)}
assert set(rank_medals([("A", 1, 0, 0), ("B", 1, 1, 0), ("C", 1, 1, 0), ("D", 1, 0, 5), ("E", 0, 10, 0)])) == {(2, 'D', 1, 0, 5), (3, 'A', 1, 0, 0), (1, 'C', 1, 1, 0), (1, 'B', 1, 1, 0), (4, 'E', 0, 10, 0)}