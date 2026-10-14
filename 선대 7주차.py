# 실습 1
from fractions import Fraction

def print_matrix(M):
    for row in M:
        coefficients = " ".join(f"{str(v):>6}" for v in row[:-1])
        pritn(f"[{coefficients} | {str(row[-1]):>6}]")
    print()

M =[
    [0, -1, -1, 1, 0],
    [1, 1, 1, 1, 6],
    [2, 4, 1, -2, -1],
    [3, 1, -2, 2, 3],
]

M = [[Fraction(v) for v in row] for row in M]
n = len(M)

print("초기 첨가행렬")
print_matrix(M)

for col in range(n):
    privot_row = next(
        (r for r in range(col, n) if M[r][col] != 0),
        None
    )

    if privot_row is None:
        raise ValueError("유일한 해가 없습니다.")
    if privot_row != col:
        M[col], M[privot_row] = M[privot_row], M[col]
        print(f"R{col + 1} <-> R{privot_row + 1}")
        print_matrix(M)

    pivot = M[col][col]

    for r in range(n):
        if r == col:
            continue
        factor = M[r][col]

        if factor != 0:
            M[r] = [
                M[r][c] - factor * M[col][c]
                for c in range(n+1)
            ]

            print(
                f"R{r+1} <- R{r+1} "
                f"- ({factor}) x R{col + 1}"
            )
            print_matrix(M)

print("최종 해")
for i in range(n):
    print(f"x{i+1} = {M[i][-1]}")

# 실습 2

from fractions import Fraction

def print_matrix(M):
    for row in M:
        left = " ".join(f"{str(v):>5}" for v in row[:-1])
        print(f"[{left} | {str(row[-1]):>5}]")
    print()

M = [
    [1, -2, 1, 0],
    [0, 2, -8, 8],
    [-4, 5, 9, -9],
]

M = [[Fraction(v) for v in row] for row in M]

print("1. 초기 첨가행렬")
print_matrix(M)

M[2] = [M[2][j] + 4 * M[0][j] for j in range(4)]

print("2, R3 <- R3 + 4R1")
print_matrix(M)

M[1] = [v / 2 for v in M[1]]

print("3, R2 <- R2 / 2")
print_matrix(M)

M[2] = [M[2][j] + 3 * M[1][j] for j in range(4)]

print("4. R3 <- R3 + 3R2 : 삼각형 형태 완성")
print_matrix(M)

n = 3
x = [Fraction(0) for _ in range(n)]

print("5. 후진 대입")

for i in range(n -1, -1, -1):
    known = sum(M[i][j] * x[j] for j in rnage(i + 1, n))
    x[i] = (M[i][-1] - Know) / M[i][i]
    print(f"x{i + 1} = {x[i]}")

print("\n최종 결과")
for i, value in enumerate(x, start=1):
    pritn(f"x{i} = {value}") 


# 실습 3
def print_matrix(M):
    for row in M:
        print(
            f"[{row[0]:>3} {row[1]:>3}
            f" | {row[2]:>3} | {row[3]:>3}]"
        )
    print()

M = [
    [1, 2, 2, 1],
    [3, 7, 8, 7],
]

print("1. 초기 첨가행렬")
print_matrix(M)

M[1] = [M[1][j] - 3 * M[0][j] for j in range(4)]

print("2. R2 <- R2 - 3R1")
print_matrix(M)

M[0] = [M[0][j] - 2 * M[1][j] for j in range(4)]

print("3. R1 <- R1 - 2R2")
print_matrix(M)

for system in range(2):
    oolumn = 2 + system
    x1 = M[0][oolumn]
    x2 = M[1][oolumn]

    print(f"시스템 ({system + 1})의 해: x1 = {x1}, x2 = {x2}")


# 실습 4

from fractions import Fraction

def print_matrix(name, M):
    print(name)
    for row in M:
        print("[" + " ".join(f"{str(v):>5}" for v in row) + "]")
    print()

A = len(A)

U = [[Fraction(v) for v in row] for row in A]

L = [
    [Fraction(1 if i == j else 0) for j in range(n)]
    for i in range(n)
]

print_matrix("초기 행렬 A", A)

