from time import time
start = time()
# 49/98  ok
# 30 / 50 not ok
# 30 / 31 not ok
# 31 / 30 not ok

for denomitor in range(11, 100):
    for numerator in range(denomitor-1, 10, -1):
        denomitor = str(denomitor)
        numerator = str(numerator)
        if "0" in denomitor or "0" in numerator:
            continue
        if numerator[0] == denomitor[0]:
            common = numerator[0]
            numerator_new = numerator.replace(common, "", 1)
            denomitor_new = denomitor.replace(common, "", 1)
            if int(numerator) / int(denomitor) == int(numerator_new) / int(denomitor_new):
                print(f"{numerator} / {denomitor}")
        elif numerator[0] == denomitor[1]:
            common = numerator[0]
            numerator_new = numerator.replace(common, "", 1)
            denomitor_new = denomitor.replace(common, "", 1)
            if int(numerator) / int(denomitor) == int(numerator_new) / int(denomitor_new):
                print(f"{numerator} / {denomitor}")
        elif numerator[1] == denomitor[0]:
            common = numerator[1]
            numerator_new = numerator.replace(common, "", 1)
            denomitor_new = denomitor.replace(common, "", 1)
            if int(numerator) / int(denomitor) == int(numerator_new) / int(denomitor_new):
                print(f"{numerator} / {denomitor}")
        elif numerator[1] == denomitor[1]:
            common = numerator[1]
            numerator_new = numerator.replace(common, "", 1)
            denomitor_new = denomitor.replace(common, "", 1)
            if int(numerator) / int(denomitor) == int(numerator_new) / int(denomitor_new):
                print(f"{numerator} / {denomitor}")
        else:
            continue

print("Time: {:.2f}".format(time() - start))