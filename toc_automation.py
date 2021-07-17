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
        yaml.dump({'test': {'hp': 34, 'sp': 8, 'level': 4}, "test": directory ,  'test': {'hp': 12, 'sp': 0, 'level': 2}}, parsed_yaml_file, default_flow_style = False)



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

