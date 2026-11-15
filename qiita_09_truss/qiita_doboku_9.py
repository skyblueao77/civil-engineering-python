# ruff: noqa: E501, E402, E741
# 文字数過多によるコミットエラー回避のために設定
#
# このファイルは、2次元三角形トラスを有限要素法で解析する教材です。
#
# 実行方法（プロジェクトルートで実行）:
#   uv sync
#   uv run python qiita_09_truss/qiita_doboku_9.py
#
# `.venv`を更新せず、現在インストール済みのパッケージだけで確認する場合:
#   uv run --no-sync python qiita_09_truss/qiita_doboku_9.py
#
# このスクリプトは `#%%` をセルの区切りとしても使えますが、上記コマンドで
# ファイル全体を上から順番に実行できます。計算は長さ[m]・力[N]・応力[Pa]
# を基本単位とし、表示時に mm や kN へ換算しています。
#
# 解析の流れ:
#   1. 節点・部材・荷重・支持条件を定義する
#   2. 要素剛性行列を作り、全体剛性行列 K に組み立てる
#   3. 支持条件を適用して K u = f を解く
#   4. 変位から支点反力と部材軸力を求め、理論値と比較する
#
# ※ 学習用の簡略モデルです。実構造物の設計や安全性の判断には使用しないでください。
#
#%% [markdown]
# :::note info
# **この記事の対象者**
#
# * Pythonの基本文法を理解している方
# * NumPy、Matplotlibなどを学んだ方
# * Pythonを土木工学の計算に活用してみたい方
# * 構造力学の基本をPythonで扱ってみたい方
# * 前回の「単純梁」の記事を読んだ方
# :::
# :::note warn
# **この記事を読む前に**
#
# * 本記事は筆者個人の学習記録であり、所属する大学や特定の団体の公式見解ではありません。
# * 本記事の内容には十分注意を払っていますが、正確性や完全性を保証するものではありません。
# * 本記事を参考にする場合は、必ずご自身でも教科書、設計基準、最新の公式資料等をご確認ください。
# * 本記事で扱う計算は学習を目的とした簡略化されたモデルです。実務上の設計・安全性の判断には使用しないでください。
# * 実務での構造解析には、関係法令、設計基準、荷重条件、材料特性、施工条件などを含めた専門的な検討が必要です。
# :::
#
# これまでの記事一覧はこちらから
#
# [【連載一覧】土木のためのPython入門](https://qiita.com/skyblueao77/items/ea31e9890f6368b25e19)
#
# この連載のGitHubリポジトリはこちら
#
# [https://github.com/skyblueao77/civil-engineering-python](https://github.com/skyblueao77/civil-engineering-python)
#
# 今回の記事の内容を気軽に実行したい方は、Google ColabからNotebookを実行できます。
#
# [Open In Colab](https://colab.research.google.com/github/skyblueao77/civil-engineering-python/blob/main/qiita_09_truss/qiita_doboku_9.ipynb)
#
# # はじめに
#
# 前回の記事では、単純支持梁に等分布荷重が作用する問題を題材として、Pythonによる構造力学の計算を行いました。
#
# 単純梁では、
#
# ```text
# L, q, E, I
#     ↓
# 理論式
#     ↓
# V(x), M(x), w(x)
# ```
#
# という流れで、梁のせん断力、曲げモーメント、たわみを計算しました。
#
# 今回は、そこからさらに一歩進みます。
#
# 今回扱うのは **トラス構造** です。
#
# トラスは、橋梁、屋根構造などさまざまな構造物で利用される代表的な構造形式です。
#
# トラスを構成する部材は、理想化すると主に軸方向の力を受ける部材として扱うことができます。
#
# 今回は2次元トラスを題材として、
#
# * 節点と部材の定義
# * 部材の長さ・方向の計算
# * 要素剛性行列
# * 座標変換
# * 全体剛性行列の組立
# * 境界条件の設定
# * `Ku=f` の求解
# * 節点変位の計算
# * 支点反力の計算
# * 部材軸力の計算
# * 変形図の可視化
# * 理論値との比較
#
# までをPythonで実装してみます。
#
# 今回の解析では、これまで学んできたNumPyが非常に重要になります。
#
# 特に、
#
# ```text
# 部材の剛性
#     ↓
# 要素剛性行列
#     ↓
# 全体剛性行列 K
#     ↓
# Ku = f
#     ↓
# 節点変位 u
#     ↓
# 部材軸力
# ```
#
# という流れをPythonで実際に確認していきます。
#
# これは、今後より複雑な構造解析をPythonで扱うための重要な考え方です。

