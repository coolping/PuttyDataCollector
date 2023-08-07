import re
import matplotlib.pyplot as plt
import csv
# 读取文件内容
with open('log.txt', 'r') as file:
    content = file.read()


# 使用正则表达式提取所有部件的占用率百分比
pattern1 = r"(\w+\s+\(.*?\))\s+(\d+\.\d+)%"
matches1 = re.findall(pattern1, content)

# 将数据按部件名称进行分类
data = {}
for part, usage in matches1:
    if part not in data:
        data[part] = []
    data[part].append(float(usage))

# 使用正则表达式提取所有部件的占用率百分比
pattern2 = r"(\w+)\s+(\d+\.\d+)%"
matches2 = re.findall(pattern2, content)

# 将数据按部件名称进行分类

for part, usage in matches2:
    if part not in data:
        data[part] = []
    data[part].append(float(usage))

# 定义可选曲线列表
available_curves = ['FE (Graphics Pipeline Front End)', 'DE (Draw Engine)', 'PE (Pixel Engine)', 'SH (Shader Engine)', 'PA (Primitive Assembly)', 'SE (Setup Engine)', 'RA (Rasterizer)', 'TX (Texture Engine)', 'VG (Vector Graphics)',  'FP (Fragment processor)','TS (Tile status)', 'MC (Memory Controller)', 'AXI_LP (AXI bus in low power)','BL', 'BP', 'IDLE0', 'USAGE']

try:
    while True:
        # 询问用户要绘制哪条曲线
        print("\nSelect the curve to plot:")
        for i, curve in enumerate(available_curves):
            print(f"{i}. {curve}")

        selected_curves_indexes = input("Enter the index(es) of the curve(s) you want to plot (separated by space, or enter -1 for 'All'): ")
        selected_curves_indexes = [int(index) for index in selected_curves_indexes.split()]

        # 询问用户是否要导出数据到CSV
        export_csv = input("\nDo you want to export the current data to CSV? (y/n): ").strip().lower()
        if export_csv == 'y':
            csv_filename = input("Enter the CSV filename (e.g., data.csv): ").strip()
        else:
            csv_filename ="None"



        # 绘制图表

        '''plt.figure(figsize=(12, 6))  # 设置图形大小

        for i, (part, usage_list) in enumerate(data.items()):
            if selected_curves_indexes == [-1] or i in selected_curves_indexes:
                plt.plot(usage_list, marker='o', label=part)

        plt.xlabel('Sample')
        plt.ylabel('Usage (%)')
        plt.title('Usage of Graphics Processor Components Over Samples')
        plt.grid(True)
        plt.legend()
        plt.xticks(range(len(usage_list)))  # 设置横坐标刻度
        plt.show()'''

        # Initialize data lists for all available curves
        for curve in available_curves:
            if curve not in data:
                print(curve)
                data[curve] = []
        
        if csv_filename.endswith('.csv'):
            with open(csv_filename, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Sample'] + available_curves)
                max_samples = max(len(data[curve]) for curve in available_curves)
                for i in range(max_samples):
                    row = [i]
                    for curve in available_curves:
                        if i < len(data[curve]):
                            row.append(data[curve][i])
                        else:
                            row.append(None)
                    writer.writerow(row)
            print("\nGenerate csv succesd!.")
except KeyboardInterrupt:
    print("\nProgram ended by user (Ctrl+C).")
