# Take the string from the user

inp_str = input("Enter the String: ")
inp_str = inp_str.lower()

freq_counts = {}
for chr in inp_str:
    freq_counts[chr] = freq_counts.get(chr,0) + 1

print(f"Character Frequencies: {freq_counts}")