#%% [markdown]
# # 1. 今回扱うトラス
#
# 今回は、最も基本的な2次元三角形トラスを考えます。
#
# ```text
#              C
#             / \
#            /   \
#           /     \
#          /       \
#         A---------B
# ```
#
# 節点A、B、Cの3つの節点と、
#
# ```text
# AB
# AC
# BC
# ```
#
# の3本の部材から構成されるトラスです。
#
# 節点Cに下向きの荷重を作用させます。
#
# ```text
#               C
#               ↓ P
#              / \
#             /   \
#            /     \
#           /       \
#          A---------B
#          ▲         ○
# ```
#
# ここでは、Aをピン支持、Bをローラー支持とします。
#
# したがって、支持条件は、
#
# ```text
# A：
# x方向変位 = 0
# y方向変位 = 0
#
# B：
# y方向変位 = 0
# ```
#
# とします。
#
# 節点Cには下向きの荷重を作用させます。
#
# 今回の条件を表にまとめると次のようになります。
#
# | 項目        |           値 |
# | --------- | ----------: |
# | A座標       |    (0, 0) m |
# | B座標       |    (4, 0) m |
# | C座標       |    (2, 3) m |
# | ヤング係数 `E` |     200 GPa |
# | 断面積 `A`   | 1.0×10⁻³ m² |
# | 節点Cの荷重    |   10 kN 下向き |
#
# ここで注意したいのが、今回の `A` です。
#
# 節点名にもAを使用していますが、断面積にも一般的に `A` が使用されます。
#
# コードでは混乱を避けるため、断面積を `A_cs` とします。

#%% [markdown]
# # 2. トラス構造の仮定
#
# 実際のトラス構造は複雑ですが、今回は学習を目的としてモデルを簡略化します。
#
# 主な仮定は次のとおりです。
#
# * 2次元構造として扱う
# * 部材は直線部材とする
# * 節点はピン接合とする
# * 部材は軸方向力のみを負担する
# * 部材の曲げ剛性は考慮しない
# * 材料は線形弾性体とする
# * 変形は小さい
# * 各部材のヤング係数は一定とする
# * 各部材の断面積は一定とする
#
# このような仮定を置いた構造を、一般に **2次元トラス要素** として扱います。
#
# 今回の解析では、部材の伸び縮みから節点の変位を求めます。
#
# つまり、梁のように、
#
# ```text
# 曲げ
# せん断
# たわみ
# ```
#
# を直接扱うのではなく、
#
# ```text
# 軸方向の伸縮
# ```
#
# を中心に考えます。

#%% [markdown]
# # 3. 節点と部材をPythonで定義する
#
# まず、節点の座標を定義します。

#%%
import numpy as np

# 節点座標
nodes = np.array([
    [0.0, 0.0],  # A
    [4.0, 0.0],  # B
    [2.0, 3.0],  # C
])

print(nodes)

#%% [markdown]
# この配列では、
#
# ```text
# nodes[0] → A
# nodes[1] → B
# nodes[2] → C
# ```
#
# となっています。
#
# 例えば、節点Cの座標は、

#%%
print(nodes[2])

#%% [markdown]
# 次に、部材を定義します。
#
# ここでは節点番号を使って、
#
# ```text
# 0 → A
# 1 → B
# 2 → C
# ```
#
# として定義します。

#%%
members = [
    (0, 1),  # A-B
    (0, 2),  # A-C
    (1, 2),  # B-C
]

#%% [markdown]
# # 4. トラスをMatplotlibで描いてみる
#
# まず、今回の解析対象を可視化してみましょう。

#%%
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 5))

# 部材
for i, j in members:
    x = [nodes[i, 0], nodes[j, 0]]
    y = [nodes[i, 1], nodes[j, 1]]
    ax.plot(x, y, color="black", linewidth=2)

# 節点
ax.scatter(
    nodes[:, 0],
    nodes[:, 1],
    color="white",
    edgecolors="black",
    s=100,
    zorder=3,
)

# 節点ラベル
labels = ["A", "B", "C"]

for i, label in enumerate(labels):
    ax.text(
        nodes[i, 0],
        nodes[i, 1] + 0.15,
        label,
        ha="center",
        fontweight="bold",
    )

# 支点A
ax.scatter(
    nodes[0, 0],
    nodes[0, 1] - 0.15,
    marker="^",
    s=200,
    color="gray",
)

# 支点B
ax.scatter(
    nodes[1, 0],
    nodes[1, 1] - 0.15,
    marker="o",
    s=100,
    color="gray",
)

# 荷重
ax.annotate(
    "",
    xy=(nodes[2, 0], nodes[2, 1] - 0.7),
    xytext=(nodes[2, 0], nodes[2, 1]),
    arrowprops=dict(
        arrowstyle="-|>",
        color="tab:red",
        lw=2,
    ),
)

ax.text(
    nodes[2, 0] + 0.15,
    nodes[2, 1] - 0.35,
    "P = 10 kN",
    color="tab:red",
)

ax.set_aspect("equal")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title("2D Truss Model")
ax.grid(True)

plt.tight_layout()
plt.show()

