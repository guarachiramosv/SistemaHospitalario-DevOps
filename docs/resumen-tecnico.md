# Resumen tecnico de fundamentos DevOps

## 1. DevOps y sus beneficios

DevOps es una forma de trabajo que une personas, procesos y tecnologia para entregar software con mayor rapidez, calidad y estabilidad. No se limita a una herramienta especifica; es una cultura de colaboracion entre desarrollo, operaciones, seguridad y calidad.

En un sistema hospitalario, DevOps ayuda a reducir errores porque cada cambio puede revisarse, probarse y registrarse antes de llegar a los usuarios. Tambien mejora la continuidad del servicio, algo importante en aplicaciones relacionadas con pacientes, personal medico, citas, historiales y administracion.

Sus beneficios principales son:

- Mayor colaboracion entre equipos.
- Entregas mas frecuentes y controladas.
- Menos errores manuales gracias a la automatizacion.
- Mejor trazabilidad de cambios mediante Git.
- Recuperacion mas rapida ante fallos.
- Mejora continua basada en metricas y retroalimentacion.

## 2. Planificacion agil con GitHub Projects

La planificacion agil permite organizar el trabajo en tareas pequenas, visibles y priorizadas. GitHub Projects facilita esta gestion mediante tableros tipo Kanban, donde las actividades pueden moverse entre estados como pendiente, en progreso y terminado.

Para un proyecto hospitalario, un tablero agil puede incluir tareas como crear el modulo de login, definir validaciones, escribir pruebas, configurar CI/CD y documentar el avance. Esta visualizacion ayuda a entender que falta, quien esta trabajando y que riesgos existen.

La planificacion agil tambien favorece la comunicacion. Las tareas pueden conectarse con issues, ramas y pull requests, de modo que cada cambio tecnico tenga contexto y seguimiento.

## 3. Control de versiones con Git y GitHub

Git es fundamental en DevOps porque permite registrar la evolucion del proyecto. Cada commit representa un cambio verificable y cada rama permite trabajar sin afectar directamente la version estable.

GitHub complementa Git al ofrecer un repositorio remoto, colaboracion, revision de cambios, pull requests y automatizaciones. En este proyecto se usa un flujo simple:

- `main` conserva la version estable.
- `develop` integra avances antes de pasar a estable.
- `feature/login` contiene el desarrollo del inicio de sesion.

El uso de ramas y commits descriptivos permite saber que cambio se hizo, cuando se hizo y por que se hizo. Esto reduce confusion y facilita la colaboracion.

## 4. Integracion y entrega continua

La integracion continua, o CI, consiste en validar automaticamente los cambios cada vez que se suben al repositorio. Su objetivo es detectar errores temprano, antes de que se acumulen o lleguen a una version principal.

En este repositorio, GitHub Actions ejecuta una prueba basica con Python. La prueba verifica que existan los archivos principales y que el formulario de login tenga campos de usuario, contrasena y boton de ingreso.

La entrega continua, o CD, extiende esta idea al preparar o desplegar artefactos de manera automatizada. En esta actividad no se despliega una aplicacion porque la consigna indica que basta con una prueba o compilacion simple. Aun asi, el pipeline deja preparada la base para agregar despliegues mas adelante.

## 5. Observabilidad y excelencia operativa

La observabilidad permite entender que esta ocurriendo dentro de una aplicacion mediante logs, metricas y trazas. En DevOps no basta con publicar software; tambien es necesario supervisarlo para detectar fallos, medir rendimiento y responder a incidentes.

En un sistema hospitalario, la observabilidad puede ayudar a identificar intentos fallidos de acceso, lentitud en servicios criticos, errores en consultas de datos o indisponibilidad de modulos. Esta informacion permite actuar rapido y mejorar la experiencia de los usuarios.

La excelencia operativa busca que el sistema sea confiable, seguro, facil de mantener y capaz de recuperarse ante problemas. DevOps apoya este objetivo mediante automatizacion, medicion, trabajo colaborativo y aprendizaje continuo.
