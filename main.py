
class SolveParty(object):
    """Funny class to solve a funny problem."""

    def __init__(self, filename):
        self.output = "{}.out".format(filename)
        self.input = "{}.in".format(filename)

        with open(self.input) as f:
            lines = f.read().splitlines()[2::2]

        self.guests = [line.split() for line in lines]

    def solution(self):
        for guests in self.guests:
            hashmap = {}
            for g in guests:
                if g not in hashmap:
                    hashmap[g] = None
                else:
                    del hashmap[g]
            alone, _ = hashmap.popitem()
            yield alone

    def write(self):
        template = "Case #{}: {}\n"
        lines = [template.format(case, guest) for case, guest in enumerate(self.solution(), 1)]
        with open(self.output, 'w') as f:
            f.writelines(lines)


if __name__ == '__main__':
    SolveParty('oval-quiz-lg').write()
    SolveParty('oval-quiz-sm').write()
