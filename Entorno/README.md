Entorno / Pentesting API

Proyecto mínimo para probar una API de login y medir tiempos de un ataque por fuerza bruta controlado. Incluye:

main.py → API FastAPI (endpoints /login, /users, etc.).

Ataque2.sh → script Bash que realiza fuerza bruta por consulta HTTP.

graficos.py → script para graficar tiempos con matplotlib.

requirements.txt → dependencias.

Requisitos

Python 3.8+ (Windows: usar python; WSL: python3).

git, curl.

Entorno virtual recomendado.

Paquetes Python: fastapi, uvicorn[standard], sqlmodel, matplotlib.

Ejemplo mínimo requirements.txt:

fastapi
uvicorn[standard]
sqlmodel
matplotlib

Instalación (Windows / Git Bash o WSL)

En Git Bash o PowerShell (Windows):
cd /c/Users/TU_USUARIO/Desktop/Entorno
python -m venv venv
source venv/Scripts/activate    # Git Bash: . venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

En WSL / Linux:

cd ~/Entorno
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

Ejecutar la API

Dentro del entorno virtual:

# desde la carpeta que contiene main.py
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

Docs interactivos: http://127.0.0.1:8000/docs

Endpoint POST /login?username=bob&password=... devuelve JSON {"ok": true/false, "msg": ...}.

Si ejecutas en WSL y quieres acceder desde Windows usa --host 0.0.0.0 y la IP de WSL o 127.0.0.1 según configuración.

Probar con el script Bash (Ataque2.sh)

El script hace requests HTTP con curl al endpoint /login y mide tiempo y número de intentos.

Preparar y ejecutar:
# dar permiso (opcional)
chmod +x Ataque2.sh

# ejecutarlo (recomendado en WSL o Git Bash con curl disponible)
./Ataque2.sh

Contraseña Encontrada: 123
Número de intentos: 92123
Tiempo empleado: 92.30 segundos

El script usa date +%s.%N para medir tiempo. Eso mide tiempo real de pared y es sensible a carga del sistema.

alphabet="0123456789" y max_length=3 configuran el espacio de búsqueda.

Si corres en Windows nativo asegúrate de usar Git Bash o WSL porque el script emplea sintaxis Bash.

Generar el gráfico (graficos.py)

Instalado matplotlib, ejecutar:

python graficos.py


El script genera una ventana con el gráfico y guarda tiempos.png.

Justificación de las estadísticas (metodología)

Qué mide: el script mide el tiempo real (wall-clock) desde el primer intento hasta encontrar la contraseña. Además se cuenta el número de intentos (contador).

Por qué los tiempos varían:

Orden de búsqueda determinista. El script genera combinaciones en orden lexicográfico por longitud. Si la contraseña objetivo aparece tarde en ese orden entonces el tiempo será mayor.

Espacio de búsqueda. El número de combinaciones crece exponencialmente con la longitud y el tamaño del alfabeto.

Carga del sistema y latencia de red influyen en el tiempo absoluto.

Qué es reproducible:

El número de intentos hasta encontrar la contraseña es determinista dado el alphabet y max_length. Es la métrica más fiable para comparar casos.

El tiempo es reproducible aproximado pero puede variar por CPU, I/O, concurrencia y latencia.

Cómo justificar cifras del README / gráficos:

Si muestras 123 = 92.3s y 444 = 124.9s debes decir: “Tiempos medidos en N ejecuciones en entorno local; valores mostrados son de una ejecución representativa. El número de intentos fue X para 123 y Y para 444. Las diferencias se explican por la posición en el orden de prueba y por variación de latencia.”

Recomendación: para informe use medias de varias ejecuciones: t_prom = (t1 + t2 + ... + tn)/n y desviación estándar.