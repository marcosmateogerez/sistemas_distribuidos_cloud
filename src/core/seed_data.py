from src.core.database import db
from src.core.role.model import Role
from src.core.permission.model import Permission

def run():
    """
    Creación de las tablas iniciales roles y permisos.
    """

    # Crear roles.
    rol_ong = Role(name="ONG")
    rol_consejo = Role(name="Consejo Directivo")

    # Agregar roles a la sesión.
    db.session.add(rol_ong)
    db.session.add(rol_consejo)

    # Crear permisos.
    permiso_ong_index = Permission(name="ong_index")
    permiso_ong_contribute = Permission(name="ong_contribute")
    permiso_ong_accept_contribution = Permission(name="ong_accept_contribution")
    permiso_consejo_index = Permission(name="consejo_index")

    # Agregar permisos a la sesión.
    db.session.add(permiso_ong_index)
    db.session.add(permiso_ong_contribute)
    db.session.add(permiso_ong_accept_contribution)
    db.session.add(permiso_consejo_index)

    # Asignación de permisos al rol de ong.
    rol_ong.permissions.extend([
        permiso_ong_index,
        permiso_ong_contribute,
        permiso_ong_accept_contribution
    ])

    # Asignación de permisos al rol de consejo directivo.
    rol_consejo.permissions.extend([
        permiso_consejo_index
    ])

    # Almacenamiento de las tablas en la base de datos.
    db.session.commit()
    print("Tablas creadas correctamente ✅.")