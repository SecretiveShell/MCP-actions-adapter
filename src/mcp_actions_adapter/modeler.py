from pydantic import BaseModel, create_model
from typing import Any, Dict, Type, Union, List

# Explicit mapping of JSON Schema types to Python types
JSON_SCHEMA_TYPE_MAPPING = {
    "string": str,
    "number": Union[int, float],
    "integer": int,
    "boolean": bool,
    "array": List[Any],
    "object": Dict[str, Any],
}


def get_tool_model(tool_name: str, input_schema: Dict[str, Any]) -> Type[BaseModel]:
    """
    Generate a Pydantic model dynamically based on the given tool's input schema.

    Args:
        tool_name (str): The name of the tool.
        input_schema (Dict[str, Any]): The tool's input schema, following JSON Schema format.

    Returns:
        Type[BaseModel]: A dynamically generated Pydantic model.
    """
    
    fields: Dict[str, tuple] = {}

    for name, schema in input_schema.items():
        schema_type = schema.get("type")
        if schema_type in JSON_SCHEMA_TYPE_MAPPING:
            field_type = JSON_SCHEMA_TYPE_MAPPING[schema_type]
            default_value = schema.get("default", ...)
            fields[name] = (field_type, default_value)

    return create_model(f"{tool_name}_Model", **fields) # type: ignore
