older_y, older_m = input('Please type year and month of first person: ').split()
younger_y, younger_m = input('Please type year and month of second person: ').split()
older_y = int(older_y)
older_m = int(older_m)
younger_y = int(younger_y)
younger_m = int(younger_m)
older = 'I'
older_total_month = older_y * 12 + older_m
younger_total_month = younger_y * 12 + younger_m
if (older_total_month) > (younger_total_month):
	older_y, younger_y = younger_y, older_y
	older_m, younger_m = younger_m, older_m
	older_total_month, younger_total_month = younger_total_month, older_total_month
	older = 'II'
dif_total_month = younger_total_month - older_total_month
print()
dif_y = dif_total_month // 12
dif_m = dif_total_month - dif_y * 12
result_string = older
if dif_y > 0:
	result_string += ', ' + str(dif_y) + (' years' if dif_y > 1 else ' year')
if dif_m > 0:
	result_string += ', ' + str(dif_m) + (' months' if dif_m > 1 else ' month')
print(result_string)