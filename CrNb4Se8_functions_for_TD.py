import numpy as np
import math

def convert_fractional_to_cartesian(frac_coords, lattice_constants):
    """
    分率座標を実座標（カルテシアン座標）に変換する関数
    
    引数:
    frac_coords (list/array): 変換したい分率座標 [u, v, w]
    lattice_constants (list): 格子定数 [a, b, c, alpha, beta, gamma]
        - a, b, c: 格子の長さ
        - alpha, beta, gamma: 格子の角度（度数法）
    
    返り値:
    cart_coords (numpy.array): 変換後の実座標 [x, y, z]
    """
    # 分率座標をnumpy配列に変換
    frac = np.array(frac_coords)
    
    # 格子定数を取得
    a, b, c, alpha, beta, gamma = lattice_constants
    alpha = np.radians(alpha)  # 度からラジアンに変換
    beta = np.radians(beta)
    gamma = np.radians(gamma)
    
    # 変換行列の計算
    cos_alpha = np.cos(alpha)
    cos_beta = np.cos(beta)
    cos_gamma = np.cos(gamma)
    sin_gamma = np.sin(gamma)
    
    # 体積の計算に必要な項
    v = np.sqrt(1 - cos_alpha**2 - cos_beta**2 - cos_gamma**2 + 2 * cos_alpha * cos_beta * cos_gamma)
    
    # 変換行列
    transformation_matrix = np.zeros((3, 3))
    transformation_matrix[0, 0] = a
    transformation_matrix[0, 1] = b * cos_gamma
    transformation_matrix[0, 2] = c * cos_beta
    transformation_matrix[1, 1] = b * sin_gamma
    transformation_matrix[1, 2] = c * (cos_alpha - cos_beta * cos_gamma) / sin_gamma
    transformation_matrix[2, 2] = c * v / sin_gamma
    
    # 分率座標から実座標への変換
    cart_coords = np.dot(transformation_matrix, frac)
    
    return cart_coords

def calculate_distance(point1, point2):
    """
    2点間のユークリッド距離を計算する関数
    
    引数:
    point1 (list/array): 1つ目の点の実座標 [x1, y1, z1]
    point2 (list/array): 2つ目の点の実座標 [x2, y2, z2]
    
    返り値:
    distance (float): 2点間のユークリッド距離
    """
    # numpy配列に変換
    p1 = np.array(point1)
    p2 = np.array(point2)
    
    # ユークリッド距離の計算
    distance = np.sqrt(np.sum((p1 - p2)**2))
    
    return distance

def calculate_octahedral_distortion(cr_position, se_position, lattice_constants):
    """
    八面体歪みを計算する関数
    
    引数:
    cr_position (list/array): Cr原子の分率座標 [u, v, w]
    se_position (list/array): Se2原子（またはS2原子）の分率座標 [u, v, w]
    lattice_constants (list): 格子定数 [a, b, c, alpha, beta, gamma]
        - a, b, c: 格子の長さ
        - alpha, beta, gamma: 格子の角度（度数法）
    
    返り値:
    distortion (float): 八面体歪み (D = Δz_real - Δz_ideal)
    delta_z_real (float): 実際のSe2原子のz座標
    delta_z_ideal (float): 理想的な八面体構造でのz座標
    """
    # Cr原子の実座標を計算
    cr_cart = convert_fractional_to_cartesian(cr_position, lattice_constants)
    
    # Se2原子の実座標を計算
    se_cart = convert_fractional_to_cartesian(se_position, lattice_constants)
    
    # Cr原子からSe2原子までの距離dを計算
    d = calculate_distance(cr_cart, se_cart)
    
    # Δz_realはSe2原子のz座標（分率座標）
    delta_z_real = se_position[2]
    
    # Δz_idealを計算
    # 理想的な正八面体では、三角形の重心のz座標は実座標でd/√3
    ideal_z_cart = d / math.sqrt(3)
    
    # 実座標を分率座標に変換（c軸方向のみの単純変換）
    delta_z_ideal = cr_position[2] + (ideal_z_cart / lattice_constants[2])  # c = lattice_constants[2]
    
    # 八面体歪みD = Δz_real - Δz_idealを計算
    distortion = delta_z_real - delta_z_ideal
    
    return distortion, delta_z_real, delta_z_ideal