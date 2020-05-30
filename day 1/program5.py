pl1 = int(input("Enter player 1 score: "))
pl2 = int(input("Enter player 2 score: "))
pl3 = int(input("Enter player 3 score: "))

st1 = pl1*100/60
st2 = pl2*100/60
st3 = pl3*100/60

print("strike rate of player 1: ",st1)
print("strike rate of player 2: ",st2)
print("strike rate of player 3: ",st3)

print("score of player 1 if played 60 ball more: ",(pl1*2))
print("score of player 2 if played 60 ball more: ",(pl2*2))
print("score of player 3 if played 60 ball more: ",(pl3*2))

print("maximum sixes of player 1: ",(pl1//6))
print("maximum sixes of player 2: ",(pl2//6))
print("maximum sixes of player 3: ",(pl3//6))
