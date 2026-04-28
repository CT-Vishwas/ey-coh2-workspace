# Take the string from the user

inp_str = input("Enter the String: ")
inp_str = inp_str.lower()
# vishwasis

freq_counts = {}
# for chr in inp_str:
#     freq_counts[chr] = freq_counts.get(chr,0) + 1

for chr in inp_str:
    if chr not in freq_counts.keys():
        freq_counts[chr] = 0+1
    else:
        freq_counts[chr] = freq_counts[chr] + 1

print(f"Character Frequencies: {freq_counts}")