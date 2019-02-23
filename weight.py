import numpy


height = 1.690
weight = 60
foot_length = 
leg_length = 
arm_length = 0.3
forearm_length = 0.25



#重力加速度****************************************************************
gravity = [0, 0, -9.80665]  #重力加速度
g = 9.80665
# 被者者データ    ""A""    ************************************************
# height = SampleDataA(1,1)   #身長
# weight = SampleDataA(1,2)    #体重59.8kg
# foot_length = SampleDataA(1,3)   #足長さ
# leg_length = SampleDataA(1,4)    #下腿長さ
# thigh_length = SampleDataA(1,5)   #大腿長さ
# torso_length = SampleDataA(1,6)  #胴長さ
# head_length = SampleDataA(1,7)    #頭長さ
#arm_length = ave_arm_length    #上腕長さ
#forearm_length = ave_forearm_length #前腕長さ
#hand_length = ave_hand_length   #手長さ
#l_length = l_length + 0.01
#r_length = r_length + 0.01
#慣性テンソル推定*******************************************************
foot_inertia = zeros(3,3)
    foot_inertia(1,1) = (-38.9258 + 214.578*foot_length + 0.01445*weight)/10000
    foot_inertia(2,2) = (-6.29702 + 37.6738*foot_length + 0.01248*weight)/10000
    foot_inertia(3,3) = (-40.9844 + 228.138*foot_length + 0.00753*weight)/10000
leg_inertia = zeros(3,3)
    leg_inertia(1,1) = (-1190.24 + 3093.33*leg_length + 5.27481*weight)/10000
    leg_inertia(2,2) = (-1174.66 + 3048.1 *leg_length + 5.19169*weight)/10000
    leg_inertia(3,3) = (-62.7928 + 104.746*leg_length + 1.10838*weight)/10000
thigh_inertia = zeros(3,3)
    thigh_inertia(2,2) = (-2043.38 + 5547.75*thigh_length + 10.6498*weight)/10000
    thigh_inertia(3,3) = (-350.308 + 418.338*thigh_length + 6.6271 *weight)/10000
torso_inertia = zeros(3,3)
    torso_inertia(1,1) = (-6157.42  + 15247.8*torso_length*(1-163/592) + 58.0109*weight)/10000
    torso_inertia(2,2) = (-6423.4   + 15063.0*torso_length*(1-163/592) + 71.5226*weight)/10000
    torso_inertia(3,3) = (-2016.55  - 1516.61*torso_length*(1-163/592) + 48.8973*weight)/10000
#torso_inertia(1,1) = (-25180.2 + 43095.5*torso_length + 200.723*weight)/10000
#torso_inertia(2,2) = (-25902.6 + 43759.1*torso_length + 217.775*weight)/10000
#torso_inertia(3,3) = (-2482.2  -385.282*torso_length + 83.2293*weight)/10000

pelvis_inertia = zeros(3,3)
 pelvis_inertia(1,1) = (-1687.06 + 5588.38*torso_length*163/592 + 22.6268*weight)/10000
 pelvis_inertia(2,2) = (-1982.55 + 6516.01*torso_length*163/592 + 27.7046*weight)/10000
 pelvis_inertia(3,3) = (-1376.85 - 2246.6 *torso_length*163/592 + 29.075 *weight)/10000
#{
arm_inertia = zeros(3,3)
arm_inertia(1,1) = (-317.679 + 1007.85*arm_length + 1.85249*weight)/10000
arm_inertia(2,2) = (-312.14 + 999.691*arm_length + 1.74277*weight)/10000
arm_inertia(3,3) = (-11.1029 -44.8794*arm_length + 0.71203*weight)/10000
forearm_inertia = zeros(3,3)
forearm_inertia(1,1) = (-145.867 + 562.219*forearm_length + 0.85722*weight)/10000
forearm_inertia(2,2) = (-146.449 + 576.661*forearm_length + 0.79727*weight)/10000
forearm_inertia(3,3) = (-13.4756 + 26.3785*forearm_length + 0.24644*weight)/10000
hand_inertia = zeros(3,3)
hand_inertia(1,1) = (-6.36541 + 80.3581*hand_length + 0.10995*weight)/10000
hand_inertia(2,2) = (-7.30695 + 82.0684*hand_length + 0.14433*weight)/10000
hand_inertia(3,3) = (-1.67255 + 9.0812*hand_length + 0.05381*weight)/10000
#}
head_inertia = zeros(3,3)
    head_inertia(1,1) = (-367.903 + 2843.24*head_length + 2.71413*weight)/10000
    head_inertia(2,2) = (-354.077 + 2680.71*head_length + 2.4924*weight)/10000
    head_inertia(3,3) = (-138.956 + 1307.37*head_length + 1.24856*weight)/10000
    
