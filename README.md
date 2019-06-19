## Desplear aplicación Flask en Kubernetes
### Paso 1: Crear imagen de Docker
```
sudo docker build -t belem-project-img . 
```

```
sudo docker run --rm belem-project-img
```

### Paso 2: Probar que la app funciona correctamente en el contenedor
```
sudo docker ps
```
#### Obtienes los nombres de los contenedores que están corriendo
```
sudo docker exec -i -t <nombre_container> bash
```
# Aqui tiras tus curls a tus endpoints para probar que todo funcione e.g curl 0.0.0.0:8000/index

### Paso 3: Taggear la imagen y subirla al container registry
```
sudo docker tag belem-project-img gcr.io/anteater-dev-240619/belem-project-img:tag1
```
```
sudo docker push gcr.io/anteater-dev-240619/belem-project-img:tag1
```
### Paso 4: Crear deployment
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: belem-project
  labels:
    app: belem-project
spec:
  replicas: 1
  selector:
    matchLabels:
      app: belem-project
  template:
    metadata:
      labels:
        app: belem-project
    spec:
      containers:
      - name: belem-container
        image: gcr.io/anteater-dev-240619/belem-project-img:tag1
        ports:
        - containerPort: 8000
```

``` kubectl apply -f deployment.yaml
```

```
kubectl get deployments
```

```
kubectl get pods
```

### Paso 5: Crear Service
```
apiVersion: v1
kind: Service
metadata:
  name: belem-service
  labels:
    app: belem-project
spec:
  type: NodePort
  ports:
  - port: 8000
  selector:
    app: belem-project
```

```
kubectl get svc
```
#### Aqui podemos ingresar al pod y curlear la ip interna del service
```
kubectl get pods
```

``` 
kubectl exec -i -t nombre_del_pod bash
``` 

```
root@pod_name$ curl ip_interna/endpoint
```

### Paso 6: Crear ingress
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: belem-ingress

spec:
  rules:
  - host: belem.example.com
    http:
      paths:
        - path: /*
          backend:
            serviceName: belem-service
            servicePort: 8000
```

#### Esperar a que se cree el load balancer, una vez que tengamos una ip externa, agregar al archivo /etc/hosts de nuestra máquina local

```
ip_externa belem.example.com
```