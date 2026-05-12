# 重力波可視化メモ / Gravitational Wave Visualization Notes

## プロジェクト名
**Spacetime Ripple Visualizer** — 時空のリップルを可視化する

## コンセプト
重力波が時空を通り過ぎる様子を描写する2D/3D可視化。Black hole merger時のspacetime curvature変化を表現。

## 数式的基盤

### 重力波の计量攝動 (Metric Perturbation)
```
h₊(t, x) = A × cos(ω(t - x/c))
h×(t, x) = A × sin(ω(t - x/c))
```

### 加動の Strain
- LIGO検出感度: h ~ 10⁻²¹
- 典型的ブラックホール合体系: M ~ 30M☉, 距離 ~ 1.3 billion light-years

## 可視化要素

1. **格子上に適用された攝動** — 時空の格子点が重力波通過時に振動
2. ** polarization cycle** — h₊ と h× の位相相差をアニメ表示
3. **ブラックホールシャドウ** — 事象的地平線の周囲の光の曲がり
4. **光子球 (Photon Sphere)** — r = 3GM/c² の領域

## 実装方針

```python
# 概念コード
import numpy as np
import matplotlib.pyplot as plt

def gravitational_wave_strain(t, x, A, omega):
    """Calculate strain at position x and time t"""
    h_plus = A * np.cos(omega * (t - x))
    h_cross = A * np.sin(omega * (t - x))
    return h_plus, h_cross

# LIGO O4 sensitivity curveも重ねて表示
```

## 参考文献

- Abramovici et al. (1992) — LIGO
- Abbott et al. (2016) — GW150914 detection
- Thorn (2009) — 3D gravitational wave visualization

## ステータス
🟡 进行中 — 実装コンセプト完成、実装待ち

---

*Created: 2026-05-13*
*Kevin — Gravitational Wave Physicist*