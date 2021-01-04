#reculsive_sum
def sum_test():
    num = input("수를 입력하세요")
    print("입력한 수",num)
    print(my_sum(int(num)))


def my_sum(n): # 이 함수의 목표는 0~n 까지의 합을 구하는 것이다
    if n == 0: # n=0 이면 합은 0이다
        return 0
    return n + my_sum(n-1) # n이 0보다 크면 0에서 n 까지의 합은, n-1까지의 합에 n을 더한 것이다.
sum_test()


#recursive_ractenglar
import turtle as t

def my_spiral(sp_len):
    if sp_len <= 5:
        return
    t.forward(sp_len)
    t.right(90)
    my_spiral(sp_len - 5)

t.speed(0)
my_spiral(200)
t.hideturtle()
t.done()


#factorial
def my_factorial(n):
    if n == 0:
        return 1
    return n * my_factorial(n-1)

def factorial_test():
    num = input("팩토리얼 수를 입력하세요")
    print("팩토리얼의 수",num)
    print(my_factorial(int(num)))

factorial_test()


#hanoi
def my_hanoi(n, from_post, to_post, aux_post):

    if n==1: #원반 한 개를 옮기다면 (옮기는 원반이 한 개 라면)

        print(from_post, "---->", to_post) # 바로 옮기면 됨
        
        return


    #원반 n-1개를 보조기둥으로 이동한다 (즉 to_post를 보조 기둥으로 한다)

    
    my_hanoi(n-1, from_post, aux_post, to_post)
        
    #가장 큰 원반을 목적지로 이동한다    
    
    print(from_post,"---->",to_post)
    
    
    #보조 기둥에 있는 원반 n-1개를 목적지로 이동한다(즉, from_post를 보조 기둥으로 한다)
    my_hanoi(n-1,aux_post, to_post, from_post)
    

def hanoi_test():
    num = input("원반의 개수를 입력하세요")
    print("원반의 개수",num)
    my_hanoi(int(num),1,3,2)

hanoi_test()
