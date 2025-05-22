import platform

print(platform.machine()) # Returns the machine type

print(platform.node()) # Computer network name

print(platform.platform()) # Returns the value of the machine platform info

processorName = platform.processor()
print(processorName) # returns the real processor name

if processorName == "arm":
    print("Congratulations You are on Very Good machine ... ")
else:
    print(" sorry please use good machine to run the program ... ")

print(platform.python_version())

print(platform.python_build())

print(platform.python_branch()) # returns the pythin SCM branch

print(platform.python_compiler()) # Returns the compiler used compile the python

print(platform.python_revision()) # Returns the python implementation SCM Revision

print(platform.python_version()) # return python version as major.minor.patch level

print(platform.python_version_tuple())

print(platform.system())

print(platform.version())

print(platform.java_ver(release=''))

print(platform.mac_ver())

print(platform.node())

