from enum import Enum


class AllureStory(str, Enum):
    LOGIN = 'LOGIN'

    GET_ENTITY = 'Get_entity'
    GET_ENTITIES = 'Get_entities'
    CREATE_ENTITY = 'Create_entity'
    UPDATE_ENTITY = 'Update_entity'
    DELETE_ENTITY = 'Delete_entity'
    VALIDATE_ENTITY = 'Validate_entity'
