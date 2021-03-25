# Magneto Challenge
Encuentre mutantes a partir de las cadenas de ADN

## ¿Cómo consumir las APIs?

### Mutant

Endpoint: https://tsgdgidxc1.execute-api.us-east-1.amazonaws.com/Prod/mutant

Method: POST

Payload:
```
{"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}
```
Responses:
HttpCode|Message
--------|--------
200|Mutant!
403|Forbidden

### Stats
Endpoint: https://tsgdgidxc1.execute-api.us-east-1.amazonaws.com/Prod/stats

Method: GET

Responses:
HttpCode|Message
--------|--------
200|```{"count_mutant_dna":40,"count_human_dna":100, "ratio":0.4}```

## ¿Cómo desplegar la solución?

En la ruta ```magneto-app``` realizar el build de los componentes:
```
sam build
```
Una vez se tenga el build realizar el deployment:
```
sam deploy
```

## ¿Cómo ejecutar las pruebas?

```
coverage run -m pytest
```

Si encuentra algun error de dependencias de python en su ambiente local, no olvide instalarlas:
```
pip install -r requirements.txt
```

## Arquitectura de solución

![Arquitectura](https://github.com/jfmatheusg/magneto/blob/main/wiki/MercadoLibre.png?raw=true)

Se decide utilizar solo servicios serverlesss de AWS para poder responder de manera rápida, costo-eficiente y sin requerimientos de administración a las variaciones de carga mencionada en el challenge (desde 100 hasta 1 millon de peticiones concurrentes).

Para el challenge se deja sin capacidad aprovisionada (On-Demand) para la tabla de DynamoDB pero para un escenario de implementación realista se podría configurar una capacidad mínima de lecturas/escrituras para atender las 100 peticiones concurrentes con un autoescalamiento de tal capacidad para poder llegar a atender el millón de peticiones.

Se elige utilizar python como lenguaje de programación por su bajo tiempo de cold start (ideal para el caso de autoescalamiento de funciones lambda) y por sus librerías de álgebra lineal para el manejo de la matriz de ADN
