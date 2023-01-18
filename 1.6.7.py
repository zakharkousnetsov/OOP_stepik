# https://stepik.org/lesson/701975/step/8?unit=702076

class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.total_mem_slots = 4
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots[:self.total_mem_slots]

    def get_config(self):
        mp = 'Материнская плата: ' + self.name
        cp = 'Центральный процессор: ' + self.cpu.name + ', ' + str(self.cpu.fr)
        sp = 'Слотов памяти: ' + str(len(self.mem_slots))
        mem = [obj.name+' - '+str(obj.volume) for obj in self.mem_slots]
        #return [mp, cp, sp, 'Память: ' + '; '.join(mem)]
        return [f"Материнская плата: {self.name}",
                f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                f"Слотов памяти: {self.total_mem_slots}",
                'Память: ' + '; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]
                #f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"]

cpu = CPU('i7', 1234)
mem1 = Memory('mem1', 8)
mem2 = Memory('mem2', 4)

mb = MotherBoard('neim', cpu, mem1, mem2)

print(mb.get_config())