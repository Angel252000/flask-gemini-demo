# Flask + Gemini demo

Servidor Flask mínimo que expone un endpoint `/ask` para hacer consultas a un
modelo de Google Generative AI (Gemini). Reemplaza `TU_API_KEY_AQUI` en
`server.py` con tu propia clave de API antes de ejecutarlo; no subas tu clave
real a ningún repositorio.

```bash
pip install flask google-generativeai
python server.py
```

Por defecto corre solo en `127.0.0.1` y sin el depurador interactivo. Para
desarrollo local con recarga automática:

```bash
FLASK_DEBUG=1 python server.py
```

No actives `FLASK_DEBUG=1` si además cambias `FLASK_HOST` a algo distinto de
`127.0.0.1`: el depurador de Werkzeug permite ejecutar código arbitrario
desde el navegador a quien pueda alcanzar el servidor.
