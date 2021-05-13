# opens data in txt files generated from CK-12
def readTxt(input,seperate):
    import csv
    with open(input) as test:
        storage = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        answer_key = []
        for lines in test:
            '''if 'Multiple' in lines:
                pass'''
            if 'True/False' in lines:
                break
            if '.' in lines:
                if 'www.' in lines:
                    pass
                elif lines == '':
                    pass
                else:
                    try:
                        if int(lines[1]) in nums:
                            storage.append(lines[4:-1])
                    except:
                        storage.append(lines[3:-1])
        counter = 0
        found_answers = 0
        for answers in test:
            if 'answer key' in answers.lower():
                found_answers = 1
                answer_key.append(answers[-2:-1])
            else:
                if found_answers == 1:
                    if answers[-1:] == '\n':
                        answer_key.append(answers[-2:-1])
                    else:
                        answer_key.append(answers[-1:])
        print(answer_key[1:])
        ans_num = 1
        to_write = []
        # For testing the list function. Comment out when done testing.
        for items in storage:
            if counter != 4:
                to_write.append(items)
                counter += 1
            else:
                to_write.append(items)
                to_write.append(answer_key[ans_num])
                print(to_write)
                if seperate == 1:
                    with open(input[:-4] + '.csv', 'a', newline='', encoding='utf-8-sig') as f:
                        w = csv.writer(f)
                        w.writerow(to_write)
                else:
                    with open('compiled.csv', 'a', newline='', encoding='utf-8-sig') as f:
                        w = csv.writer(f)
                        w.writerow(to_write)
                to_write = []
                ans_num += 1
                counter = 0