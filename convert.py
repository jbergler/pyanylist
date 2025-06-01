import re
from urllib.request import urlopen

import json5


def json_to_proto(json_descriptor):
    proto = 'syntax = "proto3";\n\n'

    # Add package if present
    if "package" in json_descriptor:
        proto += f"package {json_descriptor['package']};\n\n"

    def convert_message(message_def):
        result = ""
        name = message_def["name"]
        result += f"message {name} {{\n"

        # Handle nested enums first
        if "enums" in message_def:
            for enum_def in message_def["enums"]:
                enum_lines = convert_enum(enum_def, indent="  ")
                result += enum_lines

        # Handle fields
        for field in message_def["fields"]:
            field_type = get_field_type(field)
            field_name = field["name"]
            field_id = field["id"]
            result += f"  {field_type} {field_name} = {field_id};\n"

        result += "}\n\n"
        return result

    def convert_enum(enum_def, indent=""):
        result = ""
        name = enum_def["name"]
        result += f"{indent}enum {name} {{\n"

        for value in enum_def["values"]:
            value_name = value["name"]
            value_id = value["id"]
            result += f"{indent}  {value_name} = {value_id};\n"

        result += f"{indent}}}\n\n"
        return result

    def get_field_type(field):
        type_map = {
            "double": "double",
            "float": "float",
            "int32": "int32",
            "int64": "int64",
            "uint32": "uint32",
            "uint64": "uint64",
            "sint32": "sint32",
            "sint64": "sint64",
            "fixed32": "fixed32",
            "fixed64": "fixed64",
            "sfixed32": "sfixed32",
            "sfixed64": "sfixed64",
            "bool": "bool",
            "string": "string",
            "bytes": "bytes",
        }

        field_type = type_map.get(field["type"], field["type"])

        # Handle field rules - note: proto3 doesn't use required/optional keywords
        # but we'll convert them appropriately
        rule = field.get("rule", "")
        if rule == "repeated":
            field_type = f"repeated {field_type}"
        # Note: proto3 doesn't have required/optional keywords, fields are optional by default

        return field_type

    # Process messages array (enums are handled within each message)
    if "messages" in json_descriptor:
        for message_def in json_descriptor["messages"]:
            proto += convert_message(message_def)

    return proto


def download_defs():
    data = urlopen("https://www.anylist.com/static/webapp/js/app.min.js")
    res = re.search(
        r'dcodeIO.ProtoBuf.newBuilder\({}\)\["import"\]\((.*?)\);', str(data.read())
    )
    return res.group(1)


# Usage
if __name__ == "__main__":
    raw_data = download_defs()
    json_data = json5.loads(raw_data)

    proto_content = json_to_proto(json_data)
    print(proto_content)