display(head_inertia)
display(torso_inertia)
display(thigh_inertia)
#体節質量推定**************************************************************
foot_weight     =  -0.26784 + 2.61804*foot_length  + 0.00545*weight
leg_weight      =  -1.71524 + 6.04396*leg_length   + 0.03885*weight
thigh_weight    =  -4.53542 + 14.5253*thigh_length + 0.09324*weight
pelvis_weight   = (-10.1647 + 18.7503*torso_length + 0.48275*weight) * (163/592)#座位時の肩峰高/超骨稜高
head_weight     =  -1.1968  + 25.9526*head_length  + 0.02604*weight
torso_weight    = weight-(foot_weight+leg_weight+thigh_weight)*2-pelvis_weight-head_weight
#arm_weight = -0.36785 + 1.15588*arm_length + 0.02712*weight
#forearm_weight = -0.43807 + 2.22923*forearm_length + 0.01397*weight
#hand_weight = -0.01474 + 2.09424*hand_length + 0.00414*weight
#torso_weight = (-10.1647 + 18.7503*torso_length + 0.48275*weight) * 0.43/0.54
#マーカ位置読み込み(必要なものだけ)**********************************************
# marker_name(1=x:2=y:3=z,1,k) = marker_position(k,marker_number * 1→3:2→3+1:3→3+2)/1000
#1000で割るのは単位をmmからmに変換するため
headF=zeros([3,1,analysis_frame])headR=zeros([3,1,analysis_frame])
headD=zeros([3,1,analysis_frame])headT=zeros([3,1,analysis_frame])
C7=zeros([3,1,analysis_frame])  neckF=zeros([3,1,analysis_frame])
R_ill=zeros([3,1,analysis_frame])L_ill=zeros([3,1,analysis_frame])
R_asis=zeros([3,1,analysis_frame])L_asis=zeros([3,1,analysis_frame])
Sacral=zeros([3,1,analysis_frame])C_asis=zeros([3,1,analysis_frame])
R_knee_out=zeros([3,1,analysis_frame])R_knee_in=zeros([3,1,analysis_frame])
R_ankle_out=zeros([3,1,analysis_frame])R_ankle_in=zeros([3,1,analysis_frame])
R_toe=zeros([3,1,analysis_frame])R_heel=zeros([3,1,analysis_frame])
R_shoulder=zeros([3,1,analysis_frame])L_knee_out=zeros([3,1,analysis_frame])
L_knee_in=zeros([3,1,analysis_frame])L_ankle_out=zeros([3,1,analysis_frame])
L_ankle_in=zeros([3,1,analysis_frame])L_toe=zeros([3,1,analysis_frame])
L_heel=zeros([3,1,analysis_frame])L_shoulder=zeros([3,1,analysis_frame])
R_elb=zeros([3,1,analysis_frame])L_elb=zeros([3,1,analysis_frame])
Body_R=zeros([3,1,analysis_frame])Body_L=zeros([3,1,analysis_frame])
for k in analysis_frame
    #頭部位置同定
    headF(:,1,k) = Marker_Pos(k,1*3+0:1*3+2)/1000#front
    headT(:,1,k) = Marker_Pos(k,2*3+0:2*3+2)/1000#top
    headR(:,1,k) = Marker_Pos(k,3*3+0:3*3+2)/1000#rear
    headD(:,1,k) = Marker_Pos(k,4*3+0:4*3+2)/1000#dummy
    #体幹位置同定
    C7(:,1,k)         = Marker_Pos(k,5*3+0:5*3+2)/1000
    neckF(:,1,k)      = Marker_Pos(k,6*3+0:6*3+2)/1000
    R_shoulder(:,1,k) = Marker_Pos(k,7*3+0:7*3+2)/1000
    L_shoulder(:,1,k) = Marker_Pos(k,8*3+0:8*3+2)/1000
    R_elb(:,1,k)      = Marker_Pos(k,10*3+0:10*3+2)/1000
    L_elb(:,1,k)      = Marker_Pos(k,12*3+0:12*3+2)/1000
    Body_R(:,1,k)     = Marker_Pos(k,14*3+0:14*3+2)/1000
    Body_L(:,1,k)     = Marker_Pos(k,16*3+0:16*3+2)/1000
    #腰周り座標
    R_ill(:,1,k)    = Marker_Pos(k,17*3+0:17*3+2)/1000
    L_ill(:,1,k)    = Marker_Pos(k,18*3+0:18*3+2)/1000
    R_asis(:,1,k)   = Marker_Pos(k,19*3+0:19*3+2)/1000
    L_asis(:,1,k)   = Marker_Pos(k,20*3+0:20*3+2)/1000
    Sacral(:,1,k)   = Marker_Pos(k,21*3+0:21*3+2)/1000
    #下肢位置同定
    R_knee_out(:,1,k)   = Marker_Pos(k,23*3+0:23*3+2)/1000
    R_knee_in(:,1,k)    = Marker_Pos(k,24*3+0:24*3+2)/1000
    R_ankle_out(:,1,k)  = Marker_Pos(k,25*3+0:25*3+2)/1000
    R_ankle_in(:,1,k)   = Marker_Pos(k,26*3+0:26*3+2)/1000
    R_heel(:,1,k)       = Marker_Pos(k,27*3+0:27*3+2)/1000
    R_toe(:,1,k)        = Marker_Pos(k,28*3+0:28*3+2)/1000
    L_knee_out(:,1,k)   = Marker_Pos(k,30*3+0:30*3+2)/1000
    L_knee_in(:,1,k)    = Marker_Pos(k,31*3+0:31*3+2)/1000
    L_ankle_out(:,1,k)  = Marker_Pos(k,32*3+0:32*3+2)/1000
    L_ankle_in(:,1,k)   = Marker_Pos(k,33*3+0:33*3+2)/1000
    L_heel(:,1,k)       = Marker_Pos(k,34*3+0:34*3+2)/1000
    L_toe(:,1,k)        = Marker_Pos(k,35*3+0:35*3+2)/1000
    #関節中心座標の準備
    cervical_JC     = (C7+neckF)/2            #首原点
    C_asis(:,1,k)   = (R_asis(:,1,k)+L_asis(:,1,k))/2
    uH2(:,1,k)      = R_asis(:,1,k)-C_asis(:,1,k)
    uH1(:,1,k)      = Sacral(:,1,k)-C_asis(:,1,k)
    uH3(:,1,k)      = cross(uH1(:,1,k),uH2(:,1,k))
    R_hip_JC(:,1,k) = C_asis(:,1,k)+0.64*uH2(:,1,k)+0.44*uH1(:,1,k)-0.68*uH3(:,1,k)
    L_hip_JC(:,1,k) = C_asis(:,1,k)-0.64*uH2(:,1,k)+0.44*uH1(:,1,k)-0.68*uH3(:,1,k)
    R_knee_JC       = (R_knee_out+R_knee_in)/2
    L_knee_JC       = (L_knee_out+L_knee_in)/2
    R_ankle_JC      = (R_ankle_out+R_ankle_in)/2
    L_ankle_JC      = (L_ankle_out+L_ankle_in)/2


