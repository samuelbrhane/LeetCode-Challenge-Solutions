def compress(l):
    if not l:
        return ""

    l.sort()
    result = ""
    
    first_val = l[0]

    for i in range(1, len(l)):
        if l[i] - l[i - 1] == 1:
            continue
        else:
            char_val = str(first_val)
            if l[i - 1] == first_val:
                char_val += ","
            else:
                char_val += f"-{l[i - 1]},"
            
            result += char_val

            first_val = l[i]
        

    last_num = l[len(l) - 1]

    if last_num == first_val:
        result += f"{last_num}"
    else:
        result += f"{first_val}-{last_num}"

    return result

# Given test cases
test_case_1 = [1, 4, 5, 2, 3, 9, 8, 11, 0]
test_case_2 = [1, 4, 3, 2]
test_case_3 = [1, 4]

output_1 = compress(test_case_1)
output_2 = compress(test_case_2)
output_3 = compress(test_case_3)

print(output_1, output_2, output_3)
