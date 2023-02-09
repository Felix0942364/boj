from collections import deque

def solution(cap, n, deliveries, pickups):
    delivery_list = list()
    pickup_list = list()
    for idx in range(len(deliveries)):
        delivery_list += [idx+1] * deliveries[idx]
    for idx in range(len(pickups)):
        pickup_list += [idx+1] * pickups[idx]
    
    # [1,3,3,3,4,5,5]
    # [2,2,2,4,4,4,4]
    
    delivery_list = deque(delivery_list[-1::-cap])
    pickup_list = deque(pickup_list[-1::-cap])
    
    # [5,3]
    # [4,2]
    
    answer = list()
    while delivery_list and pickup_list:
        answer.append(max(delivery_list.popleft(), pickup_list.popleft()))
    while delivery_list:
        answer.append(delivery_list.popleft())
    while pickup_list:
        answer.append(pickup_list.popleft())
    
    return 2*(sum(answer))