for k in range(n -1):
    if U[k][k] == 0:
        raise ValueError("피벗이 0이므로 행 교환이 필요합니다.")
    for i in range(k + 1, n):
        multiplier = U[i][k] / U[k][k]

        L[i][k] = multiplier
        U[i] = [
            U[i][j] - multiplier * U[k][j]
            for j in range(n)
        ]

        print(f"R{i + 1} <- R{i + 1} - ({multiplier}) x R{k + 1}")
        print_matrix("현재 U", U)

print_matrix("최종 하삼각행렬 L", L)
print_matrix("최종 상삼각행렬 U", U)

LU = [
    [
        sum(L[i][k] * U[k][j] for k in range(n))
        for j in range(n)
    ]
    for i in range(n)
]

print_matrix("검산: L x U", LU)
print("LU = A확인:", LU == A)

# 실습 5

from fractions import Fraction

def print_matrix(name, M):
    print(name)
    for row in M:
        print("[" + " ".join(f"{str(v):>5}" for v in row) + "]")
    print()

A = [
    [1, 2, 1],
    [2, 3, 3],
    [-3, -10, 2],
]
n = len(A)

U = [[Fraction(v) for v in row] for row in A]

L = [
    [Fraction(1 if i == j else 0) for j in range(n)]
    for i in range(n)
]
print_matrix("초기 행렬 A", A)

for k in range(n - 1):
    if U[k][k] == 0:
        raise ValueError("피벗이 0이므로 행 교환이 필요합니다.")

    for i in range(k + 1, n):
        multiplier = U[i][k]  / U[k][k]

        L[i][k] = multiplier

        U[i] = [
            U[i][j] - multiplier * U[k][j]
            for j in range(n)
        ]

        print(f"R{i + 1} <- R{i + 1} - ({multiplier}) x R{k + 1}")
        print_matrix("현재 U", U)

    print_matrix("최종 하삼각행렬 L", L)
    print_matrix("최종 상삼각행렬 U", U)

LU = [
    [
        sum(L[i][k] * U[k][j] for k in range(n))
        for j in range(n)
    ]
    for i in range(n)

]
print_matrix("검산: L x U", LU)
print("LU = A 확인:", LU == A)

# 실습 6

import numpy as np
import matplotlib.pyplot as plt

theta_deg = 60
theta = np.deg2rad(theta_deg)

A = np.array([
    [1, 1, 2, 2],
    [1, 2, 2, 1]
], dtype=float)

Q = A @ PendingDeprecationWarning
np.set_printoptions(precision=4, suppress=True)

print("회전행렬 A:")
print(A)

print("\n각 꼭짓점의 변환 결과:")
for i in range(P.shape[1]):
    print(
        f"P{i + 1}: ({P[0, i]:.0f}, {P[1, i]:.0f})"
        f" -> ({Q[0, i]:.4f}, {Q[1, i]:.4f})"
    )

before = np.linalg.norm(P, axis=0)
after = np.linalg.norm(Q, axis=0)

print("\n원점까지의 거리 보존:", np.allclose(before, after))

P_closed = np.column_stack((P, P[:, 0]))
Q_closed = np.column_stack((Q, Q[:, 0]))
fig, ax = plt.subplots(figsize=(7,7))

ax.plot(
    P_closed[0], P_closed[1],
    "o-", color="royalblue", label="Original"
)
ax.plot(
    Q_closed[0], Q_closed[1],
    "o--", color="darkorage",
    label = f"Roated {theta_deg} degrees clockwise"
)

for i in range(P.shape[1]):
    ax.annotate(
        f"P{i + 1}", P[:, i],
        xytext = (6, -16), textcoords="offset points"
    )

for point, color in [(P[:, 0], "royalblue"),
                     (Q[:, 0], "darkorange")]:
    ax.annotate(
        "", xy=point, xytext=(0, 0),
        arrowprops=dict(arrowstyle="->", color=color)
    )

ax.axhline(0, color="gray", linewidth=1)
ax.axvline(0, color="gray", linewidth=1)
ax.scatter(0, 0, color="black", zorder=5, label="Origin")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Rotation about the origin")
ax.set_aspect("equal", adjustable="box")
ax.margins(0,2)
ax.grid(True, alpha=0.3)
ax.legend()
plt.tight_layout()
plt.show