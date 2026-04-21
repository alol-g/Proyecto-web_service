# Sistema Distribuido de Constancias de No Adeudo

## Introccion
Este proyecto consiste en el desarrollo de un sistema distribuido para la emisión de constancias de no adeudo, utilizando una arquitectura basada en microservicios. Cada departamento de la institución (como Biblioteca, Escolares y Laboratorios) opera de manera independiente mediante servicios web que exponen información sobre el estado de adeudos de los estudiantes.

## Integrantes
- Abril
- Alondra
- Heriberto
- Mane Isabela Velasco Naranjo
- Nelida

##Objetivo
Desarrollar un sistema distribuido funcional basado en microservicios, capaz de consultar y consolidar información de diferentes departamentos mediante comunicación HTTP/REST en una red local, utilizando contenedores Docker para garantizar portabilidad y consistencia en el despliegue.

#Infraestructura
- Nodo Principal (Orquestador): Centraliza las consultas y emite el veredicto final.
- Nodos Periféricos
  - Escolares
  - Biblioteca
  - Lab. Redes
  - Lab. Electrónica
