# Seleccionar una imagen base con Python y Django instalado
FROM python:3.11-slim-buster

# Establecer el directorio de trabajo en el contenedor
WORKDIR /applications

# Copiar los archivos de tu proyecto local al contenedor
COPY . /applications

# Instalar las dependencias de tu proyecto
RUN pip install -r requirements.txt

# Configurar la variable de entorno para el proyecto de Django
ENV DJANGO_SETTINGS_MODULE=empleado.settings

# Exponer el puerto 8000 para recibir peticiones HTTP
EXPOSE 8000

# Ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "localhost:8000"]
