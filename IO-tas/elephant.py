def load_input() -> list:
    values = [input() for _ in range(4)]
    for i in range(1, 4):
        values[i] = list(map(int, values[i].split()))
    return values


def calc_sum_mass(values) -> int:
    eleph_weight = {eleph_num: mass for eleph_num, mass in enumerate(values[1], start=1)}
    eleph_position = [(pos, dest_pos) for pos, dest_pos in zip(values[2], values[3])]
    cycle = 1
    eleph_cycle = {}
    while len(eleph_position) > 0:
        eleph_cycle[cycle] = [eleph_position.pop()[0]]
        for position in eleph_cycle[cycle]:
            for elephant in eleph_position:
                if position in elephant:
                    eleph_cycle[cycle].append(eleph_position.pop(eleph_position.index(elephant))[0])
        eleph_cycle[cycle] = list(map(lambda x: eleph_weight[x], eleph_cycle[cycle]))
        cycle += 1
    min_global_weight = eleph_weight[min(eleph_weight, key=eleph_weight.get)]
    total_mass = 0
    for cycle in eleph_cycle:
        a = sum(eleph_cycle[cycle])+((len(eleph_cycle[cycle])-2)*min(eleph_cycle[cycle]))
        b = sum(eleph_cycle[cycle])+min(eleph_cycle[cycle])+((len(eleph_cycle[cycle])+1)*min_global_weight)
        total_mass += min(a, b)
    return total_mass


def main():
    data = load_input()
    result = calc_sum_mass(data)
    print(result)
if __name__ == '__main__':
    main()
