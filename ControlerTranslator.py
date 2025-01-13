output = [0.0,0.0]
def clamp(n, min_value, max_value):
    if n < min_value:
        return min_value
    elif n > max_value:
        return max_value
    return n
#contols_turn =[0.0,0.0]
#contols_acc =[0.0,0.0]

#contols_acc_1D =0.0
def get(contols_turn,contols_acc_1D,speed=100):
    TmotorA = 0
    TmotorB =0
    power = (contols_acc_1D%1.001)
    if contols_turn[0] <-0.1:
        print("left",power)
        TmotorA = (-abs(contols_turn[0])+1)
        TmotorA = clamp(TmotorA,0.0,1.0)
        TmotorB= 1.0
    elif contols_turn[0] >0.1:
        print("right",power)
        TmotorB = (-abs(contols_turn[0])+1.0)
        TmotorB = clamp(TmotorB,0.0,1.0)
        TmotorA =1.0
    else:
        TmotorA = 1.0
        TmotorB = 1.0

    return [TmotorA*power*speed,TmotorB*power*speed]