#%% [markdown]
# # 5. 2次元トラスの自由度
#
# ここからが今回の解析の中心です。
#
# 2次元トラスでは、各節点に、
#
# ```text
# x方向変位
# y方向変位
# ```
#
# の2つの自由度があります。
#
# 今回の節点は3つなので、自由度の総数は、
#
# $$3\times2=6$$
#
# です。
#
# 自由度を次のように番号付けします。
#
# ```text
# 節点A
# u0 → x方向
# u1 → y方向
#
# 節点B
# u2 → x方向
# u3 → y方向
#
# 節点C
# u4 → x方向
# u5 → y方向
# ```
#
# したがって、節点変位ベクトルは、
#
# $$\mathbf{u} = \begin{bmatrix} u_0 \\ u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \end{bmatrix}$$
#
# となります。

#%%
# 2次元トラスでは、各節点にx方向・y方向の2自由度があります。
# したがって、節点数 × 2 が全体の自由度数です。
ndof = 2 * len(nodes)

# 変位ベクトルを、全自由度がまだ変位していない状態で初期化します。
u = np.zeros(ndof)

print(u)

#%% [markdown]
# # 6. 荷重ベクトルを作る
#
# 次に荷重を定義します。
#
# 今回は節点Cに10 kNの下向き荷重を作用させます。
#
# SI単位系を使用するため、
#
# ```text
# 10 kN = 10000 N
# ```
#
# です。
#
# 荷重ベクトルは、
#
# $$\mathbf{f} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ -10000 \end{bmatrix}$$
#
# となります。

#%%
# 荷重はNで入力します（10 kN = 10,000 N）。
P = 10_000.0

# 荷重ベクトルも自由度の並び [Aのx, Aのy, Bのx, ...] に合わせます。
f = np.zeros(ndof)

# 節点Cのy方向自由度は5番目です。下向きなので符号はマイナスです。
f[5] = -P

print(f)

#%% [markdown]
# # 7. 部材の長さを求める
#
# 次に、それぞれの部材について長さを求めます。
#
# 2点、
#
# ```text
# (xi, yi)
# (xj, yj)
# ```
#
# を結ぶ部材の長さは、
#
# $$L_e = \sqrt{(x_j-x_i)^2 + (y_j-y_i)^2}$$
#
# です。

#%%
def member_length(nodes, i, j):
    """節点iと節点jを結ぶ部材の長さ[m]を返します。"""
    dx = nodes[j, 0] - nodes[i, 0]
    dy = nodes[j, 1] - nodes[i, 1]

    return np.hypot(dx, dy)


for i, j in members:
    L = member_length(nodes, i, j)
    print(f"{i}-{j}: {L:.3f} m")

#%% [markdown]
# # 8. 部材の方向を表す
#
# トラス部材は水平・鉛直とは限りません。
#
# 例えばA-C部材には、
#
# ```text
# x方向成分
# y方向成分
# ```
#
# があります。
#
# そこで、部材の方向を表すために方向余弦を使用します。
#
# 部材の長さを `L_e` とすると、
#
# $$c = \frac{x_j-x_i}{L_e}$$
#
# $$s = \frac{y_j-y_i}{L_e}$$
#
# です。ここで、
#
# ```text
# c = cos θ
# s = sin θ
# ```
#
# に対応します。

#%%
def direction_cosines(nodes, i, j):
    """部材の方向を表す cos(theta), sin(theta) を返します。"""
    dx = nodes[j, 0] - nodes[i, 0]
    dy = nodes[j, 1] - nodes[i, 1]

    L = np.hypot(dx, dy)

    c = dx / L
    s = dy / L

    return c, s


c, s = direction_cosines(nodes, 0, 2)

print(f"c = {c:.6f}")
print(f"s = {s:.6f}")

#%% [markdown]
# # 9. トラス要素の剛性
#
# ここで、構造解析で重要になる概念が **剛性** です。
#
# ばねをイメージすると分かりやすいでしょう。
#
# ばねでは、
#
# $$F = k\delta$$
#
# という関係があります。部材の軸方向剛性は、
#
# $$\frac{EA}{L_e}$$
#
# です。
#
# ここで、
#
# * `E`：ヤング係数
# * `A`：断面積
# * `L_e`：部材長
#
# です。
#
# # 10. 要素剛性行列
#
# 2次元トラス部材について、全体座標系で表した要素剛性行列は、
#
# $$\mathbf{k}^{(e)} = \frac{EA}{L_e} \begin{bmatrix} c^2 & cs & -c^2 & -cs\\ cs & s^2 & -cs & -s^2\\ -c^2 & -cs & c^2 & cs\\ -cs & -s^2 & cs & s^2 \end{bmatrix}$$
#
# となります。

