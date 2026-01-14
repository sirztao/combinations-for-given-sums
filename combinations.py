# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 22:41:56 2018
Modified on Wen Jau 14 18:17:17 2025
@author: tao
""" 
import math
import time
from itertools import combinations

# 原始票据金额列表（保留重复值，每张票独立）
ary = [745, 298, 318, 380.2, 624.6, 216.2, 499, 399, 1923, 99.5, 245, 578.7,
       973, 506.8, 94, 164.7, 433, 441.5, 419, 165, 1196, 245, 999]

TARGET = 6194.0          # 目标总金额
TOLERANCE = 0.01         # 浮点容差
MIN_LEN = 7              # 最少票据张数
MAX_LEN = 17             # 最多票据张数
OUTPUT_FILE = r'C:\work\MyResultforJDPailieZuhe.txt'

def main():
    # 使用字典按组合长度分组存储结果：{7: [combo1, combo2, ...], 8: [...], ...}
    results_by_length = {j: [] for j in range(MIN_LEN, MAX_LEN + 1)}
    
    total_found = 0
    start_time = time.perf_counter()  # 高精度计时开始

    print("开始搜索符合条件的票据组合（按长度分组）...")
    
    # 遍历每种票据张数组合
    for j in range(MIN_LEN, MAX_LEN + 1):
        count_for_j = 0
        print(f"  正在处理 {j} 张票据的组合...", end='', flush=True)
        
        # 惰性迭代所有 j 元组合（不一次性加载到内存）
        for combo in combinations(ary, j):
            total = sum(combo)
            if math.isclose(total, TARGET, abs_tol=TOLERANCE):
                results_by_length[j].append(combo)
                total_found += 1
                count_for_j += 1
                
                # ========== 控制台打印每个解（当前注释掉，需要时取消注释） ==========
                # print(f"\n  找到一个 {j} 张票据的解: {combo} (总和 = {total:.2f})")
                # ===================================================================

        print(f" 找到 {count_for_j} 个解")  # 行末更新数量，避免刷屏

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"\n✅ 搜索完成！总共找到 {total_found} 个符合条件的组合。")
    print(f"⏱️  总耗时: {elapsed:.2f} 秒")

    # === 写入文件（按组分类）===
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as fo:
            fo.write(f"一共找到了 {total_found} 个符合要求的结果\n")
            fo.write(f"搜索耗时: {elapsed:.2f} 秒\n")
            fo.write("\n\n" + "="*80 + "\n")
            fo.write("                        符合要求的结果（按票据张数分组）\n")
            fo.write("="*80 + "\n\n")

            for j in range(MIN_LEN, MAX_LEN + 1):
                group = results_by_length[j]
                if group:
                    fo.write(f"\n【{j} 张票据的组合】（共 {len(group)} 个）\n")
                    fo.write("-" * 50 + "\n")
                    for idx, combo in enumerate(group, 1):
                        # 格式化为易读形式，保留原始数值精度
                        fo.write(f"{idx:2d}. {combo}\n")
                else:
                    fo.write(f"\n【{j} 张票据的组合】：无\n")

        print(f"📄 结果已成功写入文件: {OUTPUT_FILE}")

    except OSError as e:
        print(f"❌ 写入文件失败: {e}")
        print("请确保 C:\\work 目录存在，或修改 OUTPUT_FILE 路径。")

if __name__ == "__main__":
    main()