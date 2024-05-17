import subprocess
#path to jupyter package in your envs

# Kích hoạt đưa thư viện ảo vào kernel
def install_ipykernel(env, display_name):
    try:
        command = f"python -m ipykernel install --user --name {env} --display-name \"{display_name}\""
        subprocess.run(command, shell=True, check=True)
        print(f"Installed IPython kernel '{display_name}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing IPython kernel: {e}")

# Chạy file ipynb trong kernel
def run_ipynb(notebook_path,env,path_to_jupyter):
    try:
        # Sử dụng Popen để chạy lệnh activate trong môi trường Conda
        activate_command = f"conda activate {env} && "
        nbconvert_command = f"{path_to_jupyter} nbconvert --execute --inplace {notebook_path}"
        subprocess.Popen(activate_command + nbconvert_command, shell=True)
    except Exception as e:
        print(f"Lỗi khi thực thi tệp {notebook_path}: {e}")







if __name__ == '__main__':
    import os    
    prj_dir='1.EDA'
    notebook_dir=f'../prj/{prj_dir}'
    # print(notebook_root)
    print(f'{notebook_dir}/EDA1.ipynb')


    # Sử dụng hàm để chạy tệp notebook IPython
    path_to_jupyter="C:/Users/PC/miniconda3/envs/uii_prj/Scripts/jupyter.exe"
    install_ipykernel('uii_prj','test')
    run_ipynb(f'{notebook_dir}/EDA1.ipynb','uii_prj',path_to_jupyter)
    pass