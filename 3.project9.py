def double_day(bd1_str, bd2_str):
    bd1 = datetime.strptime(bd1_str, "%Y-%m-%d")
    bd2 = datetime.strptime(bd2_str, "%Y-%m-%d")
    if bd1 > bd2:
        bd1, bd2 = bd2, bd1
    # Solve t such that t - bd2 = 2*(t - bd1) → t = 2*bd1 - bd2
    t = bd2 + (bd2 - bd1)
    print("Double Day:", t.date())
