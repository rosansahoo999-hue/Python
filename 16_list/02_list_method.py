marks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]


print(marks)
marks.append(63)    #  this will change the original list.
marks.pop()   # remove the last index elements
marks.extend(extra_marks)  # Join to list
marks.reverse()    # revers the list element
marks.sort()    # sort the less number to greater number
marks.insert(1, 99)  # insert the 1 index to put 99 number
print(marks) 