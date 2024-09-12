print("Welcome to Data Structure Programming")
cloud_vm = ['vm1','vm2','vm3','vm4']  # list of vm
print("list of cloud vm")
print(cloud_vm)
# print(type(cloud_vm))
# help(cloud_vm)
print(cloud_vm[0])  # Access first element of cloud_vm list
cloud_vm[2] = 'virtual_machine3'
print(cloud_vm)
cloud_vm.insert(2,'vm3')
print("Updated cloud vm list",cloud_vm)

# stack operation on cloud_vm list
cloud_vm.append('vm5')
print("Updated cloud vm list",cloud_vm)
cloud_vm.append('vm6')
print("Updated cloud vm list",cloud_vm)
cloud_vm.append('vm7')
print("Updated cloud vm list",cloud_vm)
cloud_vm.append('vm8')
print("Updated cloud vm list",cloud_vm)
cloud_vm.append('vm9')
print("Updated cloud vm list",cloud_vm)
cloud_vm.pop()

# Perform Queue operation First In First Out
print("Updated cloud vm list",cloud_vm)
cloud_vm.pop(0)
print("Updated cloud vm list",cloud_vm)
cloud_vm.pop(0)
print("Updated cloud vm list",cloud_vm)
cloud_vm.remove('vm6')
print("Updated cloud vm list",cloud_vm)
# Sort cloud_vm list
cloud_vm.sort() # Ascending order
print("Sorted vm",cloud_vm)

cloud_vm.sort(reverse=True) # Descending order

print("Sorted vm in Descending Order",cloud_vm)

cloud_vm1 = ['s1','s2','s3','s4']

# Extend existing cloud_vm by cloud_vm1

cloud_vm.extend(cloud_vm1)

print("Extended cloud_vm", cloud_vm)

cloud_vm2 = cloud_vm.copy()

print(cloud_vm2)

print(cloud_vm[-1:-5:-1]) # Negative indice to access last element of list

print(cloud_vm[-1:-10:-2])

print(list(range(0,10)))