#%%
def truss_element_stiffness(E, A, nodes, i, j):
    """2次元トラス部材の4×4要素剛性行列を作成します。

    Eはヤング係数[Pa]、Aは断面積[m^2]です。
    """
    xi, yi = nodes[i]
    xj, yj = nodes[j]

    dx = xj - xi
    dy = yj - yi

    L = np.hypot(dx, dy)

    c = dx / L
    s = dy / L

    factor = E * A / L

    k = factor * np.array([
        [ c*c,  c*s, -c*c, -c*s],
        [ c*s,  s*s, -c*s, -s*s],
        [-c*c, -c*s,  c*c,  c*s],
        [-c*s, -s*s,  c*s,  s*s],
    ])

    return k

#%% [markdown]
# # 11. 実際に要素剛性行列を確認する
#
# ここではヤング係数 $E = 200\ \mathrm{GPa}$、断面積 $A = 1.0 \times 10^{-3}\ \mathrm{m^2}$ として、斜材 AC（節点 0 と節点 2）の要素剛性行列（4×4）を計算してみます。

#%%
E = 200e9
A_cs = 1.0e-3

k_ac = truss_element_stiffness(
    E,
    A_cs,
    nodes,
    0,
    2,
)

print(k_ac)

#%% [markdown]
# # 12〜14. 全体剛性行列を組み立てる
# 各部材の要素剛性行列を、対応する全体自由度へ足し合わせます。

#%%
def element_dofs(i, j):
    """部材(i, j)に対応する全体自由度番号を返します。"""
    return [
        2 * i,
        2 * i + 1,
        2 * j,
        2 * j + 1,
    ]


# 全体剛性行列Kは、全自由度同士の関係を表す行列です。
K = np.zeros((ndof, ndof))

for i, j in members:
    k = truss_element_stiffness(
        E,
        A_cs,
        nodes,
        i,
        j,
    )

    # 要素行列の4自由度を、全体行列の該当位置へ加算します。
    dofs = element_dofs(i, j)
    K[np.ix_(dofs, dofs)] += k

print(K)

#%% [markdown]
# # 15. 境界条件を設定する
#
# 支持条件：
#
# ```text
# A：ux = 0, uy = 0 (自由度 0, 1)
# B：uy = 0 (自由度 3)
# ```

#%%
# Aはx・y方向を固定し、Bはy方向だけを固定します。
# 固定自由度を除いた部分行列 K_ff だけを解くことで、既知の変位0を反映します。
fixed_dofs = [0, 1, 3]

all_dofs = np.arange(ndof)

free_dofs = np.setdiff1d(
    all_dofs,
    fixed_dofs,
)

print("固定自由度:", fixed_dofs)
print("自由自由度:", free_dofs)

#%% [markdown]
# # 16. `Ku=f` を解く
#
# 拘束されていない自由度（`free_dofs`）に対応する部分行列 $\mathbf{K}_{ff}$ と荷重ベクトル $\mathbf{f}_f$ を取り出し、`np.linalg.solve()` で未知の節点変位を求めます。

#%%
# 未知変位に対応する部分行列と荷重だけを取り出して解きます。
K_ff = K[np.ix_(free_dofs, free_dofs)]
f_f = f[free_dofs]

u_free = np.linalg.solve(
    K_ff,
    f_f,
)

u = np.zeros(ndof)
u[free_dofs] = u_free

print(u)

#%% [markdown]
# # 17. 解析全体を1つのコードにまとめる
# # 18. 節点変位を確認する
#
# 求まった節点変位 `u` の単位は [m] なので、1000倍して [mm] 単位に換算し、各節点の $x$ 方向・$y$ 方向変位を確認します。

#%%
# まとめコードとして節点変位をミリメートル単位で表示
print("節点変位")

for i in range(len(nodes)):
    ux = u[2 * i]
    uy = u[2 * i + 1]

    print(
        f"節点{i}: "
        f"ux = {ux * 1000:.6f} mm, "
        f"uy = {uy * 1000:.6f} mm"
    )

#%% [markdown]
# # 19. 支点反力を求める
#
# $$\mathbf{r} = \mathbf{K}\mathbf{u} - \mathbf{f}$$

#%%
reactions = K @ u - f

print("支点反力")

for dof in fixed_dofs:
    print(
        f"自由度 {dof}: "
        f"{reactions[dof] / 1000:.3f} kN"
    )

#%% [markdown]
# # 20. 部材軸力を求める
# # 21. なぜ斜材が圧縮になるのか
#
# 節点 C に下向き荷重が作用すると、頂点 C が下がるとともに斜材 AC・BC が押し縮められ（圧縮）、下弦材 AB は左右に引き伸ばされます（引張）。
#
# 部材軸方向の変形：
#
# $$\delta_e = -c u_i - s v_i + c u_j + s v_j$$
#
# 部材軸力：
#
# $$N_e = \frac{EA}{L_e} \delta_e$$

#%%
def member_axial_force(E, A, nodes, i, j, u):
    """部材の伸びから軸力[N]を計算します。

    正の値は引張、負の値は圧縮を表します。
    """
    xi, yi = nodes[i]
    xj, yj = nodes[j]

    dx = xj - xi
    dy = yj - yi

    L = np.hypot(dx, dy)

    c = dx / L
    s = dy / L

    dofs = element_dofs(i, j)

    ue = u[dofs]

    extension = (
        -c * ue[0]
        -s * ue[1]
        +c * ue[2]
        +s * ue[3]
    )

    N = E * A / L * extension

    return N


