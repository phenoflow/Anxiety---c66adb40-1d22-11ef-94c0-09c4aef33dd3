# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Carolyn A Chew-Graham, Nav Kapur, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"E201600","system":"readv2"},{"code":"E292.00","system":"readv2"},{"code":"E283z00","system":"readv2"},{"code":"E29y.00","system":"readv2"},{"code":"E29yz00","system":"readv2"},{"code":"Eu45y00","system":"readv2"},{"code":"E2...00","system":"readv2"},{"code":"Eu41300","system":"readv2"},{"code":"E29y500","system":"readv2"},{"code":"E283.00","system":"readv2"},{"code":"Eu41.00","system":"readv2"},{"code":"E20y.00","system":"readv2"},{"code":"E20yz00","system":"readv2"},{"code":"Eu44y00","system":"readv2"},{"code":"E292z00","system":"readv2"},{"code":"Eu46.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-xother---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-xother---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-xother---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
