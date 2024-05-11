grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

subject_sum=0
grade_sum=0

for i in range(20):
    subject = input()
    subject_list = subject.split()
    if subject_list[2] != 'P':
        subject_sum += float(subject_list[1]) * grade.get(subject_list[2], 0.0)
        grade_sum+=float(subject_list[1])


print('%.6f' % (subject_sum/grade_sum))