def sol():
    N, M = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    num = arr[0]
    know_people = []

    parties = []
    for i in range(M):
        parties.append(list(map(int, input().split(' ')))[1:])

    if num == 0:
        print(M)
        return
    know_people = arr[1:]
    while True:
        indexes = []
        new_parties = []
        new_know_people = []
        for i in range(len(parties)):
            party = parties[i]
            exist = False
            for j in know_people:
                if j in party:
                    indexes.append(i)
                    exist = True
            if not exist:
                new_parties.append(party)

        for i in indexes:
            party = parties[i]
            for person in party:
                if person not in know_people:
                    new_know_people.append(person)
        know_people = new_know_people
        parties = new_parties
        if len(know_people) == 0:
            break
    print(len(parties))


sol()
