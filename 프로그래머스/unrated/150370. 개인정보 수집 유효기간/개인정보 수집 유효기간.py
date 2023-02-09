def solution(today, terms, privacies):
    def t_tf(year, month, day, diff=0):
        if month + diff > 12:
            if (month + diff) % 12:
                return year + (month+diff)//12, (month+diff) % 12, day
            else:
                return year + (month+diff)//12-1, 12, day
        return year, month + diff, day

    answer = []
    term_dic = dict()
    for term in terms:
        k, m = term.split()
        term_dic[k] = m

    for idx in range(len(privacies)):
        t, p = privacies[idx].split()
        if tuple(map(int, today.split("."))) >= t_tf(*map(int, t.split(".")), int(term_dic[p])):
            answer.append(idx+1)

    return answer
