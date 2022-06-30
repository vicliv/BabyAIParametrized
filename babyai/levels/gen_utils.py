"""
Utilitary functions to use for level generation
"""

from babyai.minigrid.minigrid import IDX_TO_COLOR, IDX_TO_OBJECT, OBJECT_TO_IDX


def vector_to_dict(vector):
    dict = {}
    dict["agent"] = {}
    dict["agent"]["room"] = [vector[0], vector[1]]
    dict["agent"]["pos"] = [vector[2], vector[3]]
    dict["agent"]["dir"] = vector[4]

    dict["num_rows"] = vector[5] if vector[5] <= 3 else 3
    dict["num_columns"] = vector[6] if vector[6] <= 3 else 3
    dict["room_size"] = vector[7] if vector[7] <= 8 else 8

    dict["objects"] = []

    for i in range(8, 116, 6):
        object_dict = {}

        object_dict["i"] = vector[i]
        object_dict["j"] = vector[i+1]
        object_dict["type"] = IDX_TO_OBJECT[vector[i+2]]
        object_dict["color"] = IDX_TO_COLOR[vector[i+3]]
        object_dict["pos"] = [vector[i+4], vector[i+5]]

        dict["objects"].append(object_dict)
    
    dict["doors"] = []

    for i in range(117, 189, 6):
        door_dict = {}

        door_dict["i"] = vector[i]
        door_dict["j"] = vector[i+1]
        door_dict["idx"] = vector[i+2]
        door_dict["color"] = IDX_TO_COLOR[vector[i+3]]
        door_dict["locked"] = vector[i+4]
        door_dict["pos"] = vector[i+5]

        dict["doors"].append(door_dict)