Hip=(R_hip_JC+L_hip_JC)/2
#絶対座標系基底ベクトル*************************************************************
abs_x=zeros([3,1,analysis_frame])
abs_y=zeros([3,1,analysis_frame])
abs_z=zeros([3,1,analysis_frame])
for k=1:analysis_frame
    abs_x(1,1,k)=1
    abs_y(2,1,k)=1
    abs_z(3,1,k)=1
end
#腰回転中心算出*******************************************************************
#相対座標(腰回転中心算出用)************************************************************
    C_ill = (R_ill+L_ill)/2           #上前腸骨稜
for k=1:analysis_frame
    ur = R_asis-(R_ill+L_ill)/2
    ul = L_asis-(R_ill+L_ill)/2
#腰ジョイント用座標系xyz軸**********************************************************
    pel_z_axis(:,1,k) = basisvector2(ur(:,1,k),ul(:,1,k))
    pel_x_axis(:,1,k) = basisvector1(R_asis(:,1,k)/2-L_asis(:,1,k)/2)
    pel_y_axis(:,1,k) = basisvector2(pel_z_axis(:,1,k),pel_x_axis(:,1,k))
    pelvis_z_axis(:,1,k) = basisvector2(R_asis(:,1,k)-Sacral(:,1,k),L_asis(:,1,k)-Sacral(:,1,k))
    pelvis_x_axis(:,1,k) = basisvector1(R_ill(:,1,k)-C_ill(:,1,k))
    pelvis_y_axis(:,1,k) = basisvector2(pelvis_z_axis(:,1,k),pelvis_x_axis(:,1,k))
