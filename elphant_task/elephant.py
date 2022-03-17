def load_input() -> list:
    values = [input() for _ in range(4)]
    for i in range(1, 4):
        values[i] = list(map(int, values[i].split()))
    return values


def create_cycles(values) -> list:
    eleph_position = {pos: dest_pos for pos, dest_pos in zip(values[2], values[3]) if pos != dest_pos}
    cycles = []
    for elephant in values[2]:
        position = eleph_position.pop(elephant, None)
        if position is None:
            continue
        cycle = [elephant]
        while elephant != position:
            cycle.append(position)
            position = eleph_position.pop(position)
        cycles.append(cycle)
    return cycles


def calc_sum_mass(values, cycles) -> int:
    eleph_weight = {eleph_num: mass for eleph_num, mass in enumerate(values[1], start=1)}
    for i in range(len(cycles)):
        cycles[i] = list(map(lambda x: eleph_weight[x], cycles[i]))
    min_global_weight = min(values[1])
    total_mass = 0
    for cycle in cycles:
        a = sum(cycle)+((len(cycle)-2)*min(cycle))
        b = sum(cycle)+min(cycle)+((len(cycle)+1)*min_global_weight)
        total_mass += min(a, b)
    return total_mass


def main():
    data = load_input()
    cycles = create_cycles(data)
    result = calc_sum_mass(data, cycles)
    print(result)
if __name__ == '__main__':
    main()
