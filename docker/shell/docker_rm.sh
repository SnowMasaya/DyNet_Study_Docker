docker rm $(docker ps -aq)
docker rmi $(docker images | awk '/^<none>/ { print $3 }')
