# computer-vision-lab-1
Computer Vision's lab 1

## Montar el ambiente
```bash
docker build -t computer-vision-labs .
docker run --name computer-vision-labs -p 8888:8888 -v "$(pwd):/app" computer-vision-labs
docker start -i computer-vision-labs
```
