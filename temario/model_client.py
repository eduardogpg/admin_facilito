Un modelo es la representación de los datos de nuestra aplicación. 
Contiene los campos básicos
y el comportamiento de los datos que serán almacenados. 
Por lo general, cada modelo se convierte en una tabla de la base de datos.

Lo fundamental

Cada modelo es una subclase de django.db.models.Model.
Cada atributo de un modelo representa a un campo de una tabla.
Django automáticamente nos da acceso a la base de datos.