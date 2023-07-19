# Telegram CC Scraper

Este proyecto es un scrapper de Telegram que extrae números de tarjetas de crédito (CCs) de los mensajes y los almacena en un archivo, al mismo tiempo que los envía a un chat específico.

<img src="https://brandslogos.com/wp-content/uploads/images/large/python-logo.png" width="150px">

## Funcionalidades

- Busca CCs en los mensajes y los guarda en un archivo, además de enviarlos a un chat o canal específico.
- Obtiene información adicional del BIN (Bank Identification Number) para cada tarjeta encontrada.
- Envía un mensaje con detalles de la tarjeta a un chat específico.

## Configuración

Antes de ejecutar el script, asegúrate de cumplir con los siguientes requisitos:

- Tener Python 3 instalado en tu sistema.
- Instalar las dependencias requeridas ejecutando el siguiente comando:

  ```
  pip install -r requirements.txt
  ```

Asegúrate de configurar las siguientes variables de entorno:

- `API_ID`: El ID de API para acceder a la API de Telegram. Puedes obtenerlo registrando una nueva aplicación en [https://my.telegram.org/apps](https://my.telegram.org/apps).
- `API_HASH`: El hash de API correspondiente al `API_ID`.
- `send_chat`: El chat de Telegram donde se enviarán los detalles de las tarjetas encontradas.
- `chats`: La lista de chats en los que se buscarán los mensajes.

## Nota

Las variables `send_chat` y `chats` se configuran en el archivo `main.py`.
Tambien recuerda que debes cambiar el nombre de `.env.example` a `.env` o crearlo directamente

## Uso

Para ejecutar el scrapper, simplemente ejecuta el siguiente comando:

```
python main.py
```

El script se conectará a Telegram y comenzará a escuchar los nuevos mensajes en los chats especificados. Cada vez que se encuentre una CC, se almacenará en un archivo llamado `ccs.txt` y se enviará un mensaje al chat especificado en `send_chat` con los detalles de la tarjeta.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, siéntete libre de crear un pull request con tus cambios.

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).
