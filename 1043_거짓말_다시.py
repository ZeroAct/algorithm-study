from sys import stdin
from collections import defaultdict
input = stdin.readline

N, M = map(int, input().split())
dd = list(map(int, input().split()))

people_set = set(list(range(1, N+1)))
dn = dd[0]
detectors = set(dd[1:]) if len(dd) > 1 else set([])

party_people = defaultdict(list)
people_party = defaultdict(list)
for i in range(M):
    people = list(map(int, input().split()))[1:]
    for person in people:
        people_party[person].append(i)
        party_people[i].append(person)

    while True:
        before_detector = detectors.copy()
        for detector in before_detector:
            for party in people_party[detector]:
                for person in party_people[party]:
                    detectors.add(person)
        if len(before_detector) == len(detectors):
            break

safe_people = people_set - detectors
safe_party = set()
for safe_person in safe_people:
    for party in people_party[safe_person]:
        safe_party.add(party)
print(len(safe_party))
