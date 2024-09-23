import os
import subprocess
import sys
import venv

# -------------------- You can customize the tuples below --------------------

# Customize the 'dependencies' tuple with the dependencies to be installed:
dependencies = ('emoji',) # The emoji module will be installed as an example

# You can customize the 'project_folders' tuple:
project_folders = (
    'media',  # A single folder
    ('templates', 'static'),  # A parent directory, a child directory, so on and so forth
)

# -------------------- You can customize the settings above --------------------


parent_dir = os.path.dirname(os.getcwd())
project_question = f"\n\tName your project to be created in '{parent_dir}' folder ('exit' to quit): "


def get_folder_name(parameter):  # Used twice to get project and app names
    while True:
        try:
            new_folder = input(f"{parameter}").strip().replace(' ', '_')
            # new_folder = os.path.join(parent_dir, input(f"{parameter}").strip().replace(' ', '_'))
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


# paths for subprocess commands
project = get_folder_name(parameter=project_question)
venv_path = os.path.join(project, '.venv')
python = '.venv/bin/python'


# Creating venv
def create_venv(venv_path):
    print(f"\n\tCreating the virtual environment...")
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


def create_extra_folders():
    project_str = f"\n\tFolders created in project '{project}':"
    print(project_str)
    project_str_start = len(project_str)
    for _ in project_folders:
        if isinstance(_, tuple):
            folder = os.path.join(project, '/'.join(_))
            os.makedirs(folder)
            print(f"{''.ljust(project_str_start)}'{'/'.join(_)}'")
        else:
            folder = os.path.join(project, _)
            os.makedirs(folder)
            print(f"{''.ljust(project_str_start)}'{_}'")


def create_project():
    create_venv(venv_path)
    upgrade_pip()
    install_dependencies()
    create_extra_folders()


if __name__ == '__main__':
    create_project()
