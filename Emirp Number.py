another_no = "yes"
while another_no == "yes" or another_no == "y" or another_no == "Y" or another_no == "Yes" or another_no == "YES":
    x=int(input("Enter a number: "))
    if x>=2:
        y = x
        rem = 0
        sum = 0
        count1 = 0
        count2 = 0

        while (y > 0):
            rem = y % 10
            sum = sum * 10 + rem
            y = y // 10

        for i in range(2, x):
            if x % i == 0:
                count1 += 1

        for i in range(2, sum):
            if sum % i == 0:
                count2 += 1

        if count1 == 0 & count2 == 0:
            print(x, 'is an emirp number')
        else:
            print(x, 'is not an emirp number')

        another_no = input("Choose another number?...(y/n) : ")

    elif x<=1:
        print(x,"is not an emirp number")

    else:
        print("Wrong input")
        another_no=input("Choose another number?...(y/n) : ")
