def main():
    path = r"D:\Programy\z.programowanie\elephant\zadanie_B\slo2.in"
    with open(path) as f:
        c = f.read()
    c = c.split("\n")[:-1]
    for i in range(1, 4):
        c[i] = list(map(int, c[i].split()))
    ele_weight = {k: v for k, v in enumerate(c[1], start=1)}
    elephants = []
    for i in range(int(c[0])):
        if not c[2][i] == c[-1][i]:
            elephants.append((c[2][i], c[-1][i]))
        else:
            del ele_weight[c[2][i]]
    mass = 0
    for elem in elephants:
        if elem[::-1] in elephants:
            mass += ele_weight[elem[0]]+ele_weight[elem[1]]
            for i in [elem, elem[::-1]]:
                elephants.remove(i)
    ai = 1
    sort_eleph = {}
    while len(elephants) > 0:
        sort_eleph[ai] = [elephants.pop()[0]]
        for elem in sort_eleph[ai]:
            for i in elephants:
                if elem in i:
                    sort_eleph[ai].append(elephants.pop(elephants.index(i))[0])
        ai+=1
    min_global = ele_weight[min(ele_weight, key=ele_weight.get)]
    # print(min_global)
    for key in sort_eleph:
        sort_eleph[key] = sorted(list(map(lambda x: ele_weight[x], sort_eleph[key])))
        print(f"{len(sort_eleph[key])}{-1}*{min_global}")
        mass += ((len(sort_eleph[key])-1)*min_global)
        print(f"{2}*({sort_eleph[key][0]}+{min_global})")
        mass += 2*sort_eleph[key][0]
        for elem in sort_eleph[key][1:]:
            # print(elem)
            mass += elem
    print()
    print(mass)
    with open(path.replace("in", "out")) as h:
        l = h.read()
        print(l.strip())
if __name__ == '__main__':
    main()
