import re


def main(str):
    pattern = "(?<=[@]).*?(?=[.][|])"
    result = {}

    str = str.replace(" ", "")
    str = str.replace("\n", "")
    access = re.findall(pattern, str)

    for i in access:
        txt = i.split("=>")
        result[txt[1]] = txt[0]

    return result

str = ".begin ||define @'erlage'=>geti_654. |||| define @'maer_9'=> biti. |||| define @'tienza' => edtile_135. || || " \
      "define @'lain' => adidixe.||.end"

print(main(str))
