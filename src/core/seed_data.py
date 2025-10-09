from src.core.database import db
from src.core.role.model import Role
from src.core.permission.model import Permission
from src.core.user.model import User
from werkzeug.security import generate_password_hash

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

    # Guardo los cambios para que se le asigne un id a los roles y poder usarlo luego.
    db.session.commit()

    # Creación de usuario con el rol ong.
    user_ong = User(
        email="ong@projectplanning.org",
        password=generate_password_hash("ong123"),
        role_id=rol_ong.id
    )

    # Creación de usuario con el rol consejo directivo.
    user_consejo = User(
        email="consejo@projectplanning.org",
        password=generate_password_hash("consejo123"),
        role_id=rol_consejo.id
    )

    # Agregar usuarios a la sesión.
    db.session.add(user_ong)
    db.session.add(user_consejo)

    # Almacenamiento de las tablas en la base de datos.
    db.session.commit()
    print("Tablas creadas correctamente ✅.")