print("部材軸力")
for i, j in members:
    N = member_axial_force(
        E,
        A_cs,
        nodes,
        i,
        j,
        u,
    )

    print(
        f"{i}-{j}: "
        f"{N / 1000:.3f} kN"
    )

#%% [markdown]
# # 22. 変形を可視化する
#
# 実際の弾性変位はごく小さいため、グラフ上では見やすくするために `scale = 1000` 倍に拡大して変形前後の形状を重ねて描画します（`scale` は描画用であり、計算結果の `u` 自体は変更しません）。

#%%
# 実際の変位は非常に小さいため、図では1000倍に拡大して表示します。
# scaleは表示用であり、計算した変位uそのものは変更しません。
scale = 1000

deformed_nodes = nodes.copy()

for i in range(len(nodes)):
    deformed_nodes[i, 0] += scale * u[2 * i]
    deformed_nodes[i, 1] += scale * u[2 * i + 1]

fig, ax = plt.subplots(figsize=(7, 5))

# 元のトラス
for i, j in members:
    ax.plot(
        [nodes[i, 0], nodes[j, 0]],
        [nodes[i, 1], nodes[j, 1]],
        color="gray",
        linestyle="--",
        linewidth=1.5,
        label="Original" if (i, j) == members[0] else None,
    )

# 変形後
for i, j in members:
    ax.plot(
        [deformed_nodes[i, 0], deformed_nodes[j, 0]],
        [deformed_nodes[i, 1], deformed_nodes[j, 1]],
        color="tab:blue",
        linewidth=2,
        label="Deformed" if (i, j) == members[0] else None,
    )

# 変形後の節点
ax.scatter(
    deformed_nodes[:, 0],
    deformed_nodes[:, 1],
    color="tab:blue",
    zorder=3,
)

ax.set_aspect("equal")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title(
    f"Truss Deformation "
    f"(scale = {scale}x)"
)
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()

#%% [markdown]
# # 23. 部材軸力を色で表示する
#
# 引張部材を赤、圧縮部材を青とし、軸力の大きさに応じて線の太さを変えて可視化します。

#%%
fig, ax = plt.subplots(figsize=(7, 5))

forces = []

for i, j in members:
    N = member_axial_force(
        E,
        A_cs,
        nodes,
        i,
        j,
        u,
    )
    forces.append(N)

max_force = max(
    abs(N) for N in forces
)

for (i, j), N in zip(members, forces):
    if N >= 0:
        color = "tab:red"
    else:
        color = "tab:blue"

    linewidth = (
        2
        + 5 * abs(N) / max_force
    )

    ax.plot(
        [nodes[i, 0], nodes[j, 0]],
        [nodes[i, 1], nodes[j, 1]],
        color=color,
        linewidth=linewidth,
    )

    x_mid = (
        nodes[i, 0] + nodes[j, 0]
    ) / 2

    y_mid = (
        nodes[i, 1] + nodes[j, 1]
    ) / 2

    ax.text(
        x_mid,
        y_mid,
        f"{N / 1000:.2f} kN",
        ha="center",
        va="center",
        bbox=dict(
            fc="white",
            ec="none",
            alpha=0.8,
        ),
    )

ax.scatter(
    nodes[:, 0],
    nodes[:, 1],
    color="white",
    edgecolors="black",
    s=100,
    zorder=3,
)

ax.set_aspect("equal")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title("Truss Member Axial Forces")
ax.grid(True)

plt.tight_layout()
plt.show()

#%% [markdown]
# # 24. 理論値と比較する
# # 25. Pythonで理論値との誤差を確認する
#
# この静定三角形トラス（底辺 $4\ \mathrm{m}$、高さ $3\ \mathrm{m}$、斜材長さ $\sqrt{2^2 + 3^2} = \sqrt{13}\ \mathrm{m}$）では、節点法のつり合いから次の理論解が得られます。
#
# * 斜材（AC・BC）の軸力: $N_{\text{diag}} = -\dfrac{\sqrt{13}}{6}P$（圧縮）
# * 下弦材（AB）の軸力: $N_{AB} = \dfrac{P}{3}$（引張）
#
# 有限要素法で求めた値がこれらと一致するかを `np.isclose()` で検証します。

#%%
# 理論値
N_diagonal_theory = (
    -P * np.sqrt(13) / 6
)

N_bottom_theory = (
    P / 3
)

print(
    "斜材の理論値:",
    f"{N_diagonal_theory / 1000:.6f} kN"
)

print(
    "下弦材の理論値:",
    f"{N_bottom_theory / 1000:.6f} kN"
)

computed_forces = []

for i, j in members:
    N = member_axial_force(
        E,
        A_cs,
        nodes,
        i,
        j,
        u,
    )
    computed_forces.append(N)

