import re

def filter_lines_with_chapter(text):
    
    # 将文本按行分割
    lines = text.split('\n')
    
    # 过滤掉包含“第*章”的行
    filtered_lines = [line for line in lines if not line.startswith('第') ]
    # print(filtered_lines[2])
    # 将过滤后的行重新组合成一个文本字符串
    return '\n'.join(filtered_lines)

def split_and_replace_newlines(text):
    # 使用两个换行符来分割文本为章节数组
    chapters = text.split("\n\n")
    
    # 将每个章节中的换行符替换为空格
    chapters_with_spaces = [chapter.replace('\n    ', ' ') for chapter in chapters]
    print(chapters[3])
    # 使用一个换行符将修改后的章节重新组合成一个文本字符串
    return ''.join(chapters_with_spaces)

with open("天蚕土豆\斗破苍穹前传之药老传奇.txt",'r', encoding='utf-8') as file:
    text = file.read()
    
modified_text = filter_lines_with_chapter(text)

final_text = split_and_replace_newlines(modified_text)

with open("output.txt", 'w', encoding='utf-8') as file:
    file.write(final_text)