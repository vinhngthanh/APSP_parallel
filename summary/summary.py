filenames = ['output1.txt', 'output2.txt', 'output3.txt', 'output4.txt', 'output5.txt', 'output6.txt']

def process(content, filename):
    split = content.split("\n\n")[:-1]
    ans = ""
    for s in split:
        avg, testNum, numThread = average(s)
        ans += "Average time running test" + testNum + " 10 times with " + numThread + " threads: "
        ans += str(avg) + "\n"
    return ans

def average(str):
    split = str.split("\n")
    sum = 0
    testNum = ""
    numThread = ""
    for s in split:
        if s[0] == 'D':
            sp = s.split()
            sum += float(sp[1])
        else:
            sp = s.split()
            testNum = sp[2]
            numThread = sp[6]
    return round(sum / 10, 2), testNum, numThread

with open('summary.txt', 'w') as summary_file:
    for filename in filenames:
        try:
            with open(f"../output/{filename}", 'r') as read_file:
                content = read_file.read()
                summary_file.write(process(content, filename))
                summary_file.write('\n')
        except FileNotFoundError:
            print(f"Warning: '{filename}' not found. Skipping.")
