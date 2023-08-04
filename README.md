# PuttyDataCollector
將putty上的資料log下來並針對特定資料進行資料繪圖,並且輸出成.csv

Console 互動介面

Select the curve to plot:
0. FE (Graphics Pipeline Front End)
1. DE (Draw Engine)
2. PE (Pixel Engine)
3. SH (Shader Engine)
4. PA (Primitive Assembly)
5. SE (Setup Engine)
6. RA (Rasterizer)
7. TX (Texture Engine)
8. VG (Vector Graphics)
9. FP (Fragment processor)
10. TS (Tile status)
11. MC (Memory Controller)
12. AXI_LP (AXI bus in low power)
13. BL
14. BP
15. IDLE0
16. USAGE
Enter the index(es) of the curve(s) you want to plot (separated by space, or enter -1 for 'All'): -1

Do you want to export the current data to CSV? (y/n): y
Enter the CSV filename (e.g., data.csv): output


![繪製圖形](https://github.com/coolping/PuttyDataCollector/blob/main/Figure_1.png?raw=true)
