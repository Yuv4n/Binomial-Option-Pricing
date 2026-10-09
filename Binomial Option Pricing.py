import math

def option(T, S, K, r, sigma, n, q, type, option): 
    #  T expiration time
    #  S stock price
    #  K strike price
    #  r interest rate
    #  sigma volatility of the stock price
    #  n number of intervals
    #  q dividend yield
    #  European or American
    #  Call, Put

    #   Defining Variables
    deltaT = T/n 
    up = math.exp(sigma * math.sqrt(deltaT))
    p0 = (up * math.exp((r-q)*deltaT) - 1 ) / (up**2 - 1)
    p1 = 1 - p0
    fList = []
    f = 0

    #   Calculating Final Price Values
    for i in range(n+1):
        if option == "Call":
            fList.append(S * up**(n - 2*i) - K)
        elif option == "Put":
            fList.append(K - S * up**(n - 2*i))
        if fList[i] < 0:
            fList[i] = 0

    #   Counting Prices
    if type == "European":
        for m in range(n+1):
            f += math.exp(-r * T)*((math.factorial(n)//(math.factorial(m)*math.factorial(n-m))) * (p0**(n-m)) * (p1**(m)) * fList[m])
        return f

    elif type == "American":
        priceTree = []
        for i in range(n+1):
            priceTree.append([])
            for j in range(i+1):
                priceTree[i].append(S * up**(i - 2*j))
                if priceTree[i][j] < 0:
                    priceTree[i][j] = 0

        fList = [fList]
        for i in range(1, n+1):
            fList.append([])
            for j in range(n+1-i):
                fList[i].append(math.exp(-r * deltaT)*((p0 * fList[i-1][j]) + (p1 * fList[i-1][j+1])))
                #  Early Exercise 
                if option == "Call":
                    fList[i][j] = max(fList[i][j], priceTree[n-i][j] - K)
                elif option == "Put":
                    fList[i][j] = max(fList[i][j], K - priceTree[n-i][j])

        return fList[n][0]

#   Ex 13.3
print(option(0.75, 31, 30, 0.05, 0.3, 3, 0, "American", "Call")) #Exp Result 4.49

#   Ex 13.10
print(option(2, 50, 52, 0.05, 0.3, 2, 0, "American", "Put")) #Exp Result 7.43

#   Ex 13.1
print(option(0.5, 810, 800, 0.05, 0.2, 2, 0.02, "European", "Call")) #Exp Result 53.39

#   Ex 13.7
print(option(2, 50, 52, 0.05, 0.2, 2, 0.02, "European", "Put")) #Exp Result 4.66

#   For real world application we could create a CSV file with data in the required form, and read the file 
#   with pandas to create a database with the relevant data in the correct form, and pass as arguments into 
#   function with a simple function, to handle large quantities of data at once.
