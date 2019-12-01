def publishError(startStr, endStr, *args):
    print(startStr)
    for elem in args :
        (x,y) = elem
    print(endStr)

publishError("[Start]" , "[End]" , ("Hello", "Hi") ,("Hello2", "Hi2"))
#
# class BankAccount:
#     def great(self,name):
#         print("Welcome",name)
#
#
# def main():
#         m_acc = BankAccount()
#         m_acc.great()
#
#         m_acc2 = BankAccount()
#         m_acc2.great()
#
# main()
