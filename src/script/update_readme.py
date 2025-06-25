import requests, os
from datetime import datetime, timezone, timedelta

baseurl = 'https://solved.ac/api/v3'

def get_header(handle):
    response = requests.get(f"{baseurl}/user/show?handle={handle}").raise_for_status()
    user_data = response.json()

    rating = str(user_data['rating'])
    solvedCount = str(user_data['solvedCount'])
    userClass = str(user_data['class'])

    header = '<div align="center">\n\n' \
        + "# BOJ\n\n" \
        + "**백준 문제 풀이 저장소**\n\n" \
        + "![Github code size in bytes](https://img.shields.io/github/languages/code-size/b1nknet/boj?style=flat-square)\n\n" \
        + f'[![solved.ac 프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj={handle})](https://solved.ac/{handle})\n' \
        + f'![solved.ac 잔디](http://mazandi.herokuapp.com/api?handle={handle}&theme=dark)\n\n' \
        + f'*( [solved.ac](https://solved.ac/{handle}) | [BOJ](https://acmicpc.net/user/{handle}) )*\n\n' \
        + "rate: **" + rating + "** | " \
        + "solved: **" + solvedCount + "** | " \
        + "class: **" + userClass + "**\n\n" \
        + "업데이트: " + datetime.now(timezone(timedelta(hours=9))).strftime("%y.%m.%d. %H:%M:%S") + " (KST)\n\n" \
        + '</div>\n' 
    return header

def get_prob_list():
    prob_list = []
    dir_list = [f"{format(i, '02')}xxx" for i in range(1, 34)]

    for s in dir_list:
        files = sorted(os.listdir(f"./{s}"))
        
        for filename in files:
            probId, fileExt = map(str, filename.split('.'))
            prob_list.append({"id": probId, "ext": fileExt, "file_location": f'{s}/{filename}'})

    prob_id_list = [prob['id'] for prob in prob_list]
    fetchParam = ''
    for id in prob_id_list:
        fetchParam += id
        if prob_id_list.index(id) != len(prob_id_list) - 1:
            fetchParam += "%2C"

    response = requests.get(f"{baseurl}/problem/lookup?problemIds={fetchParam}").raise_for_status()
    probs_data = response.json()
    for p in prob_list:
        prob_data = probs_data[prob_list.index(p)]
        p['title'] = prob_data['titles'][0]['title']
        p['level'] = prob_data['level']

    return prob_list

def get_table():
    table = '<div align="center">\n\n'
    table += '| 번호 | 제목 | 레벨 | 코드 |\n'
    table += '|:---:|:---:|:---:|:---:|\n'
    
    ext = {
        "c": "C",
        "cpp": "C++",
        "java": "Java",
        "py": "Python"
    }

    prob_list = get_prob_list()
    for p in prob_list:
        table += '| ' + p['id'] + ' | ' + p['title'] + ' | <img style="height:30px;" src="src/tier/' + str(p['level']) + '.svg"> | [' + ext[p['ext']] + '](./'+ p['file_location'] +') |\n'

    table += '\n</div>'
    return table

# 메인 함수
if __name__ == "__main__":
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
    
    os.remove("README.md.tmp")
