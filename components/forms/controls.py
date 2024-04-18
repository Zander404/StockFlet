# Controle de cada classe instanciada para fazer alterações




global control_reference
control_reference = {}

def add_to_control_reference(key, value):
    global control_reference

    try:
        control_reference[key] = value
    except KeyError as e:
        print(e)
    finally:
        ...


def return_control_reference():
    global control_reference
    return control_reference