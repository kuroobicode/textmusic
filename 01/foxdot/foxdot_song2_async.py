
Clock.clear()

# controll #######################################################
Clock.bpm = 120
Scale.default = Scale.chromatic
Root.default = 0


p1 >> keys(
    [4,6,11,13,16,18,23,25]
    ,dur=[0.25]
    ,oct=4
    ,vibdepth=0.3 ,vib=0.01
    )

p2 >> blip(
    [4,6,11,13,15,16,18,23,25]
    ,dur=[0.25]
    ,oct=3
    ,sus=2
    ,vibdepth=0.3 ,vib=0.01
    ,amp=0.35
    )
    
p3 >> bass(
    [(11,16),[(11,16,18),(11,16,23)]]
    ,dur=[3.5]
    ,oct=6
    ,sus=6
    ,vibdepth=0.1 ,vib=0.01
    ,amp=0.25
    )

p4 >> bell(
    [23,22,18,13,11,6]
    ,dur=[0.25,0.25,0.25,0.25,0.25,0.25,4]
    ,oct=6
    ,vibdepth=0.2 ,vib=0.01
    ,amp=0.125
    )

p5 >> swell(
    [(11,6),(11,16),[(11,20),(16,23)]]
    ,dur=[1.25]
    ,amp=0.5
    ,vib=4, vibdepth=0.01
    ,oct=6
    ,sus=1.5
    ,chop=3, coarse=0)

p6 >> pasha(
    [-1,6,11,(4,1,11)]
    ,dur=[1,1,rest(0.5),1.5]
    ,vibdepth=0.3 ,vib=0.21
    ,amp=0.15
    ,sus=[0.25,2]
    ,oct=3
    )



Clock.clear()


print(Samples)
print(SynthDefs)


