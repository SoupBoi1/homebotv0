output = [0.0,0.0]
def clamp(n, min_value, max_value):
    return max(min_value, min(n, max_value))

#contols_turn =[0.0,0.0]
#contols_acc =[0.0,0.0]

#contols_acc_1D =0.0
def get(contols_turn,contols_acc_1D,speed=100):
    TmotorA = 0
    TmotorB =0
    power = (contols_acc_1D+1.0)/2.0

    if contols_turn[0]*(int(contols_acc_1D)) <0:
        TmotorA = -contols_turn[0]+1
        TmotorA = clamp(TmotorB,0,1)
        TmotorB= 1.0
    elif contols_turn[0]*int(contols_acc_1D) >0:
        TmotorB = contols_turn[0]+1
        TmotorB = clamp(TmotorB,0,1)
        TmotorA =1.0
    else:
        TmotorA = 1.0
        TmotorB = 1.0

    return [TmotorA*power,TmotorB*power]
