# controll #######################################################
Clock.bpm = 120
Scale.default = Scale.major


# ptn1 #######################################################
b1 >> bass([(0,7,0),3], dur=[0.25,0.5, 2], amp=((0.5,0.1,0.7), 1), pan=(-1,1))

b1.stop()

mp1note = [7, 2, 5, 3, 2, 0] 
mp1dur = [1.5, 3, 1.5, 0.5, 0.5, 2] 
mp1amp = [2, 1, 2, 3, 1, 2] 
mp1oct = [3, 2, 3, 4]
mp1scale = Scale.major

m1 >> pluck(mp1note, dur=mp1dur ,amp=mp1amp ,oct=mp1oct ,scale=mp1scale)


m2 >> keys(
    [16,16,12,16,12,9,7,5,4].reverse()
    ,dur=[1,0.5,0.5,0.75,0.75,0.75,0.5,1,3]
    ,scale=Scale.chromatic
    )

m2.stop()

m3 >> sawbass(
   # [16,16,12,16,12,9,7,5,4]
    [16,16,12,16,12,16,17,19]
   # ,dur=[1,0.5,0.5,0.75,0.75,0.75,0.5,1,3]
    ,dur=[1,0.5,0.5,0.75,0.75,0.75,1.5,1,2.25]
    ,scale=Scale.chromatic
    )

m4 >> spark(
    [4,5,0,4,5,7]
    ,dur=[0.25 ,rest(0.75) ,0.25, 0.25 ,rest(0.75) , rest(0.5) ,0.25, rest(0.5),1]
    ,scale=Scale.chromatic
    ,oct=6
    ,amp=1
    ,room=0.5
    )
    
# ptn2 #######################################################
b1 >> bass([(0,7,(0,3)), (2,2,4,5)]
    , dur=[(0.5,1,0.5,1.5),(2,0.5,0.5,0.5)]
    , amp=((0.5,0.1,0.7), 0.5)
    , pan=(-1,1)
    , sus= 0.5)


#mp2note = [(7, 12, 16) ,(9 ,12 ,19) ,((7 ,10 ,17),0) ,(7, 12, 16)]
mp2note = [(0, 2, 4), (3, 5, 7)] 
mp2dur = [rest(0.5) ,3.5 ,1 ,rest(1) ,3 , 6] 
mp2scale = Scale.chromatic

m2 >> varsaw(mp2note, dur=mp2dur ,scale=mp2scale ,amp=1)

m3 >> blip(
    [4,7,16,7 ,4,7,16,7 ,4,7,16,7 ,4,7,16,7
     ,3,7,14,7 ,3,7,14,7 ,3,7,14,7 ,3,7,14,7]
    ,dur=[0.25]
    ,scale=Scale.chromatic
    ,amp=0.75
    ,oct=6
    ,echo=1.75)

m3.stop()

## riff
m9 >> bass(
    [7 ,0 ,[5 ,7 ,12] ,7 ,10 ,12]
    ,dur=[1 ,1 ,rest(0.25) ,[0.25 ,0.25 ,0.25] ,rest(1.25) ,0.25 ,0.25]
    ,scale=Scale.chromatic
    )

m9.stop()

# shuffle()
    ,dur=[1 ,1 ,rest(0.25) ,[0.25 ,0.25 ,0.25] ,rest(1.25) ,0.25 ,0.25]
# dur [1]


# Rhythm #######################################################
d1 >> play("x-o-{m--}" ,amp=2.5)

d1.stop()

d2 >> play("-v n-y v o" ,amp=2)


d3 >> play("li ~ [--xx]" ,amp=3)

d2.stop()



d1.stop()

print(SynthDefs)
print(Samples)



print(Scale.names())

b2.stop()

d1.stop()

d2.stop()


Clock.clear()


