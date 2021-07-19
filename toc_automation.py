import os
import yaml

folder_list = os.listdir("content/Code Gallery")
# print(folder_list)

def toc_write(directory):
    with open('_toc.yml', 'w') as parsed_yaml_file:
        # document = """
        #         a: 1
        #         b:
        #             c: 3
        #             d: 4
        #         """
        yaml.dump([{'status': 4, 'language': 'Python', 'name': 'PyYAML', 'license': 'MIT'},
{'status': 5, 'license': 'BSD', 'name': 'PySyck', 'language': 'Python'}], parsed_yaml_file, default_flow_style = False)



toc = open("_toc.yml") 
parsed_yaml_file = yaml.load(toc, Loader=yaml.FullLoader)
content_list = parsed_yaml_file.get("parts")
for content in content_list:
    for files in content_list:
        len_files = len(files)
        # print(files["chapters"][2]["file"])
        for i in range(0, len_files+1):
            directory = files["chapters"][i]["file"]
            if directory.split("/")[2]  in folder_list:
                print(directory.split("/")[2])
                test = toc_write(directory)
        break
    break

