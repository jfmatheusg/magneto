# Magneto Challenge
Encuentre mutantes a partir de las cadenas de ADN

## ¿Cómo consumir las APIs?
<br>

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
<br>

### Stats
Endpoint: https://tsgdgidxc1.execute-api.us-east-1.amazonaws.com/Prod/stats

Method: GET

Responses:
HttpCode|Message
--------|--------
200|```{"count_mutant_dna":40,"count_human_dna":100, "ratio":0.4}```
<br>

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

[[https://github.com/jfmatheusg/magneto/blob/main/wiki/MercadoLibre.png]]
