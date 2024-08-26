"""
Gegeven twee integers n en k, geef alle mogelijke combinaties van k unieke getallen in het interval
[1, n]. Bij invoer van n = 4 en k = 2 zou je programma als uitvoer [[2,4], [3,4], [2,3],
[1,2], [1,3], [1,4]] moeten teruggeven.
"""


# Examines current offered candidate solution. Returns:
# Abandon on repeat elements or non-ascending; Accept if long enough; Continue otherwise
def examine(n, k, partiele_oplossing=""):
    if len(set(partiele_oplossing)) < len(partiele_oplossing):
        return
    elif len(partiele_oplossing) == k:
        return "ACCEPT"
    return "CONTINUE"


# Returns the partial solution and its conjugates with 1->n each.
def extend(n, kandidaat):
    extended = []
    for i in range(1, n + 1):
        if len(kandidaat) == 0 or i > kandidaat[-1]:
            extended.append(kandidaat + [i])
    return (extended)


#
def solve(n, k, partiele_oplossing=[]):
    match examine(n, k, partiele_oplossing):
        case "ACCEPT":  # End of recursion. Its returned will be appended to oplossing
            return [partiele_oplossing]
        case "CONTINUE":
            oplossing = []

            for kandidaat in extend(n, partiele_oplossing):
                end_results = solve(n, k, kandidaat)
                if end_results is not None:
                    for answer in end_results:
                        oplossing.append(answer)
            return oplossing


assert solve(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(solve(4, 2))
assert solve(5, 1) == [[1], [2], [3], [4], [5]]
print(solve(5, 1))
