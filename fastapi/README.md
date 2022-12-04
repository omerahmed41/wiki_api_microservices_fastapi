cd docker-fastapi-projects-nginx

docker build . -t nginx

# creates image in current folder with tag nginx

docker run --rm -it  -p 80:80/tcp nginx:latest

# runs nginx image

