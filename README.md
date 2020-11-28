# evaluacion_rg5

### Requerimientos:
- Docker
- Flask

Comando para crear imagen de docker
```
docker build -t evaluacion .
```

Commando para iniciar el contenedor dentro de la imagen, a manera de que corra con daemon, y de manera dinámica
```
docker run --name evaluacion_container -d -p 5050:5050 -v /rockstar/evaluacion/:/usr/src/app evaluacion
```


