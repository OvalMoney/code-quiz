import os
import collections


class SolveParty(object):
    """Funny class to solve a funny problem."""
    def __init__(self, filename):
        self.output = "{}.out".format(filename)
        self.input = "{}.in".format(filename)
        if not os.path.isfile(self.input):
            raise TypeError("{} does not exist".format(self.input))

        with open(self.input) as f:
            lines = f.read().splitlines()[1:]

        couples = zip(*[iter(lines)]*2)
        _, self.guests = zip(*couples)
        self.solution = [(case, alone) for case, alone in self._solve()]

    def _solve(self):
        for case, guests in enumerate(self.guests, 1):
            counter = collections.Counter(guests.split(" "))
            alone = [v for v, c in counter.most_common() if c == 1][0]
            yield case, alone

    def write(self):
        template = "Case #{}: {}\n"
        lines = [template.format(case, guest) for case, guest in self.solution]
        with open(self.output, 'w') as f:
            f.writelines(lines)


if __name__ == '__main__':
    SolveParty('oval-quiz-lg').write()
    SolveParty('oval-quiz-sm').write()
