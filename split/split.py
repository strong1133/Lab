test_string = 'https://dthumb-phinf.pstatic.net/?src=https://sports-phinf.pstatic.net/team/wfootball/default/19.png&amp;type=f25_25&amp;refresh=1 '
a = test_string.split('=')
b = a[1].split('&')

print (b[0])
