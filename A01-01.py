def min_workers(demand):
   allocated_workers = []
   demand_ = demand.copy()
   population = 0
   while True :
        start_day_tuple = highest_demand_days(demand_)
        start_day = start_day_tuple[0]
        for offset in range(5):
            idx = (start_day + offset ) % 7
            # print(idx)
            if demand_[idx]> 0:
                demand_[idx] -= 1
        allocated_workers.append(start_day)
        population += 1
        if highest_demand_days(demand_)[1]==0:
             return  population,allocated_workers

def highest_demand_days(demand):
    max_val = -1
    best_start_day = 0
    for start_day in range(7):
        current_window_sum = 0
        for offset in range(5):
            day = (start_day + offset) % 7
            current_window_sum += demand[day]

        if current_window_sum > max_val:
            max_val = current_window_sum
            best_start_day = start_day

    return best_start_day, max_val
print(min_workers([4, 2, 4, 3, 5, 4, 6]))
# print(highest_demand_days([4, 2, 4, 3, 5, 4, 6]))
#(7, [2, 3, 4, 2, 5, 0, 2])
# print(min_workers([1, 1, 1, 1, 1, 2, 2])[0])
#