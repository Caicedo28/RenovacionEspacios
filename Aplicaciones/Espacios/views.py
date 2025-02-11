from django.shortcuts import redirect,render
from .models import AreaPublica
from .models import Proyecto, Contratista, Material

#importando django.countrib para mensajes de confirmacion 
from django.contrib import messages

#-------------------------------------------------Área Pública---------------------------------------------------
# Create your views here.

# Página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Presentando en pantalla el formulario de nuevo Área Pública
def nuevoAreaPublica(request):
    return render(request, 'nuevoAreaPublica.html')

# Presentando en pantalla el listado de Áreas Públicas
def listadoAreaPublica(request):
    areaBdd = AreaPublica.objects.all()
    return render(request, 'listadoAreaPublica.html', {'area': areaBdd})

# Capturando datos del formulario e insertando en la Bdd
def guardarAreaPublica(request):
    nombreAre = request.POST['txt_nombre']
    ubicacionAre = request.POST['txt_ubicacion']
    estadoAre = request.POST['select_estado']
    fecha_creacionAre = request.POST['txt_fecha']
    foto = request.FILES.get('txt_foto')  # Captura la foto si existe

    nuevoAreaPublica = AreaPublica.objects.create(
        nombreAre=nombreAre, 
        ubicacionAre=ubicacionAre, 
        estadoAre=estadoAre, 
        fecha_creacionAre=fecha_creacionAre,
        foto=foto
    )
    messages.success(request, "Área Pública Insertada Exitosamente")
    return redirect('/listadoAreaPublica')

# Función para eliminar un área pública por ID
def eliminarAreaPublica(request, idAre):
    eliminarArea = AreaPublica.objects.get(idAre=idAre)
    eliminarArea.delete()
    messages.success(request, "Área Pública Eliminada")
    return redirect('/listadoAreaPublica')

# Función para mostrar el formulario de edición de Área Pública
def editarAreaPublica(request, idAre):
    editarArea = AreaPublica.objects.get(idAre=idAre)
    return render(request, "editarAreaPublica.html", {'area': editarArea})

# Función para combinar cambios de área pública en la Bdd
def procesarEdicionAreaPublica(request):
    area = AreaPublica.objects.get(idAre=request.POST['idAre'])
    nombreAre = request.POST['txt_nombre']
    ubicacionAre = request.POST['txt_ubicacion']
    estadoAre = request.POST['select_estado']
    fecha_creacionAre = request.POST['txt_fecha']
    foto = request.FILES.get('txt_foto')  # Si se sube una nueva foto

    area.nombreAre = nombreAre
    area.ubicacionAre = ubicacionAre
    area.estadoAre = estadoAre
    area.fecha_creacionAre = fecha_creacionAre
    if foto:  # Si se ha proporcionado una nueva foto
        area.foto = foto

    area.save()
    messages.success(request, "Área Pública Editada Exitosamente")
    return redirect('/listadoAreaPublica')

#------------------------------------------------- Proyectos ---------------------------------------------------
# Presentando en pantalla el formulario de nuevo Proyecto
def nuevoProyecto(request):
    area=AreaPublica.objects.all()
    return render(request, 'nuevoProyecto.html',{
        'area':area,
    })

# Presentando en pantalla el listado de Proyectos
def listadoProyecto(request):
    proyectoBdd = Proyecto.objects.all()
    return render(request, 'listadoProyecto.html', {'proyecto': proyectoBdd})

# Capturando datos del formulario e insertando en la Bdd
def guardarProyecto(request):
    nombrePro = request.POST['txt_nombre']
    fecha_inicioPro = request.POST['txt_fecha_inicio']
    fecha_finPro = request.POST['txt_fecha_fin']
    estadoPro = request.POST['select_estado']
    presupuestoPro = request.POST['txt_presupuesto']
    area_id=request.POST['txt_nombreArea']
    foto = request.FILES.get('txt_foto')  # Captura la foto si existe
    area_publica=AreaPublica.objects.get(idAre=area_id)
    nuevoProyecto = Proyecto.objects.create(
        nombrePro=nombrePro,
        area_publica=area_publica,
        fecha_inicioPro=fecha_inicioPro,
        fecha_finPro=fecha_finPro,
        estadoPro=estadoPro,
        presupuestoPro=presupuestoPro,
        foto=foto
    )
    messages.success(request, "Proyecto Insertado Exitosamente")
    return redirect('/listadoProyecto')

# Función para eliminar un proyecto por ID
def eliminarProyecto(request, idPro):
    eliminarProyecto = Proyecto.objects.get(idPro=idPro)
    eliminarProyecto.delete()
    messages.success(request, "Proyecto Eliminado")
    return redirect('/listadoProyectos')

# Función para mostrar el formulario de edición de Proyecto
def editarProyecto(request, idPro):
    editarProyecto = Proyecto.objects.get(idPro=idPro)
    area=AreaPublica.objects.all()
    return render(request, "editarProyecto.html", {
        'proyecto': editarProyecto,
        'area': area,
        })