end

for k=1:analysis_frame
    pelvis_length(k)=basislength1(C_ill(:,1,k)-C_asis(:,1,k))
    waist_JC(:,:,k) = C_ill(:,:,k)-pelvis_length(k)*pelvis_y_axis(:,:,k)-0.5*pelvis_length(k)*pelvis_z_axis(:,:,k)       #腰回転中心L4/L5
end

#相対座標(胸)***************************************************************
for k=1:analysis_frame
    thorax_z_axis(:,1,k) = basisvector1(cervical_JC(:,1,k)-Hip(:,1,k))
    temp_thorax_x_axis(:,1,k) = basisvector1(R_shoulder(:,1,k)-L_shoulder(:,1,k))
    thorax_y_axis(:,1,k) = basisvector2(thorax_z_axis(:,1,k),temp_thorax_x_axis(:,1,k))
    thorax_x_axis(:,1,k) = basisvector2(thorax_y_axis(:,1,k),thorax_z_axis(:,1,k))
end
#相対座標(頭)****************************************************************
for k=1:analysis_frame
    head_z_axis(:,1,k) = basisvector1(headT(:,1,k)-(headF(:,1,k)+headR(:,1,k))/2)
    temp_head_x_axis(:,1,k) = basisvector1(headD(:,1,k)-(headF(:,1,k)+headR(:,1,k))/2)
    head_y_axis(:,1,k) = basisvector2(temp_head_x_axis(:,1,k),head_z_axis(:,1,k))
    head_x_axis(:,1,k) = basisvector2(head_y_axis(:,1,k),head_z_axis(:,1,k))
end
#相対座標(首)*******************************************************************
for k=1:analysis_frame
    cervical_z_axis(:,1,k) = basisvector1(cervical_JC(:,1,k)-waist_JC(:,1,k))
    temp_cervical_y_axis(:,1,k) = basisvector1(neckF(:,1,k)-C7(:,1,k))
    cervical_x_axis(:,1,k) = basisvector2(temp_cervical_y_axis(:,1,k),cervical_z_axis(:,1,k))
    cervical_y_axis(:,1,k) = basisvector2(cervical_z_axis(:,1,k),cervical_x_axis(:,1,k))
end
#相対座標(胴)*******************************************************************
for k=1:analysis_frame
    torso_x_axis(:,1,k) = basisvector1(Body_R(:,1,k)-Body_L(:,1,k))
    torso_z_axis(:,1,k) = basisvector1(cervical_JC(:,1,k)-waist_JC(:,1,k))
    torso_y_axis(:,1,k) = basisvector2(torso_z_axis(:,1,k),torso_x_axis(:,1,k))
