import os
import platform
import subprocess

import cat_service


def main():
    print_header()
    output_path = get_or_create_output_folder()
    print(f'Found or created a folder at {output_path}')
    download_cats(output_path)
    display_cats(output_path)


def print_header():
    print('-----------------------------')
    print('        CAT FACTORY')
    print('-----------------------------')


def get_or_create_output_folder():
    base_dir = os.path.dirname(__file__)
    output_dir_name = 'cat_pictures'
    full_path = os.path.join(base_dir, output_dir_name)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating a new directory at {full_path}')
        os.mkdir(full_path)

    return full_path


def download_cats(output_dir):
    cat_count = 8
    print('Downloading LOL cat pictures ....')
    for i in range(1, cat_count+1):
        name = f'lolcat_{i}'
        print(f'downloading {name}')
        cat_service.get_cat(output_dir, name)
    print('Done!')


def display_cats(directory):
    print('Opening cat pictures directory ...')
    command = None
    platform_name = platform.system()
    if platform_name == 'Darwin':
        command = 'open'
    elif platform_name == 'Linux':
        command = 'xdg-open'
    elif platform_name == 'Windows':
        command = 'explorer'
    else:
        print(f'Sorry, we do not support your OS: {platform_name}')

    subprocess.call([command, directory])


if __name__ == '__main__':
    main()
