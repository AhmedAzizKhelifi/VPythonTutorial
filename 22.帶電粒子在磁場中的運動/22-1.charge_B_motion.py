"""
 VPython教學: 22-1.帶電粒子在磁場中的運動
 Ver. 1: 2018/4/8
 Ver. 2: 2019/9/16
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
    (1) 速度只有 x 方向分量, 沿著 x 軸等速度運動: theta = 0, phi = 0
    (2) 速度沒有 x 方向分量, 在 yz 平面上做等速圓周運動: theta = 90, phi = 0
    (3) 速度沒有 x 方向分量, 在 yz 平面上做等速圓周運動: theta = 0, phi = 90
    (4) 速度與 x 軸夾角 != 0 or 180, 螺線運動, e.g. theta = 80, phi = 80
    (5) 速度與 x 軸夾角 != 0 or 180, 螺線運動, e.g. theta = 100, phi = 80
"""
size, m, q = 0.005, 1E-10, 1E-9 # 粒子半徑, 質量, 電量
theta = radians(80)            # 粒子初速度與 xy 平面夾角
phi = radians(80)              # 粒子初速度在 xy 平面投影與 x 軸夾角
v0 = 10*vec(cos(theta)*cos(phi), cos(theta)*sin(phi), sin(theta))  # 粒子初速度
L = 0.4                      # 坐標軸長度
B_field = vec(10, 0, 0)      # 磁場
t, dt = 0, 1E-5              # 時間, 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗, 依照 theta 和 phi 旋轉視角
scene = canvas(title="Charged Particle in Magnetic Field", width=800, height=600, x=0, y=0, 
               center=vec(0, 0, 0), range=0.6*L, background=color.black)
if(theta == pi/2 or phi == pi/2):
    scene.camera.pos = vec(L, L/4, L/4)
    scene.camera.axis = vec(-L, -L/4, -L/4)
else:
    scene.camera.pos = vec(L/4, L/4, L)
    scene.camera.axis = vec(-L/4, -L/4, -L)
# 產生帶電粒子
charge = sphere(pos=vec(0, 0, 0), radius=2*size, v=v0, color=color.red, m=m, make_trail=True, retain = 1000)
# 產生坐標軸及標籤
arrow_x = arrow(pos=vec(-L/2, 0, 0), axis=vec(L, 0, 0), shaftwidth=0.6*size, color=color.yellow)
label_x = label(pos=vec(L/2, 0, 0), text="x", xoffset=25, color=color.yellow, font="sans")
arrow_y = arrow(pos=vec(0, -L/2, 0), axis=vec(0, L, 0), shaftwidth=0.6*size, color=color.yellow)
label_y = label(pos=vec(0, L/2, 0), text="y", yoffset=25, color=color.yellow, font="sans")
arrow_z = arrow(pos=vec(0, 0, -L/2), axis=vec(0, 0, L), shaftwidth=0.6*size, color=color.yellow)
label_z = label(pos=vec(0, 0, L/2), text="z", xoffset=-25, yoffset=-25, color=color.yellow, font="sans")
# 產生表示磁場的箭頭及標籤
arrow_B = arrow(pos=vec(-L/2, 0, 0), axis=B_field.norm()*0.1, shaftwidth=size, color=color.green)
label_B = label(pos=vec(-L/2, 0, 0), text="B", xoffset=25, yoffset=25, color=color.green, font="sans")
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos=charge.pos, shaftwidth=0.5*size, color=color.blue)
arrow_a = arrow(pos=charge.pos, shaftwidth=0.5*size, color=color.magenta)

"""
 3. 物體運動部分
"""
while(abs(charge.pos.x) < 0.6*L and abs(charge.pos.y) < 0.6*L and abs(charge.pos.z) < 0.6*L):
    rate(500)
# 計算帶電粒子所受合力, 更新帶電粒子加速度、速度、位置
    F = q*cross(charge.v, B_field)
    charge.a = F/charge.m
    charge.v += charge.a*dt
    charge.pos += charge.v*dt
# 更新表示速度、加速度的箭頭, 只畫出方向以避免動畫自動縮小
    arrow_v.pos = charge.pos
    arrow_a.pos = charge.pos
    arrow_v.axis = charge.v.norm()*0.1
    arrow_a.axis = charge.a.norm()*0.1
# 更新時間
    t += dt