#    torso_y_axis(:,1,k) = basisvector2(cervical_JC(:,1,k)-waist_JC(:,1,k),torso_x_axis(:,1,k))
#    torso_z_axis(:,1,k) = basisvector2(torso_x_axis(:,1,k),torso_y_axis(:,1,k))
#相対座標(右大腿=右膝)********************************************************
#相対座標(右下腿=右足)********************************************************
    R_thigh_z_axis(:,1,k) = basisvector1(R_hip_JC(:,1,k)-R_knee_JC(:,1,k))
    R_thigh_y_axis(:,1,k) = basisvector2(R_thigh_z_axis(:,1,k),R_knee_out(:,1,k)-R_knee_JC(:,1,k))
    R_thigh_x_axis(:,1,k) = basisvector2(R_thigh_y_axis(:,1,k),R_thigh_z_axis(:,1,k))
    R_leg_z_axis(:,1,k) = basisvector1(R_knee_JC(:,1,k)-R_ankle_JC(:,1,k))
    R_leg_y_axis(:,1,k) = basisvector2(R_leg_z_axis(:,1,k),R_ankle_out(:,1,k)-R_ankle_JC(:,1,k))
    R_leg_x_axis(:,1,k) = basisvector2(R_leg_y_axis(:,1,k),R_leg_z_axis(:,1,k))
#相対座標(右足)********************************************************
    R_foot_y_axis(:,1,k) = basisvector1(R_toe(:,1,k)-R_heel(:,1,k))
    R_foot_x_axis(:,1,k) = basisvector2(R_foot_y_axis(:,1,k),(R_ankle_JC(:,1,k)-R_heel(:,1,k)))
    R_foot_z_axis(:,1,k) = basisvector2(R_foot_x_axis(:,1,k),R_foot_y_axis(:,1,k))
#相対座標(左大腿=左膝)********************************************************
#相対座標(左下腿=左足)********************************************************
    L_thigh_z_axis(:,1,k) = basisvector1(L_hip_JC(:,1,k)-L_knee_JC(:,1,k))
    L_thigh_y_axis(:,1,k) = basisvector2(L_thigh_z_axis(:,1,k),L_knee_JC(:,1,k)-L_knee_out(:,1,k))
    L_thigh_x_axis(:,1,k) = basisvector2(L_thigh_y_axis(:,1,k),L_thigh_z_axis(:,1,k))
    L_leg_z_axis(:,1,k) = basisvector1(L_knee_JC(:,1,k)-L_ankle_JC(:,1,k))
    L_leg_y_axis(:,1,k) = basisvector2(L_leg_z_axis(:,1,k),L_ankle_JC(:,1,k)-L_ankle_out(:,1,k))
    L_leg_x_axis(:,1,k) = basisvector2(L_leg_y_axis(:,1,k),L_leg_z_axis(:,1,k))

#相対座標(左足)********************************************************
    L_foot_y_axis(:,1,k) = basisvector1(L_toe(:,1,k)-L_heel(:,1,k))
    L_foot_x_axis(:,1,k) = basisvector2(L_foot_y_axis(:,1,k),(L_ankle_JC(:,1,k)-L_heel(:,1,k)))
    L_foot_z_axis(:,1,k) = basisvector2(L_foot_x_axis(:,1,k),L_foot_y_axis(:,1,k))
    
    
###############################################################################
#重心位置**********************************************************************
#for k=1:analysis_frame
    head_cog      = (17.9*cervical_JC + 82.1*headT)/100
#    head_cog     = (50*headF + 50*headR)/100
    torso_cog     = (50*C_ill + 50*cervical_JC)/100
    pelvis_cog    = (50*C_ill + 50*(R_hip_JC + L_hip_JC)/2)/100
    R_thigh_cog   = (52.5*R_hip_JC + 47.5*R_knee_JC)/100
    L_thigh_cog   = (52.5*L_hip_JC + 47.5*L_knee_JC)/100
    R_leg_cog     = (59.4*R_knee_JC + 40.6*R_ankle_JC)/100
    L_leg_cog     = (59.4*L_knee_JC + 40.6*L_ankle_JC)/100
    R_foot_cog    = R_heel + R_foot_y_axis * foot_length * 40.5/100
    L_foot_cog    = L_heel + L_foot_y_axis * foot_length * 40.5/100
