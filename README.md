# pda_servicio_contratos
Servicio de PDA que se utiliza para el registro de información.

## debe tener un archivo .env
tomar el archivo .env.example y renombrarlo .env, luego se deben colocar las variables correctas

## levantar la base de datos
el docker ya lee de variables de entorno si y solo si el archivo se llama .env, por lo tanto el paso anterior ya debe estár completado
```python
docker-compose -f "docker-compose.yml" up
```

## levantar Apache pulsar
Ingresar a la carpeta ./pulsar y subir el broker a través del docker compose
```python
cd pulsar
docker-compose -f "docker-compose.yml" up
```

## ejecutar el servidor
se deben cargar las variables de entorno en el ambiente
```python
export $(cat .env)
```
Luego se procede a levantar el servidor
```python
flask --app src/contractual/api run -p 3000
```

## endpoint para probar comando y evento al crear un arrendamiento

endpoint: http://localhost:3000/async-contrato

tipo: POST
body
```json
{
    "propiedad_id": "46",
    "numero_contrato": "ABCD1234",
    "fecha_actualizacion": "04/03/2024",
    "fecha_creacion": "04/03/2024"
}
```

## Contribución

Daniel ochoa