print(
    "AB:",
    np.isclose(
        computed_forces[0],
        N_bottom_theory,
        rtol=1e-6,
    ),
)

print(
    "AC:",
    np.isclose(
        computed_forces[1],
        N_diagonal_theory,
        rtol=1e-6,
    ),
)

print(
    "BC:",
    np.isclose(
        computed_forces[2],
        N_diagonal_theory,
        rtol=1e-6,
    ),
)

#%% [markdown]
# # 26. 力のつり合いも確認する
#
# 全体の鉛直方向の力のつり合い $R_{Ay} + R_{By} - P = 0$ が数値誤差の範囲内で成立していることを確認します。

#%%
RA_y = reactions[1]
RB_y = reactions[3]

vertical_balance = (
    RA_y
    + RB_y
    - P
)

print(
    f"鉛直方向のつり合い: "
    f"{vertical_balance:.6e} N"
)

print(
    "つり合いが成立:",
    np.isclose(
        vertical_balance,
        0.0,
        atol=1e-8,
    ),
)

#%% [markdown]
# # 27. 剛性を変えてみる
#
# 部材の断面積 $A$ を変化させたとき、軸剛性 $EA/L$ の増加に伴って節点 C の鉛直変位が反比例して小さくなることを確認します。

#%%
areas = np.array([
    0.5e-3,
    1.0e-3,
    2.0e-3,
    4.0e-3,
])

for A_test in areas:
    K_test = np.zeros((ndof, ndof))

    for i, j in members:
        k = truss_element_stiffness(
            E,
            A_test,
            nodes,
            i,
            j,
        )

        dofs = element_dofs(i, j)

        K_test[np.ix_(dofs, dofs)] += k

    K_ff = K_test[
        np.ix_(free_dofs, free_dofs)
    ]

    u_test = np.zeros(ndof)

    u_test[free_dofs] = np.linalg.solve(
        K_ff,
        f[free_dofs],
    )

    displacement = abs(u_test[5])

    print(
        f"A = {A_test:.2e} m² : "
        f"|uy(C)| = {displacement * 1000:.6f} mm"
    )

#%% [markdown]
# # 28. ヤング係数を変えてみる
#
# 断面積 $A = 1.0 \times 10^{-3}\ \mathrm{m^2}$ を固定したままヤング係数 $E$ を 100〜250 GPa の範囲で変え、材料の剛性が高くなるほど節点 C の変位が反比例して小さくなることを確認します。

#%%
youngs_moduli = np.array([
    100e9,
    150e9,
    200e9,
    250e9,
])

for E_test in youngs_moduli:
    K_test = np.zeros((ndof, ndof))

    for i, j in members:
        k = truss_element_stiffness(
            E_test,
            A_cs,
            nodes,
            i,
            j,
        )

        dofs = element_dofs(i, j)

        K_test[np.ix_(dofs, dofs)] += k

    K_ff = K_test[
        np.ix_(free_dofs, free_dofs)
    ]

    u_test = np.zeros(ndof)

    u_test[free_dofs] = np.linalg.solve(
        K_ff,
        f[free_dofs],
    )

    displacement = abs(u_test[5])

    print(
        f"E = {E_test / 1e9:.0f} GPa : "
        f"|uy(C)| = {displacement * 1000:.6f} mm"
    )

#%% [markdown]
# # 29. 荷重を変えてみる
#
# 線形静解析では $\mathbf{K}\mathbf{u} = \mathbf{f}$ が成り立つため、構造や材料条件が同じであれば、荷重 $P$ を 2 倍・4 倍にすると変位も比例して 2 倍・4 倍になります。

#%%
# 荷重以外の条件（E、断面積、支持条件）は基準モデルに戻します。
# 直前の「ヤング係数を変えてみる」で K_ff が上書きされているため、
# ここでは基準値 E=200 GPa の全体剛性行列 K から作り直します。
K_ff = K[np.ix_(free_dofs, free_dofs)]

loads = np.array([
    5_000,
    10_000,
    20_000,
    40_000,
])

for P_test in loads:
    f_test = np.zeros(ndof)
    f_test[5] = -P_test

    u_test = np.zeros(ndof)

    u_test[free_dofs] = np.linalg.solve(
        K_ff,
        f_test[free_dofs],
    )

    print(
        f"P = {P_test / 1000:.1f} kN : "
        f"uy(C) = {u_test[5] * 1000:.6f} mm"
    )

#%% [markdown]
# # 30. 計算処理を関数にまとめる
#
# ここまでの処理（要素剛性行列の作成 → 全体剛性行列の組み立て → 境界条件の適用 → 連立方程式の求解 → 支点反力の計算）を 1 つの関数 `solve_truss()` にまとめ、条件を変えても再利用できるようにします。

