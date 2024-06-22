import os
import subprocess
import sys
import venv

# -------------------- You can customize the settings bellow --------------------

# You can customize the 'dependencies' dict with the dependencies to be installed:
dependencies = ('MyPy', 'numpy', 'Typer')

# You can customize the 'project_folders' tuple:
# A tuple of strings means a parent directory, a child directory, so on and so forth.
project_folders = (
    ('templates', 'static'),
    'media'
)

# -------------------- You can customize the settings above --------------------


parent_dir = os.path.dirname(os.getcwd())
project_question = f"\n\tName your project to be created in '{parent_dir}' folder ('exit' to quit): "


def get_folder_name(parameter):  # Used twice to get project and app names
    while True:
        try:
            new_folder = os.path.join(parent_dir, input(f"{parameter}").strip().replace(' ', '_'))
            if new_folder.lower() == 'exit':
                print('\n\tPython interpreter terminated.')
                break
            elif not new_folder:
                raise ValueError('\n\tYou must type a name,')
            elif os.path.isdir(new_folder):
                raise ValueError(f"\n\tA folder called '{new_folder}' already exists,")
            else:
                return new_folder
        except ValueError as e:
            print(f'{e} please try again.')


def run_cmd(cmd, step):
    try:
        print(step)
        subprocess.run(cmd, shell=True, check=True, cwd=project)  # setting current dir where cmds will be run
    except subprocess.CalledProcessError as e:
        print(f"\n\tsubprocess.CalledProcessError returned this error: \n\t{e}")
    except ValueError as e:
        print(f'{e} please try again.')


# paths for subprocess cmds
project = get_folder_name(parameter=project_question)
venv_path = os.path.join(project, '.venv')
python = '.venv/bin/python'


# Creating venv
def create_venv():
    builder = venv.EnvBuilder(system_site_packages=False, symlinks=True, with_pip=True)
    builder.create(venv_path)


# upgrading pip
def upgrade_pip():
    whats_happening = f'\n\tUpgrading pip to the latest version...'
    cmd = f'{python} -m pip install --upgrade pip --quiet'
    run_cmd(cmd, step=whats_happening)


def install_dependencies():
    try:
        if not dependencies:
            raise Exception('There are no dependencies to be installed,')
        else:
            for _ in dependencies:
                whats_happening = f'\n\tCollecting {_}...'
                cmd = f'{python} -m pip install {_} --quiet'
                run_cmd(cmd, step=whats_happening)
    except Exception as e:
        print(f'\t{e}')
        sys.exit()


def create_project():
    create_venv()
    upgrade_pip()
    install_dependencies()


if __name__ == '__main__':
    create_project()

