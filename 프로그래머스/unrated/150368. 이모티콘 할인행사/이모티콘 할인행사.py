def solution(users, emoticons):
    discount_rate = [10, 20, 30, 40]
    length = len(emoticons)
    max_val = (0, 0)

    for case in range(1 << 2 * length):
        discount = [discount_rate[(case >> 2 * j) % (1 << 2)] for j in range(length)]
        subset_subscription = 0
        subset_total = 0
        for tolerance, mx_value in users:
            tmp_val = 0
            for idx in range(length):
                if discount[idx] >= tolerance:
                    tmp_val += (100 - discount[idx]) * emoticons[idx] / 100
            if tmp_val >= mx_value:
                subset_subscription += 1
            else:
                subset_total += tmp_val
        if (subset_subscription, subset_total) > max_val:
            max_val = (int(subset_subscription), int(subset_total))

    return list(max_val)
