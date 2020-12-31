print(SynthDefs)
Clock.clear()
d2.stop()

# controll #######################################################
Clock.bpm = 150
Scale.default = Scale.chromatic
Root.default = 0

p1 >> sinepad(
    [3,[2,0],-1,(0,7,2)]
    ,dur=[0.5,1.5,rest(0.75),1.25]
    ,vibdepth=0.3 ,vib=0.01
    )

p2 >> pasha(
    [0,5,-1,(0,10,5)]
    ,dur=[1,1,rest(0.5),1.5]
    ,vibdepth=0.3 ,vib=0.21
    ,amp=0.25
    ,sus=[0.25,2]
    )

p3.stop()

p3 >> bass(
    [0,7,0,0,0,3,15] #12 15
    ,dur=[0.5,0.5,0.5,0.5,0.25,0.125,1.125]
    ,amp=2
    ,sus=[0.25,0.25,0.25,0.25,0.25,0.5,2]
    #,rate=0.5
    ,vibdepth=0.01,vib=0.2
    ,oct=4)

print(SynthDefs)

p4 >> gong(
    [7,3,5,0]
    ,dur=[1,2,3]
    ,amp=5
    ,vib=2, vibdepth=0.01
    ,oct=4
    ,sus=2.5
    ,coarse=1
    ,glide=[1,-1]
    ,fmod=2)

p4.stop()

p5 >> saw(
    [(3,8,12)]
    ,dur=[1,1,rest(0.5),1.5]
    ,vibdepth=0.3 ,vib=0.21
    ,amp=1
    ,sus=[0.25,2]
    )

p5.stop()

# 2nd phrase
p6 >> blip(
    [3,5,10,0]
    ,dur=[1,0.5,1,2,3]
    ,amp=3
    ,vib=2, vibdepth=0.01
    ,oct=4
    ,sus=2.5
    ,coarse=0)

p6.stop()

p7 >> klank(
    P([0, 7, 12, 4, (3, 8 ,10)]).every(3,"reverse")
    ,dur=[rest(1),linvar([0, 1], 2)]
    ,sus=[1, 2.5]    
    ,oct=5
    ,amp=0.5
    )

p7.stop()

p8 >> twang(
    P([0, 7, 12, 4, (3, 8 ,10)]).every(2,"reverse")
    ,dur=[rest(1),linvar([0, 1], 2)]
    ,sus=[1, 2.5]    
    ,oct=5
    ,chop=2
    ,amp=0.25
    )

p8.stop()

# 3rd 
p9 >> arpy(
    P([3, 8, 12, 17, [(8, 12 ,17) , (8, 12 ,20)]])
    ,dur=[([0, 1], 2)]
    ,sus=[1, 3.5]  
    ,oct=5
    )

p9.stop()

p1 >> soft(
    P([3, 8, 12, 17, [(8, 12 ,17) , (8, 12 ,20)]])
    ,dur=[[1.5, 1], 2]
    ,sus=[2, 3.5]  
    ,oct=6
    ,echo=2
    ,amp=0.75
    )

p2 >> pads(
    P([(8, 12 ,17) , (8, 12 ,20)])
    ,dur=P[[1.5, 1.75], 2]
    ,sus=[1.5, 1.5]
    ,oct=5
    ,amp=0.25
    )

p2.stop()

p3 >> jbass(
    P[8, 12 ,15, P[17,14]]
    ,dur=[3,3,3,1.5,1.5]
    ,sus=3
    ,release=2
    ,oct=5
    )


bd >> play(["x x "] ,amp=[6])

hh >> play("---(-o)[- --]" ,rate=0.75 ,amp=0.5)


d1 >> play("x[--]x[--]x", sample=d1.degree.map({"x":2, "-~":5}))

bd.stop()

hh.stop()

d1.stop()

Clock.clear()
