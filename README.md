# Sistema Distribuido de Constancias de No Adeudo

## Introducción
Este proyecto consiste en el desarrollo de un sistema distribuido para la emisión de constancias de no adeudo, utilizando una arquitectura basada en microservicios. Cada departamento de la institución (como Biblioteca, Escolares y Laboratorios) opera de manera independiente mediante servicios web que exponen información sobre el estado de adeudos de los estudiantes.

Un nodo principal, denominado Orquestador, se encarga de consultar todos los servicios en la red LAN y generar un resultado final indicando si el alumno puede obtener su constancia.

El sistema utiliza:
- Arquitectura de microservicios
- Comunicación HTTP/REST
- Formato de datos JSON
- Contenedores Docker
- Red de área local (LAN)

## Integrantes
- Abril Azeneth Quintas Rojas
- Alondra Galvan German 
- Heriberto Gómez Bolaina
- Mane Isabela Velasco Naranjo
- Nelida López Cruz

## Objetivo
Desarrollar un sistema distribuido funcional basado en microservicios, capaz de consultar y consolidar información de diferentes departamentos mediante comunicación HTTP/REST en una red local, utilizando contenedores Docker para garantizar portabilidad y consistencia en el despliegue.

## Requisitos
- Python 3.9+
- Docker instalado
- Conexión a la misma red LAN entre los equipos
- Navegador o Postman

## Infraestructura
- Nodo Principal (Orquestador): Centraliza las consultas y emite el veredicto final.
- Nodos Periféricos
  - Escolares
  - Biblioteca
  - Lab. Redes
  - Lab. Electrónica

## Estructura
proyecto/
│
├── orquestador/
│   ├── app.py
│   └── Dockerfile
│
├── biblioteca/
│   ├── app.py
│   └── Dockerfile
│
├── escolares/
│   ├── app.py
│   └── Dockerfile
│
├── lab_redes/
│   ├── app.py
│   └── Dockerfile
│
├── lab_electronica/
│   ├── app.py
│   └── Dockerfile
│
└── README.md 

## Licencia

Este proyecto está bajo la Licencia MIT.

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados, para utilizar el software sin restricción, incluyendo sin limitación los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del software.

El software se proporciona "tal cual", sin garantía de ningún tipo, expresa o implícita, incluyendo pero no limitado a garantías de comerciabilidad, idoneidad para un propósito particular y no infracción. En ningún caso los autores serán responsables de ningún reclamo, daño u otra responsabilidad derivada del uso del software.

Copyright (c) 2026 Abril, Alondra, Heriberto, Mane y Nelida.