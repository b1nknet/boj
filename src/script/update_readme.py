import requests, os
from datetime import datetime, timezone, timedelta

# solved.ac API로 사용자 정보를 가져옴
def get_solved_int(handle, param):
    print(f'Getting info for {param}...')
    response = requests.get(f"https://solved.ac/api/v3/user/show", params={"handle": handle})
    response.raise_for_status()
    return int(response.json()[param])

def get_header(handle):
    print('Generating header...')
    header = '<div align="center">\n\n'
    header += "# BOJ\n\n"
    header += "**백준 문제 풀이 저장소**\n\n"
    header += "![Github code size in bytes](https://img.shields.io/github/languages/code-size/b1nknet/boj?style=flat-square)\n\n"
    header += f'[![solved.ac 프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj={handle})](https://solved.ac/{handle})\n'
    header += f'![solved.ac 잔디](http://mazandi.herokuapp.com/api?handle={handle}&theme=dark)\n\n'
    header += f'*( [solved.ac](https://solved.ac/{handle}) | [BOJ](https://acmicpc.net/user/{handle}) )*\n\n'
    header += "rate: **" + str(get_solved_int(handle, "rating")) + "** | "
    header += "solved: **" + str(get_solved_int(handle, "solvedCount")) + "** | "
    header += "class: **" + str(get_solved_int(handle, "class")) + "**\n\n"
    header += "업데이트: "
    header += datetime.now(timezone(timedelta(hours=9))).strftime("%y.%m.%d. %H:%M:%S")
    header += " (KST)\n\n"
    header += '</div>\n'
    return header

dir_list = [f"{format(i, '02')}xxx" for i in range(1, 34)]

ext = {
    "c": "C",
    "cpp": "C++",
    "java": "Java",
    "py": "Python"
}

# solved.ac API로 문제의 정보를 가져옴
def get_problem_info(probId):
    response = requests.get(f"https://solved.ac/api/v3/problem/show", params={"problemId": probId})
    response.raise_for_status()
    return response.json()["titles"][0]["title"], response.json()["level"]

def get_table():
    table = '<div align="center">\n\n'
    table += '| 번호 | 제목 | 레벨 | 코드 |\n'
    table += '|:---:|:---:|:---:|:---:|\n'

    for s in dir_list:
        files = sorted(os.listdir(f"./{s}"))

        for filename in files:
            probId, fileExt = map(str, filename.split("."))
            print(f'Getting info for {probId}...')
            (probTitle, probLevel) = get_problem_info(probId)
            table += '| '+probId+' | ' + probTitle + ' | <img style="height:30px;" src="src/tier/'+str(probLevel)+'.svg"> | ['+ext[fileExt]+'](./'+ s + '/' + filename +') |\n'

    table += '\n</div>'
    return table

# 메인 함수
if __name__ == "__main__":
    print('Generating README.md...')
    # README.md 업데이트
    with open("README.md.tmp", "w", encoding="utf-8") as f:
        f.write(get_header("ftw_0x00") + get_table())
    
    # README.md.tmp와 README.md 비교
    with open("README.md.tmp", "r", encoding="utf-8") as f:
        tmp = f.readlines()
        with open("README.md", "r", encoding="utf-8") as f:
            readme = f.readlines()
            if tmp[16:] != readme[16:]:
                with open("README.md", "w", encoding="utf-8") as f:
                    f.writelines(tmp)
            else: print('File is up to date')
    
    os.remove("README.md.tmp")
