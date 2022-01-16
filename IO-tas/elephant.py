def load_input() -> list:
    values = [input() for _ in range(4)]
    for i in range(1, 4):
        values[i] = list(map(int, values[i].split()))
    return values


def calc_sum_mass(values) -> int:
    eleph_weight = {eleph_num: mass for eleph_num, mass in enumerate(values[1], start=1)}
    eleph_position = [(values[2][i], values[3][i]) for i in range(int(values[0]))]
    step = 1
    eleph_cycle = {}
    while len(eleph_position) > 0:
        eleph_cycle[step] = [eleph_position.pop()[0]]
        for elem in eleph_cycle[step]:
            for elephant in eleph_position:
                if elem in elephant:
                    eleph_cycle[step].append(eleph_position.pop(eleph_position.index(elephant))[0])
        eleph_cycle[step] = list(map(lambda x: eleph_weight[x], eleph_cycle[step]))
        step += 1
    min_global = eleph_weight[min(eleph_weight, key=eleph_weight.get)]
    total_mass = 0
    for key in eleph_cycle:
        a = sum(eleph_cycle[key])+((len(eleph_cycle[key])-2)*min(eleph_cycle[key]))
        b = sum(eleph_cycle[key])+min(eleph_cycle[key])+((len(eleph_cycle[key])+1)*min_global)
        total_mass += min(a,b)
    return total_mass


def main():
    a = load_input()
    result = calc_sum_mass(a)
    print(result)
if __name__ == '__main__':
    main()
