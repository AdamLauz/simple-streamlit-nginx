1. docker pull nginx:latest
2. docker tag nginx:latest my-local-nginx:latest
3. docker images
4. use "FROM my-local-nginx:latest" in Dockerfile
5. docker save -o nginx-local.docker  my-local-nginx:latest 
6. docker load -i nginx-local.docker
7. docker images
