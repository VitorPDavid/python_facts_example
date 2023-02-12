import argparse

from typing import Union

SchemaFact = tuple[str, str, str]
FactValue = Union[str, int]
Fact = tuple[str, str, FactValue, bool]


def write_facts_to_file(facts: list[Fact], file_path: str):
    with open(file_path, 'w') as f:
        for entity, attribute, value, op in facts:
            f.write(f'{entity}---{attribute}---{value}---{op}\n')


def get_schema_from_file(filepath: str) -> list[SchemaFact]:
    schema: list[SchemaFact] = []
    with open(filepath, 'r') as file:
        for line in file:
            values = line.rstrip('\n').split('---')
            schema.append((values[0], values[1], values[2]))

    return schema


def get_facts_from_file(filepath: str) -> list[Fact]:
    facts: list[Fact] = []
    with open(filepath, 'r') as file:
        for line in file:
            values = line.rstrip('\n').split('---')

            try:
                factValue = int(values[2])
            except ValueError:
                factValue = values[2]

            operation = values[3].lower() == 'true'

            facts.append((values[0], values[1], factValue, operation))

    return facts


def get_active_facts(facts: list[Fact],
                     schema: list[SchemaFact]) -> list[Fact]:
    active_entities_dict: dict[str, dict[str, Union[FactValue,
                                                    list[FactValue]]]] = {}

    for fact in facts:
        handle_fact(fact, schema, active_entities_dict)

    active_facts: list[Fact] = []

    for entity, attribute_dict in active_entities_dict.items():
        for attribute, values in attribute_dict.items():
            if isinstance(values, list):
                for value in values:
                    active_facts.append((entity, attribute, value, True))
            else:
                active_facts.append((entity, attribute, values, True))

    return active_facts


def handle_fact(fact: Fact, schema: list[SchemaFact],
                active_entities_dict: dict[str, dict[str,
                                                     Union[FactValue,
                                                           list[FactValue]]]]):
    is_many = attribute_is_many(fact[1], schema)
    if fact[3]:
        entity_dict = active_entities_dict.get(fact[0], {})

        if is_many:
            values: list[FactValue] = entity_dict.get(fact[1],
                                                      [])  # type: ignore
            values.append(fact[2])

            entity_dict[fact[1]] = values
        else:
            entity_dict[fact[1]] = fact[2]

        active_entities_dict[fact[0]] = entity_dict
    else:
        entity_dict = active_entities_dict.get(fact[0], {})

        if is_many:
            values: list[FactValue] = entity_dict.get(fact[1],
                                                      [])  # type: ignore
            values = list(filter(lambda x: x != fact[2], values))

            entity_dict[fact[1]] = values
        else:
            if fact[1] in entity_dict:
                entity_dict.pop(fact[1])

        active_entities_dict[fact[0]] = entity_dict


def attribute_is_many(attribute_name: str, schema: list[SchemaFact]) -> bool:
    for attribute, _, cardinality in schema:
        if attribute_name == attribute:
            return cardinality == 'many'

    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to generate active facts.')

    parser.add_argument('-scf', '--schema_file_path',
                        action='store',
                        default='./files/schema.txt',
                        type=str,
                        help='the path to the schema file.')

    parser.add_argument('-faf', '--facts_file_path',
                        action='store',
                        default='./files/facts.txt',
                        type=str,
                        help='the path to the facts file.')

    parser.add_argument('-of', '--output_file_path',
                        action='store',
                        default='./files/output.txt',
                        type=str,
                        help='the path to the output file.')

    args = parser.parse_args()

    schema = get_schema_from_file(args.schema_file_path)
    facts = get_facts_from_file(args.facts_file_path)

    active_facts = get_active_facts(facts, schema)

    write_facts_to_file(active_facts, args.output_file_path)
