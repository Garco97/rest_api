# REST API para ComparaSuper

## Uso


Todas las respuestas tendrán el siguiente formato

```json
{
    "data": "Tiene el contenido que se pide",
    "message": "Estatus del emnsaje"
}
```


### Lista todos los productos del usuario

**Definición**

`GET /products/<user-identifier>`

**Respuesta**

- `200 OK` cuando es correcta

**Argumentos**

- `"id":string` identificador global del cliente

```json
[
    {
        "id": "id",
        "name": "Ipad version 2018",
        "url": "link",
        "price": "700.0",
        "image":"image"
    },
    ...
]
```

### Registrar un nuevo producto

**Definición**

`POST /products`

**Argumentos**

- `"id":string` identificador global del producto (debería generarlo la BBDD)
- `"name":string` nombre completo del producto
- `"url":string` url de la dirección de Amazon
- `"price":string` precio
- `"image":string` imagen del producto

Si se añade un producto con un `id` existente, se sobreescribe

**Respuesta**

- `201 Created` cuando es correcto

```json
{
    "id": "id",
    "name": "Ipad version 2018",
    "url": "link",
    "price": "700.0",
    "image":"image"
}
```

## Mira los detalles del producto

`GET /product/<ID>`

**Respuesta**

- `404 Not Found` si el producto no existe
- `200 OK`  cuando es correcto

```json
{
    "id": "id",
    "name": "Ipad version 2018",
    "url": "link",
    "price": "700.0",
    "image":"image"
}
```

## Delete a product

**Definition**

`DELETE /products/<identifier>`

**Respuesta**

- `404 Not Found` si el producto no existe
- `204 No Content` cuando es correcto