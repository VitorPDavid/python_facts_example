# FACTS-CHALLENGE

## Description

Considering a data model that uses tuples to represent its data, that tuple is named Fact in this context.

fact example:

```python
# ('entity', 'attribute', 'value', 'operation')
('joão', 'age', 18, True)
```

> In this example, the entity(E) "joão" as the attribute(A) "age" with the "value"(V): 18.<br>
> The last fact's element: operation(OP) "True", representes whether the fact is a add or remove operation

Multiple facts example:

```python
facts = [
    ('gabriel', 'address', 'av rio branco, 109', True),
    ('joão', 'address', 'rua alice, 10', True),
    ('joão', 'address', 'rua bob, 88', True),
    ('joão', 'phone_number', '234-5678', True),
    ('joão', 'phone_number', '91234-5555', True),
    ('joão', 'phone_number', '234-5678', False),
    ('gabriel', 'phone_number', '98888-1111', True),
    ('gabriel', 'phone_number', '56789-1010', True),
]
```

Same as other data models the attributes has cardinality, that can be 1(one) or N(many)

Facts that represent information about attributes are named "schema facts", here is an example of a schema that indicates attributes information:

```python
schema = [
    ('address', 'cardinality', 'one'),
    ('phone_number', 'cardinality', 'many')
]
```

> for this challenge the unique possible fact schema attribute is "cardinality".

For example, this is the historical facts about the attribute "address" and entity "joão" using this schema example:

```python
[
    ('joão', 'address', 'rua alice, 10', True)
    ('joão', 'address', 'rua bob, 88', True),
]
```

the active fact is the last added:

```python
('joão', 'address', 'rua bob, 88', True)
```

To remove values about an entity, the last fact element must be "False", indicating that fact must be removed whether exists in the history facts, otherwise, must be ignored.

For example, use these facts to indicate the historical facts about an entity "joão":

```python
[
    ('joão', 'phone_number', '234-5678', True),     # 1° number added
    ('joão', 'phone_number', '91234-5555', True),   # 2° number added
    ('joão', 'phone_number', '234-5678', False),    # 1° number removed
]
```

Assuming that the schema indicates that "phone_number" has cardinality many, the first fact adds the phone_number "234-5678" to joão, the second add the phone_number "91234-5555" to joão and the last one remove the phone_number "234-5678" from joão.

So active facts are:

```python
[
    ('joão', 'phone_number', '91234-5555', True),
]
```

## Instructions

Your objective in this challenge is to write a function that returns the active facts. This function must receive the ordered historical facts and the schema as arguments.

Premises:

- the historical facts list is ordered from oldest to newest fact.
- Cardinality must be one or many.
- All facts are a tuple with the structure: and schema facts:
  - facts tuples = (E, A, V, OP)
  - schema tuples = (E, A, V)

- All entities, attributes, or values don't have a "---" substring.

Input

- The input is two files: facts.txt and schema.txt, both in UTF-8.
- Every line on facts.txt as one fact, with the format: entity---attribute---value---operation
- Every line on schema.txt as one fact schema, with the format: attribute---cardinality---cardinality_type

Output

The output must be a text on the console with each line being an active fact in the format entity---attribute---value---operation using "---" as a separator.

### Example

| input example                                                                                                                                                                                                                                                                                                                                                                                                                                                      | output example                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **facts.txt**<br>gabriel---address---av rio branco, 109---True<br>joão---address---rua alice, 10---True<br>joão---address---rua bob, 88---True<br>joão---phone_number---234-5678---True<br>joão---phone_number---91234-5555---True<br>joão---phone_number---234-5678---False<br>gabriel---phone_number---98888-1111---True<br>gabriel---phone_number---56789-1010---True<br><br>**schema.txt**<br>address---cardinality---one<br>phone_number---cardinality---many | **output**<br>gabriel---address---av rio branco, 109---True<br>joão---address---rua bob, 88---True<br>joão---phone_number---91234-5555---True<br>gabriel---phone_number---98888-1111---True<br>gabriel---phone_number---56789-1010---True<br>|
