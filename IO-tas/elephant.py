def main():
    path = r"D:\Programy\z.programowanie\elephant\zadanie_B\slo1.in"
    with open(path) as f:
        c = f.read()
    c = c.split("\n")[:-1]
    print(c)
    for i in range(1, 4):
        c[i] = list(map(int, c[i].split()))
    ele_weight = {k: v for k, v in enumerate(c[1], start=1)}
    elephants = [(c[2][i], c[-1][i]) for i in range(int(c[0])) if not c[2][i] == c[-1][i]]
    mass = 0
    print(ele_weight)
    for elem in elephants:
        if elem[::-1] in elephants:
            mass += (ele_weight[elem[0]]+ele_weight[elem[1]])
            for i in [elem, elem[::-1]]:
                elephants.remove(i)
    print(f"Pierwsza masa: {mass}")
    ai = 1
    sort_eleph = {}
    while len(elephants) > 0:
        sort_eleph[ai] = [elephants.pop()]
        for elem in sort_eleph[ai]:
            for i in elephants:
                if elem[1] in i:
                    sort_eleph[ai].append(elephants.pop(elephants.index(i)))
        ai+=1
    print(sort_eleph)        
    for key in sort_eleph:
        max_val = min([ele_weight[key] for i in sort_eleph[key] for key in i])
        val = list(ele_weight.values()).index(max_val)+1
        # print(key, max_val, val)
        if val != sort_eleph[key][0][0]:
            for elem in sort_eleph[key]:
                if elem[0] == val:
                    index = list(sort_eleph[key]).index(elem)
                    sort_eleph[key] = list(sort_eleph[key])[index:] + list(sort_eleph[key])[:index]
        for elem in list(sort_eleph[key])[1:]:
            print(key, ele_weight[val], ele_weight[elem[0]])
            mass += ele_weight[val] + ele_weight[elem[0]]
    print(mass)
    with open(path.replace("in", "out")) as h:
        l = h.read()
        print(l.strip())
if __name__ == '__main__':
    main()
