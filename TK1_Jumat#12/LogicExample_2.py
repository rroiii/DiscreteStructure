#-p^(q^r)
for p in (True, False):
    for q in (True, False):
        for r in (True, False):
            print("%10s %10s %10s %10s" % ( p, q, r, not p and (q or r)))