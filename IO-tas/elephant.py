def load_input() -> list:
    values = [input() for _ in range(4)]
    for i in range(1, 4):
        values[i] = list(map(int, values[i].split()))
    return values


def calc_sum_mass(values) -> int:
    eleph_weight = {eleph_num: mass for eleph_num, mass in enumerate(values[1], start=1)}
    elephants = [(values[2][i], values[3][i]) for i in range(int(values[0]))]
    step = 1
    sort_eleph = {}
    while len(elephants) > 0:
        sort_eleph[step] = [elephants.pop()]
        for elem in sort_eleph[step]:
            for elephant in elephants:
                if elem[0] in elephant:
                    sort_eleph[step].append(elephants.pop(elephants.index(elephant)))
        step += 1
    min_global = eleph_weight[min(eleph_weight, key=eleph_weight.get)]
    total_mass = 0
    for key in sort_eleph:
        sort_eleph[key] = list(map(lambda x: eleph_weight[x[0]], sort_eleph[key]))
        a = sum(sort_eleph[key])+((len(sort_eleph[key])-2)*min(sort_eleph[key]))
        b = sum(sort_eleph[key])+min(sort_eleph[key])+((len(sort_eleph[key])+1)*min_global)
        total_mass += min(a,b)
    return total_mass


def main():
    a = load_input()
    result = calc_sum_mass(a)
    print(result)
if __name__ == '__main__':
    main()
