import subprocess

image = input("input image name : ")
container = input("input container  name :")
ports  = input("input ports to be mapped : ")
detach  = input("Do you wnat to run in deatch mode , enter y/n  : ")

if detach == 'y':
    subprocess.call("docker run --name %s -p %s -d %s"%(container,ports,image),shell=True)
elif detach == 'n':
    subprocess.call("docker run --name %s -p %s %s"%(container,ports,image),shell=True)
else:
    print("Invalid option")
