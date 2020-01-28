#login
docker login

#Pull docker
$docker pull subhani007/subhani_mt18117_a2

#Create a container in the local system
$docker run -itd --name=[name] subhani007/subhani_mt18117_a2 --- (By default latest tag is considered)

#Enter into the container created in the above step
$docker exec -it [name] /bin/bash

#copy from docker to host
$docker cp gpsr:/gpsr/1.py C:/Subhani/Desktop/

#Execute python files
Eg: $python3 2.py