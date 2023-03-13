<p align="center">
<FONT FACE="times new roman" SIZE=5>
<br>
Ciencias de la computación e inteligencia artificial
<br>
<i><b>Big Data e Ingeniería de Datos</b></i>
<br>
<img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png"
width="150" height="150">
</img>
<br>
<i><b>Docente:</b></i><br> Camilo Rodriguez
<br>
<i><b>Autores:</b></i>
<br>
Johan Moreno
<br>
Erika Romero
<br>

# Parcial 1 
Este proyecto tiene como objetivo hacer web scraping a la pagina web: https://casas.mitula.com.co/searchRE/nivel1-Cundinamarca/nivel2-Bogot%C3%A1/nivel3-Chapinero/orden-0/q-bogota?req_sgmt=REVTS1RPUDtVU0VSX1NFQVJDSDtTRVJQOw== mediante las funciones de lambda de aws,  con el fin de extraer la informacion de las viviendas y guardarla en un archivo csv, desarrollando un pipeline de despliegue continuo con GitHubActions.

## Requerimientos
#### Cuenta AWS CLI
| Buckets S3 |  
| :-------- | 
|  S3 -> bucket: "casas-final-3003"|
|  S3 -> bucket: "landing-casas-3003"|

* Python 3.9
* Zappa
* Boto3
* BeautifulSoup
* Pytest
* Y demás se encuentran en los diferentes archivos requirements.txt


## Instalación

Clonación del repositorio, e ingrese a la carpeta creada

```bash
  git clone git@github.com:JohanPolar/PARCIAL-BD.git
  cd PARCIAL-BD/
```
    
Como se tienen 3 environments se debe
ingresar a cada carpeta y crear su ambiente definido 

```bash
    virtualenv -p python3.9 env
```
Activar el environment creado 
```bash
    source env/bin/activate
```
Instalación de requirements 
```bash
    pip install -r requierements.txt
```

Configuración de sus credenciales dentro de un archivo en una carpeta .aws situada en la raiz llamado credentials. 
  
# Desarrollo
  
Tener en cuenta, que dentro de los lambda creados ya esta definido que el lambda para capturar los datos se ejecute cada Lunes a las 9 am Hora colombiana
Si se quiere hacer uso de las demás funciones como: 

    - Revisión de código limpio con flake8
    - Ejecución de pruebas unitarias
    - Despliegue automático en AWS
    
Se ejecutan de manera automática por medio de un pipeline de despliegue continuo, donde al hacer cambios en alguno de los labda y hacer el zappa update dev se ejecutan en actions, para determinar que el código escrito tenga una sintaxis buena y entendible, siguiendo los parámetros de flake8. 
Se ejecutan pruebas unitarias determinando que cada uno de las funciones: 

    - Descargar html
    - Verificar que no se encuentre vació el html
    - Verificar que no se encuentre vació el csv generado

Se cumplan de manera afectiva. Para por ultimo realizar el cambio directamente en el lambda de aws

#### TENER EN CUENTA:
Se debe cambiar las variables privadas de GitHubActions, para que tenga el acceso a su cuenta de AWS y pueda realizar todas las acciones respectivas

## Insignias

[![Zappa License](https://img.shields.io/badge/License-Zappa-green)](https://github.com/zappa/Zappa/blob/master/LICENSE)

[![Flake8 License](https://img.shields.io/badge/License-Flake8-orange)](https://github.com/PyCQA/flake8/blob/main/LICENSE)

[![Pytest License](https://img.shields.io/badge/License-Pytest-red)](https://docs.pytest.org/en/7.1.x/license.html)

## Autores

- [@Johan Moreno](https://github.com/JohanPolar)
- [@Erika Romero](https://github.com/erika-romero)
