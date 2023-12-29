from advent_of_code import helper
import pandas as pd

data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

data = helper.get_puzzle_input(d=3, y=2021)
# print('\n'.join(data))

ddata = []
for i, da in enumerate(data):
    temp = []
    for j, d in enumerate(da):
        temp.extend(d)
    for c, char in enumerate(temp):
        temp[c] = int(char)
    ddata.append(temp)

oxy_df = pd.DataFrame(ddata)
co2_df = pd.DataFrame(ddata)


def drop_values(df, oxy=True):
    for col in range(len(df.columns)):
        try:
            val_counts = df[col].value_counts().sort_index()

            ones = val_counts[1]
            zeros = val_counts[0]

            if oxy:
                delete_with = 0 if zeros < ones or zeros == ones else 1
            else:
                # co2 scrub
                delete_with = 1 if zeros < ones or zeros == ones else 0

            df[col].where(df[col] != delete_with, inplace=True)
            df.dropna(subset=[col], inplace=True)
        except KeyError:
            pass

    return df


oxy_calc = drop_values(oxy_df)
oxy_rating = int("".join([str(int(x)) for x in oxy_calc.values.flatten()]), 2)
print(f"Oxygen generator rating: {oxy_rating}")

co2_calc = drop_values(co2_df, False)
co2_rating = int("".join([str(int(x)) for x in co2_calc.values.flatten()]), 2)
print(f"Co2 scrubber rating: {co2_rating}")

print(f"Life support rating: {oxy_rating * co2_rating}")
