import sys
import unittest


class Issue():
    def __init__(self):
        self.mod = 10**9
        self.motion = []

    # for checking the expected number as per the input of 5 numbers.
    def standard(self):
        self.get_awaited_number(2, 5, 1, 3, 5)
        self.get_awaited_number(3, 20, 4, 9, 17)
        print("E(2,5,1,3,5) : ",self.get_awaited_number(2, 5, 1, 3, 5))
        print("E(3,20,4,9,17) : ",self.get_awaited_number(3, 20, 4, 9, 17))

    # It returns the expected number of steps as per the input.
    def get_awaited_number(self, n, k, a, b, c):
        g = (2**(n + 2) - 3 - (-1)**n) // 6
        # print("get_awaited_number : ",2 * g * (c - a) * (k - 1) - (2 * k - b - c) * (c - b))
        return 2 * g * (c - a) * (k - 1) - (2 * k - b - c) * (c - b)

    # resolving() is using for printing the expected number of steps and checking the number as per inputs.
    def resolving(self):
        self.standard()
        print("∑1≤n≤10000 E(n,10n,3n,6n,9n) : ",self.get_number())

    # get_number() is using for getting the number of steps.
    def get_number(self):
        total_awaited_number = 0
        temp = 1
        previous, current = 0, 1
        k, a, b, c = 10, 3, 6, 9
        while temp < 10001:
            awaited_number = (2 * current * (c - a) * (k - 1) - (2 * k - b - c) * (c - b)) % self.mod
            total_awaited_number = (total_awaited_number + awaited_number) % self.mod
            previous, current = current, (current + 2 * previous + 1) % self.mod
            k = (k * 10) % self.mod
            a = (a * 3) % self.mod
            b = (b * 6) % self.mod
            c = (c * 9) % self.mod
            temp=temp+1
        return total_awaited_number

    # it returns the number of steps for different movements.
    def imitate(self, n):
        a, b, c = 3, 4, 5
        self.shift_tower(n, a, c, b)
        return self.figure(a, b, c)

    # shift_tower() is using to passing the parameters to the functions
    def shift_tower(self, peak, from_pillar, to_pillar, with_pillar):
        if peak >= 1:
            self.shift_tower(peak - 1, from_pillar, with_pillar, to_pillar)
            self.shift_disk(from_pillar, to_pillar)
            self.shift_tower(peak - 1, with_pillar, to_pillar, from_pillar)

    # appending the movement from one pillar to another pillar
    def shift_disk(self, from_pillar, to_pillar):
        self.motion.append((from_pillar, to_pillar))

    # It returns the number of steps from one pillar to another as per the value of n.
    def figure(self, a, b, c):
        fig = {}
        motion_count = len(self.motion)
        while motion_count - 1:
            current_from_pillar, current_to_pillar = self.motion[i]
            next_from_pillar, next_to_pillar = self.motion[i + 1]
            pillar_to_pillar = [(current_from_pillar, current_to_pillar), (current_to_pillar, next_from_pillar)]
            for current_motion in pillar_to_pillar:
                if current_motion not in fig:
                    fig[current_motion] = 0
                fig[current_motion] += 1
        current_motion = self.motion[motion_count - 1]
        if current_motion not in fig:
            fig[current_motion] = 0
        fig[current_motion] += 1
        return fig


def main():
    # making an object of class Issue() for accessing the members of class.
    issue = Issue()
    issue.resolving()


if __name__ == '__main__':
    sys.exit(main())