#end
#重心速度**********************************************************************
#初期値を0とする
velo_head_cog(:,1,1)    =[000]
velo_torso_cog(:,1,1)   =[000]
velo_pelvis_cog(:,1,1)  =[000]
velo_R_thigh_cog(:,1,1) =[000]
velo_R_leg_cog(:,1,1)   =[000]
velo_R_foot_cog(:,1,1)  =[000]
velo_L_thigh_cog(:,1,1) =[000]
velo_L_leg_cog(:,1,1)   =[000]
velo_L_foot_cog(:,1,1)  =[000]
for k=2:analysis_frame
    velo_head_cog(:,1,k)    =(head_cog(:,1,k)   -head_cog(:,1,k-1))     *f_motion
    velo_torso_cog(:,1,k)   =(torso_cog(:,1,k)  -torso_cog(:,1,k-1))    *f_motion
    velo_pelvis_cog(:,1,k)  =(pelvis_cog(:,1,k) -pelvis_cog(:,1,k-1))   *f_motion
    velo_R_thigh_cog(:,1,k) =(R_thigh_cog(:,1,k)-R_thigh_cog(:,1,k-1))  *f_motion
    velo_R_leg_cog(:,1,k)   =(R_leg_cog(:,1,k)  -R_leg_cog(:,1,k-1))    *f_motion
    velo_R_foot_cog(:,1,k)  =(R_foot_cog(:,1,k) -R_foot_cog(:,1,k-1))   *f_motion
    velo_L_thigh_cog(:,1,k) =(L_thigh_cog(:,1,k)-L_thigh_cog(:,1,k-1))  *f_motion
    velo_L_leg_cog(:,1,k)   =(L_leg_cog(:,1,k)  -L_leg_cog(:,1,k-1))    *f_motion
    velo_L_foot_cog(:,1,k)  =(L_foot_cog(:,1,k) -L_foot_cog(:,1,k-1))   *f_motion    

#重心加速度***************************************************************
#初期値を0とする
accel_head_cog(:,1,1)    =[000]
accel_torso_cog(:,1,1)   =[000]
accel_pelvis_cog(:,1,1)  =[000]
accel_R_thigh_cog(:,1,1) =[000]
accel_R_leg_cog(:,1,1)   =[000]
accel_R_foot_cog(:,1,1)  =[000]
accel_L_thigh_cog(:,1,1) =[000]
accel_L_leg_cog(:,1,1)   =[000]
accel_L_foot_cog(:,1,1)  =[000]
for k=2:analysis_frame
    accel_head_cog(:,1,k)    =(velo_head_cog(:,1,k)   -velo_head_cog(:,1,k-1))    *f_motion
    accel_torso_cog(:,1,k)   =(velo_torso_cog(:,1,k)  -velo_torso_cog(:,1,k-1))   *f_motion
    accel_pelvis_cog(:,1,k)  =(velo_pelvis_cog(:,1,k) -velo_pelvis_cog(:,1,k-1))  *f_motion
    accel_R_thigh_cog(:,1,k) =(velo_R_thigh_cog(:,1,k)-velo_R_thigh_cog(:,1,k-1)) *f_motion
    accel_R_leg_cog(:,1,k)   =(velo_R_leg_cog(:,1,k)  -velo_R_leg_cog(:,1,k-1))   *f_motion
    accel_R_foot_cog(:,1,k)  =(velo_R_foot_cog(:,1,k) -velo_R_foot_cog(:,1,k-1))  *f_motion
    accel_L_thigh_cog(:,1,k) =(velo_L_thigh_cog(:,1,k)-velo_L_thigh_cog(:,1,k-1)) *f_motion
    accel_L_leg_cog(:,1,k)   =(velo_L_leg_cog(:,1,k)  -velo_L_leg_cog(:,1,k-1))   *f_motion
    accel_L_foot_cog(:,1,k)  =(velo_L_foot_cog(:,1,k) -velo_L_foot_cog(:,1,k-1))  *f_motion    
