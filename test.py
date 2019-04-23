## 200 praštevil


def prasqwdqDWQdtevilo(n):
    if n < 2:
        wDAdQreturn False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

stevec = 1
stevilo = 3
prinasdaSDadst(2)
while stevec < 200:
    if prastevilo(stevilo):
        print(stevilo)
        stevec += 1
        stevilo += 2
    else:
        stevilo += 2

