---
name: avast-rompe-pip-y-python
description: "En el PC de Iván, Avast inspecciona HTTPS y rompe pip y otras descargas de Python (certificado y respuestas troceadas)"
metadata:
  node_type: memory
  type: project
  originSessionId: 4db748f8-8779-4c9c-9c47-43349b167e13
  modified: 2026-10-01T10:05:44.069Z
---

En el equipo de Iván (Windows 10), Avast Web/Mail Shield intercepta HTTPS y vuelve a firmar las conexiones con su certificado «Avast Web/Mail Shield Root». Comprobado el 2026-10-01 con `pypi.org`.

**Why:** explica dos fallos encadenados al instalar el MCP de DaVinci Resolve: (1) `pip` da `CERTIFICATE_VERIFY_FAILED` porque Python no confía en el certificado de Avast; (2) aun con `--use-feature=truststore`, las páginas de índice de PyPI llegan cortadas (`InvalidChunkLength`, y `curl` sale con código 56). Los instaladores que crean un venv y luego llaman a pip se quedan a medias sin avisar.

**How to apply:** ante cualquier `pip install`, descarga de modelos o instalador de Python que falle con errores de SSL o de conexión rota, sospechar de Avast antes que del paquete. Usar `pip --use-feature=truststore` para el certificado; si la conexión se sigue rompiendo, la salida es que Iván añada una excepción en Avast para `pypi.org` y `files.pythonhosted.org` (lo hace él, es configuración de seguridad). No usar `--trusted-host`. El Python del sistema es el de Microsoft Store (3.11) y ya tiene `mcp` 2.x, incompatible con servidores que piden `mcp<2`.
