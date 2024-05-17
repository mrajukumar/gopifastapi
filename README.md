command to run the container
docker run -itd --netrork="host" gopi
as we are not using any env file for caomtiner externally we are attaching the host network to connect to my sql  for api from inside the conatiner
hocalhost:80 to acces the api
