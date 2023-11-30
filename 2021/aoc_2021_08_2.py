import helper

data = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]
data = helper.get_puzzle_input(d=8, y=2021)
data = [x.split(" | ") for x in data]


def jn_sort(something):
    return "".join(sorted(something))


def seq_in_seqs(seq, seqs):
    for i, n in enumerate(seqs):
        diff = set(seq).difference(set(n))
        if not diff:
            del seqs[i]
            return jn_sort(n)


def seq_in_seqs_least_diff(seq, seqs):
    diffs = {}
    for i, n in enumerate(seqs):
        diff = set(seq).difference(set(n))
        diffs[len(diff)] = [i, n]

    del seqs[sorted(diffs.items())[0][1][0]]
    return jn_sort(sorted(diffs.items())[0][1][1])


result = 0

for lll, line in enumerate(data):
    numbers = [""] * 10

    # NUMBERS 1, 4, 7 & 8
    for i, num in zip([1, 4, 7, 8], [2, 4, 3, 7]):
        foo = [x for x in line[0].split() if len(x) == num][0]
        numbers[i] = "".join(sorted(foo))

    five_seg = [x for x in line[0].split() if len(x) == 5]
    six_seg = [x for x in line[0].split() if len(x) == 6]

    numbers[3] = seq_in_seqs(numbers[7], five_seg)
    numbers[9] = seq_in_seqs(numbers[3], six_seg)
    numbers[0] = seq_in_seqs(numbers[7], six_seg)
    numbers[6] = jn_sort(six_seg[0])
    del six_seg

    numbers[5] = seq_in_seqs_least_diff(numbers[6], five_seg)
    numbers[2] = jn_sort(five_seg[0])
    del five_seg

    out = []
    output_sequence = line[1].split()
    for mess in output_sequence:
        sort = jn_sort(mess)
        if sort in numbers:
            out.append(numbers.index(sort))

    out_value = int("".join([str(x) for x in out]))
    # print(' '.join(numbers), ':', out_value)
    result += out_value

print(f"Puzzle answer: {result}")
