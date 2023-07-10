from json import load,dumps
from os.path import normpath,join


def filter_json(json_file_path :str,json_path_to_save:str,classes_to_filter : list):
    json_file_path = normpath(json_file_path)
    file = open(json_file_path)
    data = load(file)
    file.close()

    for annotation in data:
        objects = list()
        for object in annotation['Label']['objects']:
            if object['value'] in classes_to_filter:
                objects.append(object)
        annotation['Label']['objects'] = objects
    json_path_to_save = normpath(json_path_to_save)
    json_object = dumps(data, indent=4)
    with open(join(json_path_to_save, "Filtered_Final.json"), "w+") as outfile:
        outfile.write(json_object)
    return join(json_path_to_save, "Filtered_Final.json")


