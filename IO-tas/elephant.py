def main():    
    with open(r".\zadanie_B\slo1.in") as f:
        c = f.read()

    c = c.split("\n")[:-1]
    for i in range(1, 4):
        c[i] = list(map(int, c[i].split()))

    ele_weight = {k: v for k, v in enumerate(c[1], start=1)}
    elephants = [(c[2][i], c[-1][i]) for i in range(int(c[0])) if not c[2][i] == c[-1][i]]

    mass = 0
    for elem in elephants:
        if elem[::-1] in elephants:
            mass += (ele_weight[elem[0]]+ele_weight[elem[1]])/2
            for i in [elem, elem[::-1]]:
                elephants.remove(i)

    # print(elephants)
    print(int(mass))

    ai = 1
    sort_eleph = {}
    while len(elephants) > 0:
        sort_eleph[ai] = [elephants.pop()]
        for elem in sort_eleph[ai]:
            for i in elephants:
                if elem[1] in i:
                    sort_eleph[ai].append(elephants.pop(elephants.index(i)))
        ai+=1

    for key in sort_eleph:
        print(key, len(sort_eleph[key]))


    print(sort_eleph)
    # with open(r".\zadanie_B\slo3.out") as f:
    #     c = f.read()
    #     # print(c.strip())

if __name__ == '__main__':
    main()
