from app.wsgi import *
from erp.models import Type

# Listar: SELECT * FROM table
# query = Type.objects.all()
# print(query)

# Inserción
# t = Type()
# t.name = 'Directorio'
# t.save()

# Edición
# t = Type.objects.get(id=1)
# t.name = 'Invercionistas'
# t.save()

# Eliminación
# t = Type.objects.get(id=3)
# t.delete()

########
# obj = Type.objects.filter(name__endswith='e')
# print(obj)
