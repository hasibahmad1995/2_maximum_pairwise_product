# def add(x,y):
#     return x + y
#
# m_input = input()
# y_input = input()
# print(add(int(m_input),int(y_input)))
#
# def Find_product(a):
#
#     mul = []
#     m = 1
#     for i in range(0,len(a)-1):
#         for k in range(m,len(a)):
#             mul.append(a[i]*a[k])
#         m+=1
#     return mul
# var = Find_product([5,6,2,7,4])
#
# max_value = var[0]
#
# for i in range(0,len(var),1):
#     if max_value<var[i]:
#         max_value = var[i]
#
# print(max_value)






# def Find_product(a):
#
#     mul = []
#     m = 1
#     for i in range(0,len(a)-1):
#         for k in range(m,len(a)):
#             mul.append(a[i]*a[k])
#         m+=1
#     return max(mul)
#
# given_values = []
# tot_val = 0
# while tot_val < 5:
#     values = int(input())
#     given_values.append(values)
#     tot_val+=1
# var = Find_product(given_values)
#
# print(var)

# def Find_product(a):
#
#     sorted_a = sorted(a)
#     return sorted_a[-1]*sorted_a[-2]
#
# given_values = []
# tot_val = 0
# while tot_val < 5:
#     values = int(input())
#     given_values.append(values)
#     tot_val+=1
# var = Find_product(given_values)
#
# print(var)


def Find_product(a):

    sorted_a = sorted(a)

    return sorted_a[-1]*sorted_a[-2]
elem = []
given_values = []
f = open("5.txt", "r")
for i in f:
    given_values.append(i.split())
for i in given_values[0]:
    elem.append(int(i))

var = Find_product(elem)

print(var)

def Find_product(a):

    mul = []
    m = 1
    for i in range(0,len(a)-1):
        for k in range(m,len(a)):
            mul.append(a[i]*a[k])
        m+=1
    return mul
elem = []
given_values = []
f = open("5.txt", "r")
for i in f:
    given_values.append(i.split())
for i in given_values[0]:
    elem.append(int(i))

var = Find_product(elem)

print(var)







