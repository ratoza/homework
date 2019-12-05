s = "azcbobobegghakl"
longest = ""
temp = ""

for i in s:
    if len(temp) == 0:
        temp += i
        continue
    if i >= temp[-1]:
        temp += i
    else:
        if len(temp) >= len(longest):
            longest, temp = temp, i

print(longest)