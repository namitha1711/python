def nth_day(bd1_str, bd2_str, n):
    bd1 = datetime.strptime(bd1_str, "%Y-%m-%d")
    bd2 = datetime.strptime(bd2_str, "%Y-%m-%d")
    if bd1 > bd2:
        bd1, bd2 = bd2, bd1
    # Solve (t - bd2) = n * (t - bd1)
    # ⇒ t = (n*bd1 - bd2) / (n - 1)
    delta = bd2 - bd1
    t = bd2 + delta / (n - 1)
    print(f"{n}× Day:", t.date())
