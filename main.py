import subprocess
f = open("wifiSifreler.txt","w")
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}\n".format(i, results[0]))
            f.write("{:<30}|  {:<}\n".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}\n".format(i, ""))
            f.write("{:<30}|  {:<}\n".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
        f.write("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
        f.close()