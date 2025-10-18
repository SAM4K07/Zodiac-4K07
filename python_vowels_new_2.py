tome = 0
oldwords = []

aconsto = []
bconsto = []
cconsto = []
dconsto = []
econsto = []
fconsto = []
gconsto = []
hconsto = []
iconsto = []
jconsto = []
kconsto = []
lconsto = []
mconsto = []
nconsto = []
oconsto = []
pconsto = []
qconsto = []
rconsto = []
sconsto = []
tconsto = []
uconsto = []
vconsto = []
wconsto = []
xconsto = []
yconsto = []

while True:
    tome += 1
    print("this is your", tome, "time")

    word = input("enter your word: ")
    if word == "exit":
        break

    oldwords.append(word)

    count = 0
    acount = 0
    ecount = 0
    icount = 0
    ocount = 0
    ucount = 0

    bcount = 0
    ccount = 0
    dcount = 0
    fcount = 0
    gcount = 0
    hcount = 0
    jcount = 0
    kcount = 0
    lcount = 0
    mcount = 0
    ncount = 0
    pcount = 0
    qcount = 0
    rcount = 0
    scount = 0
    tcount = 0
    vcount = 0
    wcount = 0
    xcount = 0
    ycount = 0
    zcount = 0

    conscount = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for letter in word:
        if letter in vowels:
            count += 1
            if letter == 'a':
                acount += 1
            if letter == 'e':
                ecount += 1
            if letter == 'i':
                icount += 1
            if letter == 'o':
                ocount += 1
            if letter == 'u':
                ucount += 1
        else:
            conscount += 1
            if letter == 'b':
                bcount += 1
            if letter == 'c':
                ccount += 1
            if letter == 'd':
                dcount += 1
            if letter == 'f':
                fcount += 1
            if letter == 'g':
                gcount += 1
            if letter == 'h':
                hcount += 1
            if letter == 'j':
                jcount += 1
            if letter == 'k':
                kcount += 1
            if letter == 'l':
                lcount += 1
            if letter == 'm':
                mcount += 1
            if letter == 'n':
                ncount += 1
            if letter == 'p':
                pcount += 1
            if letter == 'q':
                qcount += 1
            if letter == 'r':
                rcount += 1
            if letter == 's':
                scount += 1
            if letter == 't':
                tcount += 1
            if letter == 'v':
                vcount += 1
            if letter == 'w':
                wcount += 1
            if letter == 'x':
                xcount += 1
            if letter == 'y':
                ycount += 1
            if letter == 'z':
                zcount += 1

    print("number of vowels in your word is:", count)
    print("number of consonants in your word is:", conscount)
    print("total letters altogether:", count + conscount)

    print("a:", acount, "e:", ecount, "i:", icount, "o:", ocount, "u:", ucount)
    print("b:", bcount, "c:", ccount, "d:", dcount, "f:", fcount, "g:", gcount,
          "h:", hcount, "j:", jcount, "k:", kcount, "l:", lcount, "m:", mcount,
          "n:", ncount, "p:", pcount, "q:", qcount, "r:", rcount, "s:", scount,
          "t:", tcount, "v:", vcount, "w:", wcount, "x:", xcount, "y:", ycount)

    if acount > 0:
        aconsto.append(acount)
    if bcount > 0:
        bconsto.append(bcount)
    if ccount > 0:
        cconsto.append(ccount)
    if dcount > 0:
        dconsto.append(dcount)
    if ecount > 0:
        econsto.append(ecount)
    if fcount > 0:
        fconsto.append(fcount)
    if gcount > 0:
        gconsto.append(gcount)
    if hcount > 0:
        hconsto.append(hcount)
    if icount > 0:
        iconsto.append(icount)
    if jcount > 0:
        jconsto.append(jcount)
    if kcount > 0:
        kconsto.append(kcount)
    if lcount > 0:
        lconsto.append(lcount)
    if mcount > 0:
        mconsto.append(mcount)
    if ncount > 0:
        nconsto.append(ncount)
    if ocount > 0:
        oconsto.append(ocount)
    if pcount > 0:
        pconsto.append(pcount)
    if qcount > 0:
        qconsto.append(qcount)
    if rcount > 0:
        rconsto.append(rcount)
    if scount > 0:
        sconsto.append(scount)
    if tcount > 0:
        tconsto.append(tcount)
    if ucount > 0:
        uconsto.append(ucount)
    if vcount > 0:
        vconsto.append(vcount)
    if wcount > 0:
        wconsto.append(wcount)
    if xcount > 0:
        xconsto.append(xcount)
    if ycount > 0:
        yconsto.append(ycount)

    print(" ")

print("You have typed a total of", tome, "times")
print("All words entered:", oldwords)
print(
   
    "Sum of a:", sum(aconsto), "/",
    "Sum of b:", sum(bconsto), "/",
    "Sum of c:", sum(cconsto), "/",
    "Sum of d:", sum(dconsto), "/",
    "Sum of e:", sum(econsto), "/",
    "Sum of f:", sum(fconsto), "/",
    "Sum of g:", sum(gconsto), "/",
    "Sum of h:", sum(hconsto), "/",
    "Sum of i:", sum(iconsto), "/",
    "Sum of j:", sum(jconsto), "/",
    "Sum of k:", sum(kconsto), "/",
    "Sum of l:", sum(lconsto), "/",
    "Sum of m:", sum(mconsto), "/",
    "Sum of n:", sum(nconsto), "/",
    "Sum of o:", sum(oconsto), "/",
    "Sum of p:", sum(pconsto), "/",
    "Sum of q:", sum(qconsto), "/",
    "Sum of r:", sum(rconsto), "/",
    "Sum of s:", sum(sconsto), "/",
    "Sum of t:", sum(tconsto), "/",
    "Sum of u:", sum(uconsto), "/",
    "Sum of v:", sum(vconsto), "/",
    "Sum of w:", sum(wconsto), "/",
    "Sum of x:", sum(xconsto), "/",
    "Sum of y:", sum(yconsto), "/"
)
