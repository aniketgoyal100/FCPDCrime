#FCPD Crime Data Analysis Tool
#Created By: Aniket Goyal 
#Contact: goyalaniket105@gmail.com
#Last Revision: December 25, 2024

#Note: This file contains global code at the bottom which tests the various methods for correct implementation. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


class FCPDCrime(list):
    def __init__(self, name = "Fairfax County Police Crime Report"):
        super().__init__()
        self.name = name

    def printCrimes(self, searchkey = "all", zipcode = "all", locale = "all"):
        report = []

        for x in self: 
            Found = True 
            if searchkey != "all" and searchkey.upper() not in x[2].upper():
                Found = False 
            if str(zipcode) != "all" and str(zipcode) != str(x[-1]):
                Found = False 
            if locale != "all" and locale.upper() != x[-3].upper():
                Found = False 
            if Found:
                report.append(x)

        for lines in report:
            print(lines)
            


    def countByCrime(self, select = "all"):
        report = [] #report used for sorting 
        crimes = [] #used to hold numbers and codes 
        final_report = []
        total = len(self)
        for x in self:
            if select == "all":
                crime_code = x[1]
                description = x[2]
                found = False
                for y in crimes:
                    if y[0] == crime_code:
                        y[1] += 1
                        found = True
                        break
                if not found:
                    crimes.append([crime_code, 1, description])
            elif str(select) == str(x[-1]):
                crime_code = x[1]
                description = x[2]
                found = False
                for y in crimes:
                    if y[0] == crime_code:
                        y[1] += 1
                        found = True
                        break
                if not found:
                    crimes.append([crime_code, 1, description])
        for crime_code, count, description in crimes:
            frequencynum = (count / total) * 100
            report.append([count, crime_code, f"{frequencynum:.2f}%", description])
            report.sort(reverse = True)
        for x in report:
            final_report.append([x[1], x[0], x[2], x[3]])
        return final_report

    def zipCodeList(self, zip_code):
        report = []
        
        for x in self :
            if x[-1] == str(zip_code):
                report.append(x)
        if not report:
            return "Error"
        return report
        

    def countByZip(self):
        report = []
        final_report = []
        counts = []
        total = len(self)

        for x in self: 
            zip_code = x[-1]
            found = False
            for y in counts:
                if y[0] == zip_code:
                    y[1] += 1
                    found = True
                    break
            if not found:
                    counts.append([zip_code, 1])
        for zip_code, count in counts: 
            frequencynum = (count / total) * 100
            report.append([count, zip_code, f"{frequencynum:.2f}%"])
            report.sort(reverse = True)
        for x in report:
            final_report.append([x[1], x[0], x[2]])
        return final_report
            

    def load(self, file):
        f = open(file, "r")
        for line in f:
            row = []
            for item in line.strip().split(","):
                new_line = item.strip()
                row.append(new_line)
            self.append(row)
        return len(self)
    

#------------------------------------------------------

FC = FCPDCrime(name = "TestRun"" FCPD Crime Reporting Analytics Class")
input("\nCheck that file has been loaded correctly: (Should print 964) ")                
L = FC.load(file = "/Users/aniketg/Desktop/IT/Python /CrimeReports.csv")
print(L)
input("\nCheck ""zipCodeList"" method (Checking ZIPCODE 22079): ")
check =FC.zipCodeList(22079)
for x in check:
    print(x)
input("\n""countByZip"" check: ")
check = FC.countByZip()
for x in check:
    print(x)
input("\n""Check ""CountByCrimes"" method (select = all): ")
check = FC.countByCrime()
for x in check:
    print(x)
input("\n""Check ""CountByCrimes"" method (select = zipcode(22079)): ")
check = FC.countByCrime(22079)
for x in check:
    print(x)
input("\nprintCrimes check (default ALL values)")
check = FC.printCrimes()
print("\n\n""All crimes printed out succesfully")
input("\nprintCrimes check (zipcode = 22079)")
check = FC.printCrimes(zipcode = 22079)
input("\nprintCrimes check (searchkey = assault)")
check = FC.printCrimes(searchkey = "assault")
input("\nprintCrimes check (locale = Fairfax)")
check = FC.printCrimes(locale = "Fairfax")
input("\nprintCrimes check (locale = Fairfax, searchkey = shoplifting)")
check = FC.printCrimes(locale = "Fairfax", searchkey = "shoplifting")

