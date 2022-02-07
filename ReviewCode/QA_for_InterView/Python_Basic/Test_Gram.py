def solution(num_heads,num_legs):
    sol='no solution'
    for chick_head in range(num_heads+1):
        rabit_head=num_heads-chick_head
        if 2*chick_head+4*rabit_head==num_legs:
            return chick_head,rabit_head

    return sol,sol
num_had=35
num_leg=94
solut=solution(num_had,num_leg)
print(solut)

