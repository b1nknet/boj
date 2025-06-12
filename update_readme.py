import requests, os
from datetime import datetime, timezone, timedelta

# solved.ac API로 사용자 정보를 가져옴
def get_solved_int(handle, param):
    response = requests.get(f"https://solved.ac/api/v3/user/show", params={"handle": handle})
    response.raise_for_status()
    return int(response.json()[param])

def get_header(handle):
    header = '<div align="center">\n\n'
    header += "# BOJ\n\n"
    header += "**백준 문제 풀이 저장소**\n\n"
    header += "![Github code size in bytes](https://img.shields.io/github/languages/code-size/b1nknet/boj?style=flat-square)\n\n"
    header += f'<img style="height:60" alt="" src="assets/tier/{get_solved_int(handle, "tier")}.svg">\n\n'
    header += f'<div style="font-weight:bold;font-size:2em;">{handle}</div>'
    header += "rate: " + str(get_solved_int(handle, "rating")) + " | "
    header += "solved: " + str(get_solved_int(handle, "solvedCount")) + " | "
    header += "class: " + str(get_solved_int(handle, "class")) + "\n\n"
    header += "업데이트: "
    header += datetime.now(timezone(timedelta(hours=9))).strftime("%y.%m.%d. %H:%M:%S")
    header += " (KST)\n\n"
    header += '</div>'
    return header

dir_list = [
    "1xxx",
    "2xxx"
]

ext = {
    "c": "C",
    "cpp": "C++",
    "java": "Java",
    "py": "Python"
}

# solved.ac API로 문제의 제목을 가져옴
def get_problem_title(problemId):
    response = requests.get(f"https://solved.ac/api/v3/problem/show", params={"problemId": problemId})
    response.raise_for_status()
    return response.json()["titles"][0]["title"]

# solved.ac API로 문제의 난이도를 가져옴
def get_problem_level(problemId):
    response = requests.get(f"https://solved.ac/api/v3/problem/show", params={"problemId": problemId})
    response.raise_for_status()
    return response.json()["level"]

def get_table():
    table = '<div align="center">\n\n'
    table += '| 번호 | 제목 | 레벨 | 코드 |\n'
    table += '|:---:|:---:|:---:|:---:|\n'

    for s in dir_list:
        files = os.listdir(f"./{s}")

        for filename in files:
            probId, fileExt = map(str, filename.split("."))
            table += '|'+probId+'|' + get_problem_title(probId) + '| <img style="height:30px;" src="assets/tier/'+str(get_problem_level(probId))+'.svg"> |['+ext[fileExt]+'](./'+ s + '/' + filename +')|\n'

    table += '\n</div>'
    return table

# 메인 함수
if __name__ == "__main__":
    # README.md 업데이트
    os.remove("README.md")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(get_header("ftw_0x00") + get_table())