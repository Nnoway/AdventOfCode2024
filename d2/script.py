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

i=0
nb_safe_report=0
nb_unsafe_report=0
nb_report=0
empty_report = 0
report1elt = 0

while i < len(l):
    safe = True
    if len(l[i]) ==1 :
        report1elt += 1
        i += 1
        continue
    if len(l[i]) ==0 :
        empty_report += 1
        i += 1
        continue
    
    if l[i][1] == l[i][0]:
        # case stable
        nb_unsafe_report += 1

    elif l[i][1] > l[i][0] :
        # case increasing
        for j in range (1, len(l[i])):
            if abs(l[i][j] - l[i][j-1]) > 3 :
                nb_unsafe_report += 1
                safe = False
                break
                
            if l[i][j] <= l[i][j-1]:
                nb_unsafe_report += 1
                safe = False
                break
        
        if safe:
            nb_safe_report += 1
        

    elif l[i][1] < l[i][0] :
        # case decreasing
        for j in range (1, len(l[i])):
            if abs(l[i][j] - l[i][j-1]) > 3 :
                nb_unsafe_report += 1
                safe = False
                break

            if l[i][j] >= l[i][j-1]:
                nb_unsafe_report += 1
                safe = False
                break
        
        if safe:
            nb_safe_report += 1
        

    
    nb_report += 1
    i += 1

print("Number of safe reports : ", nb_safe_report)
print("Number of unsafe reports : ", nb_unsafe_report)
print("Total number of reports : ", nb_report)
print("Number of empty reports : ", empty_report)
print("Number of reports with only one element : ", report1elt)
