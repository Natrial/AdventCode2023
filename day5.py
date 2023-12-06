soils = []
import os

absolute_path = os.path.dirname(__file__)
with open(absolute_path+"/day5.txt") as my_file:
    mapa=[]

    for line in my_file:
        if line[:5] == 'seeds':
            seeds=list(map(int, line[line.index(': ') +2:-1].split(" ")))
        elif line[0].isdigit():
            data=list(map(int, line.split(" ")))
            mapa.append(data)
        elif len(line)==1:
            soils.append(mapa)
            mapa = []
    
    soils.append(mapa)
soils.pop(0)

for i in range(len(soils)):
    for j in range(len(soils[i])):
        sourceRange = (soils[i][j][1],soils[i][j][1]+soils[i][j][2])
        destination = soils[i][j][0]
        transfromation=[]
        for k in range(len(seeds)):
            if isinstance(seeds[k], int) and seeds[k] >= sourceRange[0] and seeds[k] <= sourceRange[1]:
                #print(seeds[k], destination, soils[i][j][1],'inicio')
                #print(destination+seeds[k]-soils[i][j][1],'fin')
                seeds[k]=str(destination+seeds[k]-soils[i][j][1])
            
    seeds= list(map(int, seeds))

print('part 1: ',min(seeds))


def eval(lo, hi, mapping):
    res = []
    for mp in mapping:
        src_lo, dest, rng = mp
        src_hi = src_lo + rng - 1
        if lo < src_lo:
            if hi < src_lo:
                res.append((lo, hi))
                return res
            res.append((lo, src_lo-1))
            lo = src_lo
        if lo > src_hi:
            continue
        if hi <= src_hi:
            res.append((lo - src_lo + dest, hi - src_lo + dest))
            return res
        res.append((lo - src_lo + dest, src_hi - src_lo + dest))
        lo = src_hi + 1

    res.append((lo, hi))
    return res


def part2():
    with open(absolute_path+"/day5.txt") as f:
        text = f.read().split('\n\n')
    seeds = [*map(int, text[0].split()[1:])]
    mappings = [sorted([[int(line.split()[i]) for i in [1,0,2]] for line in mp.strip().split('\n')[1:]]) for mp in text[1:]]

    def find_min(pair, map_level):
        mapping = mappings[map_level]
        lo, hi = pair
        ranges = eval(lo, hi, mapping)
        if map_level == len(mappings) - 1:
            return ranges[0][0]
        return min([find_min(pair, map_level+1) for pair in ranges])

    seed_pairs = [(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds)-1, 2)]
    print(min([find_min(pair, 0) for pair in seed_pairs]))


part2()

