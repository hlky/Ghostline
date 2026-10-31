"""Conservative classification of observed fact bindings, not engine defaults."""


def fact_name(data):
    value = data.get('factName')
    if isinstance(value, dict):
        value = value.get('$value')
    return value if isinstance(value, str) else ''


def fact_role(data):
    typ = data.get('$type')
    if typ == 'questSetVar_NodeType':
        return 'writers'
    if typ in {'questVarComparison_ConditionType', 'scnVarComparison_FactConditionTypeParams', 'GameplayFactCondition'}:
        return 'readers'
    # Achievement progress, photo-mode callbacks and braindance clue events
    # bind fact names too. Their fields alone do not establish a read/write
    # operation, so retain them without inventing a dataflow direction.
    return 'other_uses'
