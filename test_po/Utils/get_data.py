import yaml,os


def get_datas(path):
    with open(path,encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        add_data = data['add']
        return add_data

if __name__ == '__main__':
    # 获取父级目录
    current_path = os.path.dirname(os.path.dirname(__file__))
    # print(current_path)
    print(get_datas(f'{current_path}/data/data.yaml'))