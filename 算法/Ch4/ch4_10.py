def gcd_i(m,n):
    while(n!=0):
        print(f'gcd({m},{n})',end='')
        r = m % n
        m = n
        n = r
    return m    

print(gcd_i(20,14))
