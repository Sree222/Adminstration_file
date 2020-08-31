#College Administration project
import csv


def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer= csv.writer(csv_file)

        if  csv_file.tell()==0:
            writer.writerow(["NAME", "AGE", "DOB", "CONTACT_NUM", "E-MAIL_ID"])
            
        writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    student_num=1
    
    


    while (condition):
        student_info=input("ENTER STUDENT INFORMATION IN SPECIFIED FORMAT FOR STUDENT #{}(NAME AGE DOB CONTACT_NUM E-MAIL_ID: ".format(student_num))

    
        student_info_list=student_info.split(' ')
        print("Entered information: \nNAME: {}\nAGE: {}\nDOB: {}\nCONTACT_NUM: {}\nE-MAIL_ID: {}"
              .format( student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
        
        check=input("IS THE ENTERED INFORMATION CORRECT?(yes/no) : ")

   


        if check=="yes":
            write_into_csv(student_info_list)
            
            condition_statement=input("ENTER '(yes/no)' FOR ADDING NEXT STUDENTS INFORMATION :")
            if (condition_statement =="yes"):
                condition=True
                student_num=student_num+1
            elif (condition_statement =="no"):
                condition=False
        elif check=="no":
            print("please enter correct information")
            

       
