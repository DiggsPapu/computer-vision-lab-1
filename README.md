# computer-vision-lab-1

Computer Vision's lab 1

- Juan Luis Solorzano
- Diego Andrés Alonzo Medinilla 20172
- Arturo Argueta

## Montar el ambiente

```bash
docker build -t computer-vision-labs .
docker run --name computer-vision-labs --device /dev/video0 -p 8888:8888 -v "$(pwd):/app" computer-vision-labs
docker start -i computer-vision-labs
```

## Correr el Colour Detector

```bash
python ColourDetectorEx6.py
```
