#读取部分

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#转换部分
def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count =  0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line. split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:	
				for m in s[2:]:
					allen_word_count+= len(m)
		if name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen说了', allen_word_count , '个字')
	print('allen发了', allen_sticker_count, '个表情')
	print('allen发了', allen_image_count, '张图')
	print('viki说了', viki_word_count , '个字')
	print('viki发了', viki_sticker_count, '个表情')
	print('viki发了', viki_image_count, '张图')
#写文档部分
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

#触发机制 触发点
def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

#接入点
main()