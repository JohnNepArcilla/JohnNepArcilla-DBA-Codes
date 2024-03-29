# John Nep Arcilla  06/06/2023
ans = 'Y'
while ans == 'Y':
    # Inputs of all data 
    newlyHiredMales = int(input("Enter the number of newly hired males:"))
    newlyHiredFemales = int(input("Enter the number of newly hired females:"))
    permanentPositionMales = int(input("Enter the number of permanent position males:"))
    permanentPositionFemales = int(input("Enter the number of permanent position females:"))
    resignedMales = int(input("Enter the number of resigned males:"))
    resignedFemales = int(input("Enter the number of resigned females:"))
    print("""=================
    Thank you for the Information
    =================
    Here is the Summary!!!\n""")

    # Computation of all data in total
    totalNewlyHired = newlyHiredFemales + newlyHiredMales
    totalPermanentEmployee = permanentPositionFemales + permanentPositionMales
    totalResigned = resignedFemales + resignedMales
    totalEmployee = totalNewlyHired + totalPermanentEmployee

    # Get the percentage of male and female
    percentageMaleNH = newlyHiredMales/totalNewlyHired*100
    percentageFemaleNH = newlyHiredFemales/totalNewlyHired*100
    percentageMalePE = permanentPositionMales/totalPermanentEmployee*100
    percentageFemalePE = permanentPositionFemales/totalPermanentEmployee*100
    percentageMaleRE = resignedMales/totalResigned*100
    percentageFemaleRE = resignedFemales/totalResigned*100
    percentageTotalEmployeeM = newlyHiredMales+permanentPositionMales/totalEmployee*100
    percentageTotalEmployeeF = newlyHiredFemales+permanentPositionFemales/totalEmployee*100

    # Outputs of all data with rounded numbers
    print("Number of Hired Employee = ", totalNewlyHired)
    print("Male = ", round(percentageMaleNH, 2),"%")
    print("Female = ", round(percentageFemaleNH, 2),"%\n")
    print("Number of Permanent Employee = ", totalPermanentEmployee)
    print("Male = ", round(percentageMalePE, 2),"%")
    print("Female = ", round(percentageFemalePE, 2),"%\n")
    print("Number of Resigned Employee = ", totalResigned)
    print("Male = ", round(percentageMaleRE, 2),"%")
    print("Female = ", round(percentageFemaleRE, 2),"%\n")
    print("Total Number of Employee = ", totalEmployee)
    print("Male = ", round(percentageTotalEmployeeM, 2),"%")
    print("Female = ", round(percentageTotalEmployeeF, 2),"%\n")

    ans = input("Do you want to try again? Y or N :")
    if ans == 'N':
        print("All Set!")
    else:
        ans = 'Y'