# Función para combinar cambios de proyecto en la Bdd
def procesarEdicionProyecto(request):
    proyecto = Proyecto.objects.get(idPro=request.POST['idPro'])
    nombrePro = request.POST['txt_nombre']
    area_id=request.POST['txt_nombreArea']
    fecha_inicioPro = request.POST['txt_fecha_inicio']
    fecha_finPro = request.POST['txt_fecha_fin']
    estadoPro = request.POST['select_estado']
    presupuestoPro = request.POST['txt_presupuesto']
    foto = request.FILES.get('txt_foto')  # Si se sube una nueva foto

    proyecto.nombrePro = nombrePro
    proyecto.area_id = area_id
    proyecto.fecha_inicioPro = fecha_inicioPro
    proyecto.fecha_finPro = fecha_finPro
    proyecto.estadoPro = estadoPro
    proyecto.presupuestoPro = presupuestoPro
    if foto:  # Si se ha proporcionado una nueva foto
        proyecto.foto = foto

    proyecto.save()
    messages.success(request, "Proyecto Editado Exitosamente")
    return redirect('/listadoProyecto')


#------------------------------------------------- Contratista ---------------------------------------------------

# Presentando en pantalla el formulario de nuevo Contratista
def nuevoContratista(request):
    return render(request, 'nuevoContratista.html')

# Presentando en pantalla el listado de Contratistas
def listadoContratista(request):
    contratistaBdd = Contratista.objects.all()
    return render(request, 'listadoContratista.html', {'contratista': contratistaBdd})

# Capturando datos del formulario e insertando en la Bdd
def guardarContratista(request):
    nombreCon = request.POST['txt_nombre']
    telefonoCon = request.POST['txt_telefono']
    emailCon = request.POST['txt_email']
    especialidadCon = request.POST['txt_especializacion']
    experienciaCon = request.POST['txt_experiencia']
    foto = request.FILES.get('txt_foto')  # Captura la foto si existe

    nuevoContratista = Contratista.objects.create(
        nombreCon=nombreCon, 
        telefonoCon=telefonoCon, 
        emailCon=emailCon, 
        especialidadCon=especialidadCon,
        experienciaCon=experienciaCon,
        foto=foto
    )
    messages.success(request, "Contratista Insertado Exitosamente")
    return redirect('/listadoContratista')

# Función para eliminar un contratista por ID
def eliminarContratista(request, idCon):
    eliminarContratista = Contratista.objects.get(idCon=idCon)
    eliminarContratista.delete()
    messages.success(request, "Contratista Eliminado")
    return redirect('/listadoContratista')

# Función para mostrar el formulario de edición de Contratista
def editarContratista(request, idCon):
    editarContratista = Contratista.objects.get(idCon=idCon)
    return render(request, "editarContratista.html", {'contratista': editarContratista})

# Función para combinar cambios de contratista en la Bdd
def procesarEdicionContratista(request):
    contratista = Contratista.objects.get(idCon=request.POST['idCon'])
    nombreCon = request.POST['txt_nombre']
    telefonoCon = request.POST['txt_telefono']
    emailCon = request.POST['txt_email']
    especialidadCon = request.POST['txt_especializacion']
    experienciaCon = request.POST['txt_experiencia']
    foto = request.FILES.get('txt_foto')  # Captura la foto si existe

    contratista.nombreCon = nombreCon
    contratista.telefonoCon = telefonoCon
    contratista.emailCon = emailCon
    contratista.especialidadCon = especialidadCon
    contratista.experienciaCon = experienciaCon
    if foto:  # Si se ha proporcionado una nueva foto
        contratista.foto = foto

    contratista.save()
    messages.success(request, "Contratista Editado Exitosamente")
    return redirect('/listadoContratista')

#-------------------------------------------------Material---------------------------------------------------

# Presentando en pantalla el formulario de nuevo Material
def nuevoMaterial(request):
    return render(request, 'nuevoMaterial.html')

# Presentando en pantalla el listado de Materiales
def listadoMaterial(request):
    materialesBdd = Material.objects.all()
    return render(request, 'listadoMaterial.html', {'material': materialesBdd})

# Capturando datos del formulario e insertando en la Bdd
def guardarMaterial(request):
    nombreMat = request.POST['txt_nombre']
    tipoMat = request.POST['select_tipo']
    unidadMat = request.POST['txt_unidad']
    costoMat = request.POST['txt_costo']
    cantidadMat = request.POST['txt_cantidad']

    nuevoMaterial = Material.objects.create(
        nombreMat=nombreMat,
        tipoMat=tipoMat,
        unidadMat=unidadMat,
        costoMat=costoMat,
        cantidadMat=cantidadMat
    )
    messages.success(request, "Material Insertado Exitosamente")
    return redirect('/listadoMaterial')

# Función para eliminar un material por ID
def eliminarMaterial(request, idMat):
    eliminarMaterial = Material.objects.get(idMat=idMat)
    eliminarMaterial.delete()
    messages.success(request, "Material Eliminado Exitosamente")
    return redirect('/listadoMaterial')

# Función para mostrar el formulario de edición de Material
def editarMaterial(request,idMat ):
    editarMaterial = Material.objects.get(idMat=idMat)
    return render(request, "editarMaterial.html", {'material': editarMaterial})

# Función para combinar cambios de material en la Bdd
def procesarEdicionMaterial(request):
    material = Material.objects.get(idMat=request.POST['idMat'])
    nombreMat = request.POST['txt_nombre']
    tipoMat = request.POST['select_tipo']
    unidadMat = request.POST['txt_unidad']
    costoMat = request.POST['txt_costo']
    cantidadMat = request.POST['txt_cantidad']

    material.nombreMat = nombreMat
    material.tipoMat = tipoMat
    material.unidadMat = unidadMat
    material.costoMat = costoMat
    material.cantidadMat = cantidadMat

    material.save()
    messages.success(request, "Material Editado Exitosamente")
    return redirect('/listadoMaterial')
