import re
with open("day4.txt") as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

    #print lines

passports = []
passport = {}
for i in range(len(lines)):
    if lines[i] != "\n":
        fields = lines[i].split()
        #print fields
        for j in range(len(fields)):
            k,v = fields[j].split(":")
            passport[k] = v
    else:
        passports.append(passport)
        passport = {}

passports.append(passport)

valid = 0
for i in range(len(passports)):
    p = passports[i]
    if "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p:
        hcl_re = re.compile('^#[a-f0-9]{6}$')
        pid_re = re.compile('^[0-9]{9}$')
        if (
                1920 <= int(p['byr']) <= 2002 and
                2010 <= int(p['iyr']) <= 2020 and
                2020 <= int(p['eyr']) <= 2030 and
                (
                        (p['hgt'][-2:] == 'in' and
                         59 <= int(p['hgt'][0:-2]) <= 76
                        ) or
                        (p['hgt'][-2:] == 'cm' and
                         150 <= int(p['hgt'][0:-2]) <= 193
                        )
                ) and
                hcl_re.match(p['hcl']) and
                p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
                pid_re.match(p['pid'])
        ):
            valid +=1

print valid