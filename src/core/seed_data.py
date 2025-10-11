from src.core.database import db
from src.core.role.model import Role
from src.core.permission.model import Permission
from src.core.user.model import User
from src.core.stage.model import Stage, CoverageRequest
from src.core.observation.model import Observation 
from src.core.observation.model import Status as status_observation
from src.core.stage.model import status as status_stage

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

    #Creación de una stage de ejemplo
    stage_example = Stage(
        id_project=1,
        name="Etapa de ejemplo",
        description="Esta es una etapa de ejemplo para un proyecto.",
        start_date="2023-10-01 00:00:00",
        end_date="2023-12-31 23:59:59",
        coverage_request=CoverageRequest.DINERO,
        status=status_stage.PENDING
    )
    
    stage_2 = Stage(
        id_project=1,
        name="Etapa de ejemplo",
        description="Esta es una etapa de ejemplo para un proyecto 2.",
        start_date="2023-10-01 00:00:00",
        end_date="2023-12-31 23:59:59",
        coverage_request=CoverageRequest.MATERIALES,
        status=status_stage.PENDING
    )
    
    stage_3 = Stage(
        id_project=2,
        name="Etapa de ejemplo",
        description="Esta es una etapa de ejemplo para un proyecto 3.",
        start_date="2023-10-01 00:00:00",
        end_date="2023-12-31 23:59:59",
        coverage_request=CoverageRequest.MANO_DE_OBRA,
        status=status_stage.PENDING
    )
    # Agregar observación a la sesión.
    observation_example = Observation(
        id_project=1,
        name="Observación de ejemplo",
        description="Esta es una observación de ejemplo para un proyecto.",
        status=status_observation.PENDING
    )
    
    db.session.add(stage_example)
    db.session.add(stage_2)
    db.session.add(stage_3)
    db.session.add(observation_example)
    
    # Almacenamiento de las tablas en la base de datos.
    db.session.commit()
    print("Tablas creadas correctamente ✅.")