import numpy as np
import os
import argparse
from CrNb4Se8_functions_for_TD import convert_fractional_to_cartesian, calculate_distance, calculate_octahedral_distortion

def main():
    # argparseを使ってコマンドライン引数を処理
    parser = argparse.ArgumentParser(description='3つの物質の八面体歪みを計算して結果をファイルに出力します。')
    parser.add_argument('output_file', nargs='?', default='CrNb4Se8_trigonal_distortion.txt',
                        help='出力ファイル名 (デフォルト: CrNb4Se8_trigonal_distortion.txt)')
    args = parser.parse_args()
    
    # 出力ファイル名を取得
    output_filename = args.output_file
    
    # 現在のディレクトリ（スクリプトと同じディレクトリ）にファイルを出力
    output_file = os.path.join(os.path.dirname(__file__), output_filename)
    
    # 出力ファイルを開く
    with open(output_file, "w") as f:
        # 画面とファイルの両方に出力する関数
        def print_output(text):
            print(text)
            f.write(text + "\n")
        
        print_output("=== 3物質の八面体歪み計算 ===\n")

        # ========== CrNb4Se8（最適化前）==========
        print_output("1. CrNb4Se8（最適化前）")
        
        # 六方晶系の格子定数 [a, b, c, alpha, beta, gamma]
        lattice_constants1 = [6.90400, 6.90400, 12.57, 90.0, 90.0, 120.0]
        
        # Cr原子の分率座標
        cr_position1 = [0.0, 0.0, 0.0]
        
        # Se2原子の分率座標
        se2_position1 = [0.16667, 0.33333, 0.125]
        
        # 八面体歪みを計算
        distortion1, delta_z_real1, delta_z_ideal1 = calculate_octahedral_distortion(
            cr_position1, se2_position1, lattice_constants1
        )
        
        # Cr-Se2間の距離を計算
        cr_cart1 = convert_fractional_to_cartesian(cr_position1, lattice_constants1)
        se2_cart1 = convert_fractional_to_cartesian(se2_position1, lattice_constants1)
        distance1 = calculate_distance(cr_cart1, se2_cart1)
        
        # 結果の表示
        print_output(f"格子定数: a = b = {lattice_constants1[0]} Å, c = {lattice_constants1[2]} Å")
        print_output(f"Cr原子の分率座標: ({cr_position1[0]}, {cr_position1[1]}, {cr_position1[2]})")
        print_output(f"Se2原子の分率座標: ({se2_position1[0]}, {se2_position1[1]}, {se2_position1[2]})")
        print_output(f"Cr-Se2間距離: {distance1:.5f} Å")
        print_output(f"実際のΔz: {delta_z_real1:.6f}")
        print_output(f"理想的なΔz: {delta_z_ideal1:.6f}")
        print_output(f"八面体歪み (D = Δz_real - Δz_ideal): {distortion1:.6f}\n")
        
        # ========== CrNb4Se8（最適化後）==========
        print_output("2. CrNb4Se8（最適化後）")
        
        # 六方晶系の格子定数 [a, b, c, alpha, beta, gamma]
        lattice_constants2 = [6.90400, 6.90400, 12.57, 90.0, 90.0, 120.0]
        
        # Cr原子の分率座標
        cr_position2 = [0.0, 0.0, 0.0]
        
        # Se2原子の分率座標
        se2_position2 = [0.168359, 0.336717, 0.118357]
        
        # 八面体歪みを計算
        distortion2, delta_z_real2, delta_z_ideal2 = calculate_octahedral_distortion(
            cr_position2, se2_position2, lattice_constants2
        )
        
        # Cr-Se2間の距離を計算
        cr_cart2 = convert_fractional_to_cartesian(cr_position2, lattice_constants2)
        se2_cart2 = convert_fractional_to_cartesian(se2_position2, lattice_constants2)
        distance2 = calculate_distance(cr_cart2, se2_cart2)
        
        # 結果の表示
        print_output(f"格子定数: a = b = {lattice_constants2[0]} Å, c = {lattice_constants2[2]} Å")
        print_output(f"Cr原子の分率座標: ({cr_position2[0]}, {cr_position2[1]}, {cr_position2[2]})")
        print_output(f"Se2原子の分率座標: ({se2_position2[0]}, {se2_position2[1]}, {se2_position2[2]})")
        print_output(f"Cr-Se2間距離: {distance2:.5f} Å")
        print_output(f"実際のΔz: {delta_z_real2:.6f}")
        print_output(f"理想的なΔz: {delta_z_ideal2:.6f}")
        print_output(f"八面体歪み (D = Δz_real - Δz_ideal): {distortion2:.6f}\n")
        
        # ========== CrTa4S8 ==========
        print_output("3. CrTa4S8")
        
        # 六方晶系の格子定数 [a, b, c, alpha, beta, gamma]
        lattice_constants3 = [6.59590, 6.59590, 12.03910, 90.0, 90.0, 120.0]
        
        # Cr原子の分率座標
        cr_position3 = [0.0, 0.0, 0.0]
        
        # S2原子の分率座標
        s2_position3 = [0.1667, 0.3334, 0.1188]
        
        # 八面体歪みを計算
        distortion3, delta_z_real3, delta_z_ideal3 = calculate_octahedral_distortion(
            cr_position3, s2_position3, lattice_constants3
        )
        
        # Cr-S2間の距離を計算
        cr_cart3 = convert_fractional_to_cartesian(cr_position3, lattice_constants3)
        s2_cart3 = convert_fractional_to_cartesian(s2_position3, lattice_constants3)
        distance3 = calculate_distance(cr_cart3, s2_cart3)
        
        # 結果の表示
        print_output(f"格子定数: a = b = {lattice_constants3[0]} Å, c = {lattice_constants3[2]} Å")
        print_output(f"Cr原子の分率座標: ({cr_position3[0]}, {cr_position3[1]}, {cr_position3[2]})")
        print_output(f"S2原子の分率座標: ({s2_position3[0]}, {s2_position3[1]}, {s2_position3[2]})")
        print_output(f"Cr-S2間距離: {distance3:.5f} Å")
        print_output(f"実際のΔz: {delta_z_real3:.6f}")
        print_output(f"理想的なΔz: {delta_z_ideal3:.6f}")
        print_output(f"八面体歪み (D = Δz_real - Δz_ideal): {distortion3:.6f}")
        
        # ========== 結果のまとめ（表形式） ==========
        print_output("\n\n=============== 結果まとめ ===============")
        print_output("| 物質名               | c軸長 (Å)   | Cr-X2間距離 (Å) | Δz_real     | Δz_ideal    | 歪み係数 D   |")
        print_output("|----------------------|-------------|----------------|-------------|-------------|-------------|")
        print_output(f"| CrNb4Se8（最適化前） | {lattice_constants1[2]:.5f}   | {distance1:.5f}       | {delta_z_real1:.6f}  | {delta_z_ideal1:.6f}  | {distortion1:.6f}  |")
        print_output(f"| CrNb4Se8（最適化後） | {lattice_constants2[2]:.5f}   | {distance2:.5f}       | {delta_z_real2:.6f}  | {delta_z_ideal2:.6f}  | {distortion2:.6f}  |")
        print_output(f"| CrTa4S8              | {lattice_constants3[2]:.5f}   | {distance3:.5f}       | {delta_z_real3:.6f}  | {delta_z_ideal3:.6f}  | {distortion3:.6f}  |")
        print_output("\n注: X2はCrNb4Se8ではSe2原子、CrTa4S8ではS2原子を表します。")
    
    # 絶対パスでファイルの位置を表示
    abs_output_file = os.path.abspath(output_file)
    print(f"\nファイルが保存されました: {abs_output_file}")
    print(f"使用方法: python {os.path.basename(__file__)} [出力ファイル名]")
    print(f"例: python {os.path.basename(__file__)} CrNb4Se8_trigonal_distortion.txt")

if __name__ == "__main__":
    main()
