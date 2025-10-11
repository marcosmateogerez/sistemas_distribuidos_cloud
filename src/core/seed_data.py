from src.core.stage.model import Stage, CoverageRequest
from src.core.stage.model import status as status_stage
from werkzeug.security import generate_password_hash
from src.core.permission.model import Permission
from src.core.role.model import Role
from src.core.user.model import User
from src.core.database import db

def run():
    """
    Creación de las tablas iniciales.
    """

    # Crear roles.
    rol_ong_originante = Role(name="ONG originante")
    rol_ong_colaborativa = Role(name="ONG colaborativa")
    rol_consejo_directivo = Role(name="Consejo Directivo")
    rol_system_admin = Role(name="System Admin")

    # Agregar roles a la sesión.
    db.session.add(rol_ong_originante)
    db.session.add(rol_ong_colaborativa)
    db.session.add(rol_consejo_directivo)
    db.session.add(rol_system_admin)

    # Crear permisos para la ONG originante.
    permiso_ong_originante_upload_stage = Permission(name="upload_stage")
    permiso_ong_originante_list_observations = Permission(name="list_observations")
    permiso_ong_originante_upload_corrected_observation = Permission(name="upload_corrected_observation")

    # Crear permisos para la ONG colaborativa.
    permiso_ong_colaborativa_list_available_stages = Permission(name="list_available_stages")
    permiso_ong_colaborativa_subscribe_to_stage = Permission(name="subscribe_to_stage")
    permiso_ong_colaborativa_complete_stage = Permission(name="complete_stage")

    # Crear permisos para el Consejo Directivo.
    permiso_consejo_directivo_add_observation = Permission(name="add_observation")

    # Agregar permisos a la sesión.
    db.session.add(permiso_ong_originante_upload_stage)
    db.session.add(permiso_ong_originante_list_observations)
    db.session.add(permiso_ong_originante_upload_corrected_observation)
    db.session.add(permiso_ong_colaborativa_list_available_stages)
    db.session.add(permiso_ong_colaborativa_subscribe_to_stage)
    db.session.add(permiso_ong_colaborativa_complete_stage)
    db.session.add(permiso_consejo_directivo_add_observation)

    # Asignación de permisos al rol de ONG originante.
    rol_ong_originante.permissions.extend([
        permiso_ong_originante_upload_stage,
        permiso_ong_originante_list_observations,
        permiso_ong_originante_upload_corrected_observation
    ])

    # Asignación de permisos al rol de ONG colaborativa.
    rol_ong_colaborativa.permissions.extend([
        permiso_ong_colaborativa_list_available_stages,
        permiso_ong_colaborativa_subscribe_to_stage,
        permiso_ong_colaborativa_complete_stage
    ])

    # Asignación de permisos al rol de Consejo Directivo.
    rol_consejo_directivo.permissions.extend([
        permiso_consejo_directivo_add_observation
    ])

    # Guardo los cambios para que se le asigne un id a los roles y poder usarlo luego.
    db.session.commit()

    # Creación de usuario con el rol ONG originante.
    user_ong_originante = User(
        email="ong_originante@projectplanning.org",
        password=generate_password_hash("ong_originante"),
        role_id=rol_ong_originante.id
    )

    # Creación de usuario con el rol ONG colaborativa.
    user_ong_colaborativa = User(
        email="ong_colaborativa@projectplanning.org",
        password=generate_password_hash("ong_colaborativa"),
        role_id=rol_ong_colaborativa.id
    )

    # Creación de usuario con el rol Consejo Directivo.
    user_consejo_directivo = User(
        email="consejo_directivo@projectplanning.org",
        password=generate_password_hash("consejo_directivo"),
        role_id=rol_consejo_directivo.id
    )

    # Agregar usuarios a la sesión.
    db.session.add(user_ong_originante)
    db.session.add(user_ong_colaborativa)
    db.session.add(user_consejo_directivo)

    # Crear stages de ejemplo.
    stage_1 = Stage(
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
    
    # Agregar stages y observaciones a la sesión.
    db.session.add(stage_1)
    db.session.add(stage_2)
    db.session.add(stage_3)
    
    # Almacenamiento de las tablas en la base de datos.
    db.session.commit()
    print("Tablas creadas correctamente ✅.")