end
##################################################################################
#角速度ベクトル_絶対座標**********************************************************
##################################################################################
#座標変換のための行列を定義
head_A=zeros([3,3,analysis_frame])thorax_A=zeros([3,3,analysis_frame])
torso_A=zeros([3,3,analysis_frame])pelvis_A=zeros([3,3,analysis_frame])
R_thigh_A=zeros([3,3,analysis_frame])L_thigh_A=zeros([3,3,analysis_frame])
R_leg_A=zeros([3,3,analysis_frame])L_leg_A=zeros([3,3,analysis_frame])
R_foot_A=zeros([3,3,analysis_frame])L_foot_A=zeros([3,3,analysis_frame])
#座標変換行列(頭)****************************************************************
for k=1:analysis_frame
head_A(:,1,k)   =head_x_axis(:,1,k)    head_A(:,2,k)   =head_y_axis(:,1,k)    head_A(:,3,k)   =head_z_axis(:,1,k)
torso_A(:,1,k)  =torso_x_axis(:,1,k)   torso_A(:,2,k)  =torso_y_axis(:,1,k)   torso_A(:,3,k)  =torso_z_axis(:,1,k)
pelvis_A(:,1,k) =pelvis_x_axis(:,1,k)  pelvis_A(:,2,k) =pelvis_y_axis(:,1,k)  pelvis_A(:,3,k) =pelvis_z_axis(:,1,k)
thorax_A(:,1,k) =thorax_x_axis(:,1,k)  thorax_A(:,2,k) =thorax_y_axis(:,1,k)  thorax_A(:,3,k) =thorax_z_axis(:,1,k)
R_thigh_A(:,1,k)=R_thigh_x_axis(:,1,k) R_thigh_A(:,2,k)=R_thigh_y_axis(:,1,k) R_thigh_A(:,3,k)=R_thigh_z_axis(:,1,k)
R_leg_A(:,1,k)  =R_leg_x_axis(:,1,k)   R_leg_A(:,2,k)  =R_leg_y_axis(:,1,k)   R_leg_A(:,3,k)  =R_leg_z_axis(:,1,k)
R_foot_A(:,1,k) =R_foot_x_axis(:,1,k)  R_foot_A(:,2,k) =R_foot_y_axis(:,1,k)  R_foot_A(:,3,k) =R_foot_z_axis(:,1,k)
L_thigh_A(:,1,k)=L_thigh_x_axis(:,1,k) L_thigh_A(:,2,k)=L_thigh_y_axis(:,1,k) L_thigh_A(:,3,k)=L_thigh_z_axis(:,1,k)
L_leg_A(:,1,k)  =L_leg_x_axis(:,1,k)   L_leg_A(:,2,k)  =L_leg_y_axis(:,1,k)   L_leg_A(:,3,k)  =L_leg_z_axis(:,1,k)
L_foot_A(:,1,k) =L_foot_x_axis(:,1,k)  L_foot_A(:,2,k) =L_foot_y_axis(:,1,k)  L_foot_A(:,3,k) =L_foot_z_axis(:,1,k)
end

#グローバル座標での書く速度ベクトルの算出
#1.変換行列の微分値を求める
#2.変換行列の転置を掛けてひずみ対象行列を算出
#3.三次元の角速度ベクトルを取り出す
head_ST=zeros([3,3,analysis_frame])thorax_ST=zeros([3,3,analysis_frame])torso_ST=zeros([3,3,analysis_frame])
pelvis_ST=zeros([3,3,analysis_frame])R_thigh_ST=zeros([3,3,analysis_frame])R_leg_ST=zeros([3,3,analysis_frame])
R_foot_ST=zeros([3,3,analysis_frame])L_thigh_ST=zeros([3,3,analysis_frame])L_leg_ST=zeros([3,3,analysis_frame])
L_foot_ST=zeros([3,3,analysis_frame])
#座標系をR(phi,theta,psi)であるとして、pitchのthetaを求めたい
torso_theta_d   =rpy_pitch(torso_A)
R_thigh_theta_d =rpy_pitch(R_thigh_A)
R_leg_theta_d   =rpy_pitch(R_leg_A)
L_thigh_theta_d =rpy_pitch(L_thigh_A)
L_leg_theta_d   =rpy_pitch(L_leg_A)
tunk_theta_d    =rpy_pitch(thorax_A)
