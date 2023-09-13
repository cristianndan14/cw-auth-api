# Utiliza la imagen base de Ubuntu 22.04
FROM ubuntu:22.04


ENV DEBIAN_FRONTEND=noninteractive
# Configura la zona horaria como variable de entorno
ENV TZ=America/Guayaquil

# Actualiza e instala paquetes necesarios
RUN apt-get update && \
    apt-get install -y python3-pip tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

# Crea el directorio de trabajo y copia los archivos necesarios
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copia el archivo requirements.txt y realiza la instalación de dependencias
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia el archivo access.json desde el directorio swagger_server/config en el contenedor
COPY swagger_server/config/access.json /usr/src/app/access.json

# Establece la variable de entorno ENVIRONMENT en "production"
ENV ENVIRONMENT=PROD

RUN mkdir -p /usr/src/app/logs
COPY . /usr/src/app

EXPOSE 2103

ENTRYPOINT ["python3"]
CMD ["-m", "swagger_server"]