#%%
def solve_truss(
    nodes,
    members,
    E,
    A,
    loads,
    fixed_dofs,
):
    """2次元トラスの線形静解析を行います。

    部材剛性を全体剛性行列へ組み立て、拘束されていない自由度だけを
    取り出して連立方程式を解きます。

    Parameters
    ----------
    nodes : numpy.ndarray
        節点座標 [m]
    members : list of tuple
        部材を構成する節点番号
    E : float
        ヤング係数 [Pa]
    A : float
        部材断面積 [m^2]
    loads : numpy.ndarray
        荷重ベクトル [N]
    fixed_dofs : list
        拘束する自由度番号

    Returns
    -------
    K : numpy.ndarray
        全体剛性行列
    u : numpy.ndarray
        節点変位ベクトル [m]
    reactions : numpy.ndarray
        支点反力ベクトル [N]
    """

    ndof = 2 * len(nodes)

    K = np.zeros((ndof, ndof))

    for i, j in members:
        k = truss_element_stiffness(
            E,
            A,
            nodes,
            i,
            j,
        )

        dofs = element_dofs(i, j)

        K[np.ix_(dofs, dofs)] += k

    all_dofs = np.arange(ndof)

    free_dofs = np.setdiff1d(
        all_dofs,
        fixed_dofs,
    )

    K_ff = K[
        np.ix_(free_dofs, free_dofs)
    ]

    f_f = loads[free_dofs]

    u = np.zeros(ndof)

    u[free_dofs] = np.linalg.solve(
        K_ff,
        f_f,
    )

    reactions = K @ u - loads

    return K, u, reactions

#%% [markdown]
# # 31. 関数を使って解析する
#
# 作成した `solve_truss()` に基準条件を渡して解析を実行し、先ほど手組みで求めた節点 C の変位と一致することを確認します。

#%%
f = np.zeros(ndof)
f[5] = -10_000.0

K, u, reactions = solve_truss(
    nodes=nodes,
    members=members,
    E=200e9,
    A=1.0e-3,
    loads=f,
    fixed_dofs=[0, 1, 3],
)

print(
    f"Cのx方向変位: "
    f"{u[4] * 1000:.6f} mm"
)

print(
    f"Cのy方向変位: "
    f"{u[5] * 1000:.6f} mm"
)

#%% [markdown]
# # 32. 今回の解析の流れ
#
# 今回の解析は、次の 6 ステップで進めました。
#
# 1. **モデル化**: 節点座標 `nodes` と部材接続 `members` を定義する
# 2. **要素剛性行列**: 各部材の方向余弦 $(c, s)$ から 4×4 行列を求める
# 3. **全体剛性行列**: 全自由度に対応する $\mathbf{K}$ へ各要素行列を加算する
# 4. **境界条件**: 固定自由度を除いた部分行列 $\mathbf{K}_{ff}$ を取り出す
# 5. **求解**: $\mathbf{K}_{ff}\mathbf{u}_f = \mathbf{f}_f$ を解いて節点変位を求める
# 6. **後処理**: 支点反力 $\mathbf{r} = \mathbf{K}\mathbf{u} - \mathbf{f}$ と各部材の軸力 $N_e$ を算出する
#
# # 33. 単純梁解析との違い
#
# 第8回で扱った単純梁では、等分布荷重に対するせん断力・曲げモーメント・たわみの**理論式に直接数値を代入**しました。一方、今回のトラス解析では、構造を要素に分割して剛性行列を組み立て、**連立一次方程式を解くことで任意の形状・荷重・支持条件に対応できる**点が大きく異なります。
#
# # 34. 「有限要素法」の考え方
#
# 複雑な構造物を単純な「要素（element）」と「節点（node）」の集合に分割し、各要素の力のつり合い（要素剛性行列）を全体の連立方程式へ統合して解く手法が**有限要素法（FEM）**の基本です。今回の2次元トラス解析は、有限要素法における最もシンプルで本質的な入門例といえます。
#
# # 35. NumPyが構造解析に向いている理由
#
# 有限要素法では行列・ベクトルの演算が中心になります。NumPy を使うことで、ゼロ行列の生成（`np.zeros`）、インデクシングによる全体剛性行列への加算（`np.ix_`）、連立一次方程式の求解（`np.linalg.solve`）、行列積（`@`）を数行で簡潔かつ高速に記述できます。
#
# # 36. モデルを大きくしてみる
#
# `solve_truss()` は節点数や部材数をコード内に固定せず `len(nodes)` と `members` から自動的に自由度数を計算しています。そのため、`nodes`、`members`、`loads`、`fixed_dofs` の入力データを増やすだけで、ワーレントラスやプラットトラスなどの大規模モデルへそのまま拡張できます。
#
# # 37. 複数の条件を自動計算する
#
# 関数化したことで、荷重条件を変えた多数ケースの自動計算も容易になります。ここでは荷重 $P$ を 1 kN から 50 kN まで 50 通り変化させて解析を繰り返し、荷重と節点 C の鉛直変位の線形関係をグラフで確認します。

