print("welke dag is het vandaag?")
antw = input()

if antw.lower() == 'maandag':
    print("op naar school")
elif antw.lower() == 'dinsdag':
    print("pak je spullen, op naar school.")
elif antw.lower() == 'woensdag':
    print("kom op, snel zijn.")
elif antw.lower() == 'donderdag':
    print("bijna weekend.")
elif antw.lower() == 'vrijdag':
    print("laatste dag, blijf sterk!!")
else:
    print("het is weekend")
