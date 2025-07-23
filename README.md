#Django

1) Crear entorno con "python -m venv entorno"

2) Levantar el entorno "source entorno/bin/activate"

3) crear archivo "requirements.txt" y ahí escribir las librerias a incorporar, como Django y pillow

4) mandar a instalar las librerias con "pip install -r requirements.txt"

5) Crear proyecto Django con "django-admin startproject nombre ." 

6) Levantar el server con "python manage.py runserver"                         Para cerrar el server solo aplicar Ctrl+C en terminal

7) "Migracion es el proceso de incrustar los modelos de Django en una DB para que queden como tablas" Preparar migración con "python manage.py makemigrations"

8) Hacer migración con "python manage.py migrate"

9) Crear usuario con "python manage.py createsuperuser"

10) rellenar datos, solo es necesario nombre y password, por default serán user "admin" y pass "1234"

11) proyecto->settings.py->debajo de ALLOWED_HOSTS pegar "CSRF_TRUSTED_ORIGINS=["https://localhost:8000",]" esto permite habilitar que te conectes al proyecto, es por seguridad.

12) Crear app con "python manage.py startapp nombre"

13) En app->crear archivo urls.py // En proyecto->urls.py agregar path("", include(nombreapp.urls)),  // 
en proyecto->settings.py->INSTALLED_APPS agregar "nombreapp",//
finalmente en app->urls.py agregar lineas "from django.urls import path,include" y "urlpatterns = []" para manejar las urls de la app.

14) En app->views.py crear función (ejemplo) def hola(request): return render(request, "hola.html") //
 En app.urls.py agregar "from .views import hola// y en urlpatterns agregar: "path("", hola, name="hola"),//


15)  Crear  carpeta Templates y en proyecto->settings.py->DIRS agregar "[BASE_DIR / "Templates"]"//
Dentro de Templates crear hola.html
Dentro de hola.html usar "html:5" y ya se puede configurar la visual de la pagina 


16) Crear  modelo: en app->models.py crear clase 
class Producto(models.Model):
    nombre=models.CharField("nombre", max_lenght=50)
    descripcion=models.TextField("descripcion")
    precio=models.DecimalField("precio", max_digits=10, decimal_places=2)
    stock=models.PositiveBigIntegerField("stock", default=0)
    creado=models.DateTimeField("creado",auto_now_add=True)
    actualizado=models.DateTimeField("actualizado",auto_now=True)

    def __str__(self):
        return f"{self.nombre}"

17) Dado que se creo un modelo, se debe hacer la migración mediante:
    "python manage.py makemigrations mi_app"
    "python manage.py migrate"

18) Para hacer visible el nuevo modelo: En app->admin.py
    from .models import Producto
    @admin.register(Producto)
    class ProductoAdmin(admin.ModelAdmin):
        pass

19) Repitiendo los pasos anteriores, ahora se debe crear una ruta para los productos, por lo tanto
    En app->views.py crear función:
        def listar_productos(request):
            productos=Producto.objects.all()
            return render(request,"lista_de_productos.html", {"productos":productos})


    En app->urls.py->urlpatterns:
        *agregar listar_productos en "from .views..."*
        path("productos",listar_productos, name="listar_productos")

    En Templates:
        crear lista_de_productos.html (tiene que ser igual al link del return hecho en la función de views.py)
        dentro de lista_de_productos.html usar el "html:5"
       Para mostrar la tabla se debe: (en body)
       <h1>Productos</h1> (titulo opcional)
       {% for producto in productos %}
            {{producto.nombre}}
            {{producto.descripcion}}
            {{producto.precio}}
            {{producto.stock}}
            {{producto.creado}}
            {{producto.actualizado}}
        {% endfor %}

    Para mostrar bien la tabla, usaremos bootstrap y reemplazaremos lo anterior por:
        <h1>Productos</h1>
        {% for producto in productos %}
            <div class="card" style="width: 18rem;">
                <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">{{producto.nombre}}</h5>
                    <p class="card-text">Descripcion: {{producto.descripcion}}</p>
                    <p class="card-text">Precio: ${{producto.precio}}</p>
                    <p class="card-text">Stock: {{producto.stock}}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
            {{producto.creado}}
            {{producto.actualizado}}
        {% endfor %}


    