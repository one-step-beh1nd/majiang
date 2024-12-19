from shagua import shagua
from fujian import fujian
from sichuan import sichuan
import json

round = 100000
games_per_round = 6
step = 1

result = {'shagua':{}, 'fujian': {}, 'sichuan': {}}

for i in range(0, games_per_round, step):
    shagua_virus = [0, 0, 0, 0]
    fujian_virus = [0, 0, 0, 0]
    sichuan_virus = [0, 0, 0, 0]
    for j in range(round):
        new_virus = shagua(i)
        for k in range(4):
            shagua_virus[k] += new_virus[k]

        new_virus = fujian(i)
        for k in range(4):
            fujian_virus[k] += new_virus[k]

        new_virus = sichuan(i)
        for k in range(4):
            sichuan_virus[k] += new_virus[k]

    result['shagua'][i] = shagua_virus
    result['fujian'][i] = fujian_virus
    result['sichuan'][i] = sichuan_virus

with open("./result.json", 'w') as f:
    json.dump(result, f, indent=4)




import matplotlib.pyplot as plt
import json
import os

if not os.path.exists('./pic'):
    os.makedirs('./pic')

save_path = './pic'
with open('./result.json', 'r') as f:
    majiang: dict = json.load(f)

x = [i for i in range(0, games_per_round, step)]

y_1_shagua = []
y_1_fujian = []
y_1_sichuan = []

y_2_shagua = []
y_2_fujian = []
y_2_sichuan = []

y_3_shagua = []
y_3_fujian = []
y_3_sichuan = []

for xx, li in majiang['shagua'].items():
    y_1_shagua.append(li[1])
    y_2_shagua.append(li[2])
    y_3_shagua.append(li[3])

for xx, li in majiang['fujian'].items():
    y_1_fujian.append(li[1])
    y_2_fujian.append(li[2])
    y_3_fujian.append(li[3])

for xx, li in majiang['sichuan'].items():
    y_1_sichuan.append(li[1])
    y_2_sichuan.append(li[2])
    y_3_sichuan.append(li[3])

y = [y_1_shagua, y_1_fujian, y_1_sichuan, y_2_shagua, y_2_fujian, y_2_sichuan, y_3_shagua, y_3_fujian, y_3_sichuan]

index = ['1', '2', '3']

majiang_name = ['Da Zhong','Fu Jian','Si Chuan']

for i in range(9):
    people = index[i//3]
    m_name = majiang_name[i%3]
    
    plt.figure(figsize=(8, 8))

    # 绘制子图
    plt.plot(x, y[i], marker='o')

    plt.title(f"{people} {m_name}")
    plt.xlabel('Disinfection Interval / Round')
    plt.ylabel('Virus / Unit')
    plt.grid(True)
    # 保存每个子图为一个文件
    plt.savefig(os.path.join(save_path, f'{people}_{m_name}.png'))

    # 关闭当前图形，避免累积
    plt.close()


# 个人对比
plt.figure(figsize=(8, 8))
plt.plot(x, y[0], marker='o', label='dazhong')
plt.plot(x, y[1], marker='o', label='fujian')
plt.plot(x, y[2], marker='o', label='sichuan')
plt.title('1')
plt.xlabel('Disinfection Interval / Round')
plt.ylabel('Virus / Unit')
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(save_path, f'1.png'))
plt.close()

plt.figure(figsize=(8, 8))
plt.plot(x, y[3], marker='o', label='dazhong')
plt.plot(x, y[4], marker='o', label='fujian')
plt.plot(x, y[5], marker='o', label='sichuan')
plt.title('2')
plt.xlabel('Disinfection Interval / Round')
plt.ylabel('Virus / Unit')
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(save_path, f'2.png'))
plt.close()

plt.figure(figsize=(8, 8))
plt.plot(x, y[6], marker='o', label='dazhong')
plt.plot(x, y[7], marker='o', label='fujian')
plt.plot(x, y[8], marker='o', label='sichuan')
plt.title('3')
plt.xlabel('Disinfection Interval / Round')
plt.ylabel('Virus / Unit')
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(save_path, f'3.png'))
plt.close()

# 同一麻将对比
for i in range(3):
    plt.figure(figsize=(8, 8))
    plt.plot(x, y[i], marker='o', label='1')
    plt.plot(x, y[i+3], marker='o', label='2')
    plt.plot(x, y[i+6], marker='o', label='3')

    plt.title(majiang_name[i])
    
    plt.xlabel('Disinfection Interval / Round')
    plt.ylabel('Virus / Unit')
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(save_path, f'{majiang_name[i]}.png'))
    plt.close()