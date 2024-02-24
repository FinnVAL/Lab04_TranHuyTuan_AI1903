def count_lines_no_T(file_name):
    with open(file_name, 'r') as f:
        lines_no_T = sum(1 for line in f if not line.startswith('T'))
    return lines_no_T

file_name = "story.txt"
print("No of lines not starting with 'T' =",count_lines_no_T(file_name))