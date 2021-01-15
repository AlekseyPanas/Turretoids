import subprocess

try:
    process = subprocess.run(['pip', 'install', '--upgrade', '--user', 'pip'],
                             stdout=subprocess.PIPE,
                             universal_newlines=True,
                             shell=True)
    print(process.stdout)

    libs = ["pygame"]
    for lib in libs:
        process = subprocess.run(['pip', 'install', lib],
                                 stdout=subprocess.PIPE,
                                 universal_newlines=True,
                                 shell=True)
        print(process.stdout)
except Exception as e:
    print("An error has occurred:")
    print(e)

    print()
    input("press enter to continue")

print("The script has finished. Press enter to close this window")

input()