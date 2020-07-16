import sys
from Calcu import GCD

class continuedFrac:

    def __init__(self, nume, deno):
        assert GCD(nume, deno) == 1
        self.nume = nume
        self.deno = deno
        self.a_arr = []
        self.p_arr = []
        self.q_arr = []
        self.a_gen()
        self.pq_gen()

    def _a_calcu(self, nume, deno, arr):
        if deno == 1:
            arr.append(nume)
        else:
            arr.append(nume // deno)
            self._a_calcu(deno, nume % deno, arr)

    def a_gen(self):
        self._a_calcu(self.nume, self.deno, self.a_arr)

    def pq_gen(self):
        '''
        p_0 = a_0   p_1 = a_0*a_1 + 1
        q_0 = 1     q_1 = a_1
        '''
        self.p_arr = [self.a_arr[0], self.a_arr[0]*self.a_arr[1]+1]
        self.q_arr = [1, self.a_arr[1]]
        for i in range(2, self.a_arr.__len__()):
            '''
            p_i = a_i*p_{i-1} + p_{i-2}
            q_i = a_i*q_{i-1} + q_{i-2}
            '''
            self.p_arr.append(self.a_arr[i]*self.p_arr[i-1]+self.p_arr[i-2])
            self.q_arr.append(self.a_arr[i]*self.q_arr[i-1]+self.q_arr[i-2])


def main(argv):
    obj = continuedFrac(int(argv[0]), int(argv[1]))
    print(argv[0]+"/"+argv[1]+"'s abbreviated notation is", obj.a_arr)
    print("and nume arr is", obj.p_arr)
    print("    deno arr is", obj.q_arr)

if __name__ == "__main__":
    main(sys.argv[1:])
