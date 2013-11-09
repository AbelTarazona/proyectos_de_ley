# Ideas

* Nos gustaría que todo eso se refleje en una página independiente donde se listen todos los Proyectos de ley y los nombres completos.
* Ya si podría pasársele OCR automáticamente a todos sería un hit.

* Se me ocurre que este programa podría generar y actualizar una pagina web con la lista de proyectos de ley y con su información pertinente.
* Si en caso el OCR funciona bien, podría generarse una página para cada projecto, conteniendo el contenido del PDF en texto, o en todo caso el PDF mismo.
* Además al tener cada proyecto de ley como una pagina .html se podría generar un RSS feed para que los interesados se puedan subscribir al servicio.

# Dependencias
Estos scripts ha sido probados en una computadora usando Ubuntu 13.10 y
necesitan que las siguientes dependencias estén instaladas.

* Python
* pip: ``sudo apt-get install python-pip``
* bs4: ``sudo apt-get install python-bs4``
* requests: ``sudo apt-get install python-requests``

# Modo de ejecución

## script scrape.py

* El script ``scrape.py`` se encarga de cosechar la información del servidor del
congreso.
* Elabora un HTML con la lista de proyectos ``index.html``,
información básica (título, autores, código) y enlaces al expediente y PDF del
proyecto. 
* También descarga los PDFs y los almacena en el folder ``pdf/``.
* Toda la información cosechada se almancena en el archivo
  ``proyectos_data.json`` el cual actúa como "base de datos" (no es realmente
  base de datos). Este archivo permite llevar la cuenta de qué proyectos ya han
  sido procesados y se evitan procesarlos otra vez.

## script do_ocr.py
[We don't want OCR yet]

* El script ``do_ocr.py`` se encarga de convertir los PDFs del folder ``pdf/``
  a HTML previo proceso OCR usando ``tesseract``.
* También crea un ATOM Feed ``feed.xml`` conteniendo los proyectos de ley que
  han sido convertidos de PDF a HTML.
* Si un PDF ya ha sido procesado por OCR y convertido a HTML, este script
  evitará volverlo a procesar en futuras corridas.
* Los archivos HTML y el ``feed.xml`` son creados con info contenida en la
  "base de datos" ``proyectos_data.json``.

## plantilla HTML

* El archivo ``base.html`` funciona como plantilla para crear las páginas HTML.
  Cualquier cambio al estilo se debe realizar en este archivo. Esta plantilla
  usa un estilo basado en Twitter Bootstrap con *responsive features* para que
  se vea bien en computadoras y dispositivos móbiles.
* También se puede usar un HTML radicalmente diferente como plantilla. Pero es
  necesario que este archivo se llame ``base.html`` y tenga los siguientes
  campos:

     * ``{% titulo %}``
     * ``{% content %}``

* Esos campos se usan para introducir en contenido en la plantilla y generar
  los archivos HTML.




