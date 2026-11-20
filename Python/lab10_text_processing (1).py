print("=" * 40)
print("TEXT PROCESSING TOOL".center(40))
print("=" * 40)

sentence = input("Enter a sentence: ")

print()
print("--- Processing Results ---")

pos = int(input("Enter position for indexing: "))
if 0 <= pos < len(sentence):
    print(f"{'Character at position ' + str(pos):<30}: '{sentence[pos]}'")
else:
    print("Position is out of range.")

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
sliced = sentence[start:end]
print(f"{'Sliced string [' + str(start) + ':' + str(end) + ']':<30}: '{sliced}'")

print(f"{'Uppercase':<30}: {sentence.upper()}")
print(f"{'Lowercase':<30}: {sentence.lower()}")

old = input("Enter word to replace         : ")
new = input("Enter replacement word        : ")
print(f"{'After replace':<30}: {sentence.replace(old, new)}")
print(f"{'Length of sentence':<30}: {len(sentence)}")

print()
print("=" * 40)
print("Analysis Complete!")
print("=" * 40)
