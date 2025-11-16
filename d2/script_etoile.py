import sys

# without argument, basic case
if len(sys.argv) < 2:
    filename = 'ex0.txt'
else:
    filename = sys.argv[1]

try:
    with open('./src/' + filename, 'r') as f:
        l = []
        for line in f:
            numbers = [int(x) for x in line.strip().split()]
            l.append(numbers)
except FileNotFoundError:
    print(f"Error: The file './src/{filename}' do not exist.")
    sys.exit(1)

if not l:
    print("Error: the folder is empty.")
    sys.exit(1)


def is_safe(report):
    if report[1] == report[0]:
        return False  
    
    if report[1] > report[0] :
        # case increasing
        for j in range (1, len(report)):
            if abs(report[j] - report[j-1]) > 3 :
                return False
            if report[j] <= report[j-1]:
                return False
    
    elif report[1] < report[0]:
        # case decreasing
        for j in range (1, len(report)):
            if abs(report[j] - report[j-1]) > 3 :
                return False
            if report[j] >= report[j-1]:
                return False
    return True


def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        # Create a new report without element at index i
        edited_report = report[:i] + report[i+1:]
        if is_safe(edited_report):
            return True
    
    return False


i = 0
nb_safe_report = 0
nb_unsafe_report = 0
nb_report = 0
empty_report = 0
report1elt = 0

while i < len(l):
    if len(l[i]) == 1:
        report1elt += 1
        i += 1
        continue
    if len(l[i]) == 0:
        empty_report += 1
        i += 1
        continue
    
    if is_safe_with_dampener(l[i]):
        nb_safe_report += 1
    else:
        nb_unsafe_report += 1
    
    nb_report += 1
    i += 1

print("Number of safe reports (with dampener): ", nb_safe_report)
print("Number of unsafe reports: ", nb_unsafe_report)
print("Total number of reports: ", nb_report)
print("Number of empty reports: ", empty_report)
print("Number of reports with only one element: ", report1elt)
