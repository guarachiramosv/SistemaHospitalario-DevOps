# Sistema Hospitalario - DevOps

Proyecto integrador para aplicar fundamentos de DevOps en un sistema hospitalario ficticio. La actividad demuestra el uso de Git, GitHub, ramas de trabajo, Pull Requests, documentacion tecnica e integracion continua con GitHub Actions.

## Objetivo

Simular el flujo de trabajo de un equipo que desarrolla un modulo de inicio de sesion para un sistema hospitalario. El proyecto organiza el trabajo con GitHub Flow, registra cambios mediante commits descriptivos y ejecuta una validacion automatica cada vez que se suben cambios al repositorio.

## Alcance del proyecto

- Crear documentacion tecnica sobre los modulos de DevOps estudiados.
- Implementar una pantalla basica de inicio de sesion para el sistema hospitalario.
- Mantener ramas `main`, `develop` y `feature/login`.
- Integrar la rama de funcionalidad hacia `develop`.
- Configurar un flujo CI/CD simple con GitHub Actions.

## Estructura

```text
.
|-- .github/workflows/ci.yml
|-- docs/
|   |-- reflexion-critica.md
|   `-- resumen-tecnico.md
|-- evidencias/
|   `-- microsoft-learn.png
|-- tests/
|   `-- test_project.py
|-- index.html
|-- login.html
`-- README.md
```

## Flujo de trabajo Git

- `main`: contiene la version estable del proyecto.
- `develop`: integra los avances aprobados.
- `feature/login`: contiene el desarrollo del modulo de inicio de sesion.

El flujo usado es:

1. Crear cambios en una rama de funcionalidad.
2. Validar los archivos con pruebas automaticas.
3. Fusionar la funcionalidad hacia `develop`.
4. Publicar las ramas en GitHub.

## Pipeline CI/CD

El archivo `.github/workflows/ci.yml` se ejecuta automaticamente en cada `push` y en cada `pull_request`. Su objetivo es validar que la estructura del proyecto exista y que los archivos HTML principales contengan los elementos esperados.

No se realiza despliegue porque la consigna solicita una prueba basica o compilacion simple como evidencia del uso de CI/CD.

## Evidencias publicadas

- Pull Request fusionado a `develop`: https://github.com/guarachiramosv/SistemaHospitalario-DevOps/pull/1
- Ejecucion exitosa de GitHub Actions: https://github.com/guarachiramosv/SistemaHospitalario-DevOps/actions/runs/34673683755
- PDF del portafolio: `output/pdf/portafolio-devops.pdf`

## Autor

Vania Guarachi Ramos
