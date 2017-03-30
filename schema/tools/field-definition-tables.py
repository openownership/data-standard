#!/usr/bin/env python
import json
import csv
import collections
import re
import os

def format(text):
    return re.sub(r'\[([^\[]+)\]\(([^\)]+)\)', r'`\1 <\2>`__', text.replace("date-time","[date-time](#date)"))

def make_link(text):
    if "http" in text:
        return format("["+text.split("/")[-1]+"]("+text+")")
    else:
        text = text.replace("#/definitions/","")
        return format("["+text+"](#"+text.lower()+")")
        

def make_definition_table(json,file_path,what="properties",section=""): 
    table = [[_('Field Name'),_('Description'),_('Format')]]
    if(section):
        if "/" in section:
            try:
                block = json[what][section.split("/")[0]]["properties"][section.split("/")[1]]["properties"]
            except KeyError:
                block = json[what][section.split("/")[0]]["items"]["properties"]
        else:
            block = json[what][section]["properties"]
    else:
        block = json[what]

    
    for prop in block:
        types = block[prop].get('type','')
        if block[prop].get("enum") or block[prop].get("items",{}).get("enum"):
            types = types + (" enum (codelist)")
        if isinstance(types,list):
            types = format(", ".join(types).replace(", null","").replace("null,",""))
        else:
            types = format(types)

        types = types.replace("Reference","Object").strip()

        deprecated = " (DEPRECATED)" if "deprecated" in block[prop] else ""

        title = ""
        if "title" in block[prop]:
            title = format(block[prop].get('title','')) + deprecated + ": "

        description = title + format(block[prop].get('description',''))

        if block[prop].get("enum"):
            description = description + _(" Codelist options: [``") + "``, ``".join(block[prop].get("enum")) + "``]"

        if block[prop].get("items",{}).get("enum"):
            description = description + _(" Codelist options: [``") + "``, ``".join(block[prop].get("items",{}).get("enum")) + "``]"

        if types == "array":
           if block[prop].get('items').get("$ref"):
               table.append([prop,description + _(" See ") + make_link(block[prop]['items']["$ref"]) + _(" section for further details."),"Object Array"])
           else:
               table.append([prop,description,"Array"])
        elif block[prop].get("$ref"):
          table.append([prop,description + _(" See ") + make_link(block[prop]["$ref"]),"Object"])
        elif block[prop].get("oneOf"):
          table.append([prop,description + _(" One of ") + " or ".join([make_link(oneOf['$ref']) for oneOf in block[prop].get("oneOf")])])
        elif "object" in types:
            table.append([prop,description + _(" See ") + make_link(prop),"Object"])
        elif(block[prop].get('format','')):
          table.append([prop,description,block[prop].get('format','') + " " + types])
        else:
          table.append([prop,description,types])

        with open(file_path, 'w') as f:
            writer = csv.writer(f)
            for row in table:
                writer.writerow(row)


if __name__ == "__main__":
    from os.path import abspath, dirname, join
    import gettext


    schema_dir = dirname(dirname(abspath(__file__)))
    file_path = join(schema_dir,"../docs/_schema_tables/")
    language = os.environ.get("SCHEMA_LANG")
    if language:
        schema_dir = join(schema_dir, "../../build", language)
        fallback=False
    else:
        language = 'en'
        fallback=True

    translator = gettext.translation('schema', 'docs/locale', languages=[language], fallback=fallback)
    global _ 
    _ = translator.gettext

    
    with open(join(schema_dir, 'beneficial-ownership-statements.json'), 'r') as f:
        schema = json.loads(f.read(),object_pairs_hook=collections.OrderedDict)

    make_definition_table(schema,join(file_path,"statementGroup.csv"))

    make_definition_table(schema,join(file_path,"BeneficialOwnershipStatement.csv"),what="definitions",section="BeneficialOwnershipStatement")

    make_definition_table(schema,join(file_path,"Interest.csv"),what="definitions",section="Interest")

    make_definition_table(schema,join(file_path,"Share.csv"),what="definitions",section="Interest/share")

    make_definition_table(schema,join(file_path,"Annotation.csv"),what="definitions",section="Annotation")

    make_definition_table(schema,join(file_path,"EntityStatement.csv"),what="definitions",section="EntityStatement")

    make_definition_table(schema,join(file_path,"PersonStatement.csv"),what="definitions",section="PersonStatement")

    make_definition_table(schema,join(file_path,"NullParty.csv"),what="definitions",section="NullParty")

    make_definition_table(schema,join(file_path,"Address.csv"),what="definitions",section="Address")

    make_definition_table(schema,join(file_path,"Identifier.csv"),what="definitions",section="Identifier")

    make_definition_table(schema,join(file_path,"AlternateName.csv"),what="definitions",section="AlternateName")

    make_definition_table(schema,join(file_path,"Source.csv"),what="definitions",section="Source")

    make_definition_table(schema,join(file_path,"PersonStatementReference.csv"),what="definitions",section="PersonStatementReference")

    make_definition_table(schema,join(file_path,"EntityStatementReference.csv"),what="definitions",section="EntityStatementReference")