#%%
loads = np.linspace(
    1_000,
    50_000,
    50,
)

displacements = []

for P_test in loads:
    f_test = np.zeros(ndof)
    f_test[5] = -P_test

    _, u_test, _ = solve_truss(
        nodes=nodes,
        members=members,
        E=E,
        A=A_cs,
        loads=f_test,
        fixed_dofs=[0, 1, 3],
    )

    displacements.append(
        abs(u_test[5])
    )

displacements = np.array(
    displacements
)

plt.figure(figsize=(8, 5))

plt.plot(
    loads / 1000,
    displacements * 1000,
)

plt.xlabel("Load P [kN]")
plt.ylabel("|uy(C)| [mm]")
plt.title(
    "Load vs. Vertical Displacement"
)

plt.grid(True)
plt.show()

#%% [markdown]
# # 38. 構造解析をデータ処理につなげる
#
# 複数の解析条件に対する計算結果をリストに蓄積し、`pandas.DataFrame` にまとめることで、表形式での比較、CSV ファイルへの保存、条件間の統計処理など第3回で学んだデータ分析手法へそのまま連携できます。

#%%
import pandas as pd

results = []

for P_test in [
    5_000,
    10_000,
    20_000,
    40_000,
]:
    f_test = np.zeros(ndof)
    f_test[5] = -P_test

    _, u_test, _ = solve_truss(
        nodes=nodes,
        members=members,
        E=E,
        A=A_cs,
        loads=f_test,
        fixed_dofs=[0, 1, 3],
    )

    results.append({
        "P [kN]": P_test / 1000,
        "ux_C [mm]": u_test[4] * 1000,
        "uy_C [mm]": u_test[5] * 1000,
    })

df = pd.DataFrame(results)

print(df)

#%% [markdown]
# # 39. 今回の解析モデルで重要なこと
#
# 今回のプログラムでは、非常に重要な考え方をいくつか扱いました。
#
# まず、
#
# ```text
# 構造物
# ```
#
# を、
#
# ```text
# 節点
# +
# 部材
# ```
#
# というデータに変換しました。
#
# 次に、各部材について、
#
# ```text
# 長さ
# 方向
# 剛性
# ```
#
# を計算しました。
#
# そして、それらを、
#
# ```text
# 全体剛性行列 K
# ```
#
# へ組み立てました。
#
# 最後に、
#
# $$\mathbf{K}\mathbf{u} = \mathbf{f}$$
#
# を解くことで、節点変位を求め、さらにその変位から支点反力や部材軸力を計算しました。
#
# # 40. 今回学んだこと
#
# 本回では、2次元トラス構造の有限要素法解析について次の内容を学びました。
#
# * 構造物を「節点座標（`nodes`）」と「部材接続（`members`）」のデータとしてモデル化する方法
# * 部材長さ $L$ と方向余弦 $(c, s)$ を用いて 4×4 要素剛性行列を構築する方法
# * 要素剛性行列を全体剛性行列 $\mathbf{K}$ に組み立て、境界条件を適用して $\mathbf{K}_{ff}\mathbf{u}_f = \mathbf{f}_f$ を解く手順
# * 節点変位から支点反力や部材軸力を求め、理論解および力のつり合い式で結果を検証する方法
# * `solve_truss()` として関数化し、パラメータを変えた多数ケースの自動計算と `pandas` による集計を行う流れ
#
# # 41. 次回以降につながる考え方
#
# 今回実装した「モデル化 → 要素剛性の組み立て → 境界条件の適用 → 連立方程式の求解 → 検証・可視化」という枠組みは、より大規模なトラス橋モデル、梁要素を用いたラーメン骨組解析、さらには 3 次元有限要素法へそのまま発展させられます。また、複数条件の自動計算結果を `DataFrame` として蓄積する手法は、設計最適化や機械学習のデータ生成にも直結します。
#
# # まとめ
#
# 今回は、最も基本的な 2 次元三角形トラスを題材に、有限要素法（FEM）の仕組みを NumPy と Matplotlib で一から実装しました。
#
# 特に重要なのは、
#
# > **計算プログラムがエラーなく動いたあと、理論解や力のつり合いと照合して物理的・工学的に妥当か検証すること**
#
# です。数値解析のロジックと検証の視点をあわせて身につけ、今後のより高度な工学解析に活かしていきましょう。
#
# ---
#
# ## 参考
#
# * 﨑元達郎（著）『[構造力学［第2版・新装補訂版］上 静定編](https://www.morikita.co.jp/books/mid/042514)』森北出版、2025年12月。ISBN 978-4-627-42514-9
# * Python Documentation: https://docs.python.org/3/
# * NumPy Documentation: https://numpy.org/doc/
# * Matplotlib Documentation: https://matplotlib.org/stable/
# * pandas Documentation: https://pandas.pydata.org/docs/
# * 本連載のGitHubリポジトリ: https://github.com/skyblueao77/civil-engineering-python