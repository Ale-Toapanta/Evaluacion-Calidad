# 🕵️‍♂️ Misión: Operación Código Limpio (Python Edition)



**Tiempo estimado:** 90 minutos

Bienvenidos. El equipo anterior nos ha entregado un proyecto funcional, pero el código base acumula demasiada "deuda técnica". Su misión como desarrolladores asignados es implementar un flujo de trabajo profesional dividido en dos frentes: asegurar la integridad del código en la nube y auditar su calidad en sus entornos locales.

## 🎯 Objetivos de la Misión

### Frente 1: La Nube (GitHub Actions)
1. Haz un **Fork** de este repositorio hacia tu cuenta personal de GitHub y clónalo en tu computadora.
2. Crea el directorio y archivo `.github/workflows/python-ci.yml`.
3. Configura un pipeline que se dispare al hacer `push` a la rama `main`. Este pipeline debe:
   - Instalar las dependencias (`pip install -r requirements.txt`).
   - Ejecutar las pruebas unitarias usando `pytest`.
4. **El Huevo de Pascua:** Agrega un paso final en tu archivo YAML llamado "Sello de Victoria" que use el comando `echo` para imprimir una figura en Arte ASCII en los logs (un trofeo, un gato, un cohete, etc.). Este paso **solo debe ejecutarse** si `pytest` pasa exitosamente sin errores.

### Frente 2: El Cuartel Local (SonarQube)
1. En la raíz de tu proyecto local, crea el archivo `sonar-project.properties`. Define la llave del proyecto, el nombre, la exclusión de archivos de prueba (`sonar.exclusions=test_app.py`) y la ruta de los archivos fuente.
2. Enciende tu servidor local de SonarQube (`localhost:9000`).
3. Ejecuta el comando `sonar-scanner` en tu terminal para enviar el código a auditar.

### Frente 3: La Purgación (Refactorización)
1. Abre tu dashboard de SonarQube e identifica los *code smells* y problemas reportados en `app.py`.
2. Refactoriza el código de Python: elimina código muerto o no utilizado, mejora el nombramiento de variables, simplifica la lógica de los condicionales y atrapa las excepciones correctamente. **¡Asegúrate de no romper la lógica de las pruebas unitarias!**
3. Vuelve a correr `sonar-scanner` de forma iterativa hasta que el *Quality Gate* pase a estado **"Passed" (Verde)**.
4. Haz `push` a GitHub para verificar que tus cambios pasen las pruebas en la nube y logres visualizar tu Arte ASCII.

### Frente 4: El Reporte Final
1. Genera el *Badge* de estado desde tu SonarQube y colócalo en la parte superior de este `README.md` (reemplazando el comentario HTML).
2. Toma una captura de pantalla de tu dashboard de SonarQube mostrando el Quality Gate en "Passed" y el nivel de deuda técnica resuelto.
3. Sube la imagen a tu repositorio e inclúyela al final de este documento con una breve conclusión de 2 a 3 líneas sobre las mejoras estructurales que le aplicaste al código original.

---

## 📊 Rúbrica de Evaluación (10 Puntos)

| Criterio | Logro a Evaluar | Puntaje |
| :--- | :--- | :---: |
| **Pipeline en la Nube (CI)** | El archivo de GitHub Actions ejecuta correctamente `pytest` en cada *push* y las pruebas pasan exitosamente con el código refactorizado. | 2.5 pts |
| **El Huevo de Pascua** | Se evidencia en los logs de ejecución de GitHub Actions la figura en Arte ASCII configurada al final del pipeline. | 1.5 pts |
| **Integración Local** | El archivo `sonar-project.properties` está correctamente configurado para Python y el escáner logra comunicarse con el servidor local. | 2.0 pts |
| **Calidad de Código** | El repositorio muestra el *Badge* en el README y la captura evidencia el *Quality Gate* en estado "Verde", demostrando la eliminación exitosa de los *code smells*. | 4.0 pts |
