print('''
                                       ____                                         
                              .-"    `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____        
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. where do you want to go?")
cross_road = input("       Type 'left' or 'right'    \n")

if cross_road == "right":
    print("Fall into hole. Game over.")

elif cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    first_choice = input("    Type 'wait' to wait for a boat of 'swim' to swim across.\n")

    if first_choice == "swim": 
        print("Attacked by trout. Game over.")

    elif first_choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        second_choice = input("One red, one yellow and one blue. Which colour do you choose?\n")

        if second_choice == "red":
            print("Burned by fire. Game over.")

        elif second_choice == "blue":
            print("Eaten by beasts. Game over.")

        elif second_choice == "yellow":
            print("You win!")

        else:
            print("Game over.")

    else:
        print("Attacked by trout. Game over.")

else:
    print("Fall into hole. Game over.")