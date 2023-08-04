class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu1 = Cpu()
cpu2 = cpu1
print(cpu1)
print(cpu2)

disk = Disk()
computer1 = Computer(cpu1, disk)

import copy

computer2 = copy.copy(computer1)
print(computer1, computer1.cpu, computer1.disk)
print(computer2, computer2.cpu, computer2.disk)

computer3 = copy.deepcopy(computer1)
print(computer1, computer1.cpu, computer1.disk)
print(computer3, computer3.cpu, computer3.disk)
