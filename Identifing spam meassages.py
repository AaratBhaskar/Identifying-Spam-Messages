spam=("Make a lot of money","make a lot of money","Buy now""buy now","Subcribe this","subcribe this""Click this""click this")

a=(input("Enter message or comment to indentify spam:"))
if(a in spam):
    print("This is a spam comment/message")
else:
    print("This is no spam comment")