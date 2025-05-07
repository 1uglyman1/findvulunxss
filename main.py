import subprocess
import os

def run_xscan(file):
    """
    ./xscan spider --file domain.txt --xss-json /result
    :param url:
    :return:
    """
    try:
        command = f'./xscan spider  --file {file}  -xss-json /result '
        print(command)
        #subprocess.run(command, shell=True, check=True)
        print("run_xscan 扫描任务执行成功")
    except subprocess.CalledProcessError as e:
        print(f"执行 run_xscan 扫描任务时出错: {e}")
        return False
    return True

if __name__ == '__main__':
    run_xscan("url.txt")
    # with open('./xscan/config.yaml','r', encoding='utf-8') as f:
    #     for line in f:
    #         line = line.strip()  # 去掉行尾换行符和空白
    #         run_xscan(line)

