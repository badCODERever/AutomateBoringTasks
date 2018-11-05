while True:
        number=int(input())
        def collatz(number):
                if number%2==0:
                        return number//2
                else:
                        return 3*number+1
        ans=collatz(number)
        print(ans)
        if ans==1:
                break
        else:
                continue
