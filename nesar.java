import java.util.Scanner;
import java.util.Random;
public class nesar {

    public static void main(String[] args) {
    System.out.println("Welcome, would you like to encrypt, decrypt or generate your password?");
    System.out.println("Press : \n1:Encryption\n2:Decryption\n3:Password generation");
    Scanner sn = new Scanner(System.in);
    int choice= sn.nextInt(); //Accepting the user's input.
    switch(choice)
    {
        case 1:System.out.println("Only lowercase and no numbers are allowed.");
            System.out.print("Enter your password: ");
                String msg = sn.next().toLowerCase();
                char[] password = msg.toCharArray();
                for(int i=0; i<password.length; i++){
                    switch(password[i]){
                    case 'a':
                        password[i] = '+';
                        break;
                    case 'b':
                        password[i] = '-';
                        break;
                    case 'c':
                        password[i] = '*';
                        break;
                    case 'd':
                        password[i] = '/';
                        break;
                    case 'e':
                        password[i] = '\'';
                        break;
                    case 'f':
                        password[i] = '\"';
                        break;
                    case 'g':
                        password[i] = ')';
                        break;
                    case 'h':
                        password[i] = '[';
                        break;
                    case 'i':
                        password[i] = '{';
                        break;
                    case 'j':
                        password[i] = ':';
                        break;
                    case 'k':
                        password[i] = '#';
                        break;
                    case 'l':
                        password[i] = '?';
                        break;
                    case 'm':
                        password[i] = '%';
                        break;
                    case 'n':
                        password[i] = '}';
                        break;
                    case 'o':
                        password[i] = '$';
                        break;
                    case 'p':
                        password[i] = '<';
                        break;
                    case 'q':
                        password[i] = '~';
                        break;
                    case 'r':
                        password[i] = ';';
                        break;
                    case 's':
                        password[i] = '&';
                        break;
                    case 't':
                        password[i] = '|';
                        break;
                    case 'u':
                        password[i] = '€';
                        break;
                    case 'v':
                        password[i] = '¥';
                        break;
                    case 'w':
                        password[i] = '(';
                        break;
                    case 'x':
                        password[i] = '¿';
                        break;
                    case 'y':
                        password[i] = '>';
                        break;
                    case 'z':
                        password[i] = ']';
                        break;
                        case ' ':
                            password[i] = ' ';
                            break;
                    default:
                        password[i] = ' ';
                } //Assignment of special characters for letters from a to z.
            }
                    System.out.println("YOUR ENCRYPTED PASSWORD IS: ");
                    System.out.println(password);
                    break;

        case 2: System.out.print("Enter your password: ");
                String message = sn.next();
                char[] passcode = message.toCharArray();
            for(int i=0; i<passcode.length; i++){
                switch(passcode[i]){
                    case '+':
                        passcode[i] = 'a';
                        break;
                    case '-':
                        passcode[i] = 'b';
                        break;
                    case '*':
                        passcode[i] = 'c';
                        break;
                    case '/':
                        passcode[i] = 'd';
                        break;
                    case '\'':
                        passcode[i] = 'e';
                        break;
                    case '\"':
                        passcode[i] = 'f';
                        break;
                    case ')':
                        passcode[i] = 'g';
                        break;
                    case '[':
                        passcode[i] = 'h';
                        break;
                    case '{':
                        passcode[i] = 'i';
                        break;
                    case ':':
                        passcode[i] = 'j';
                        break;
                    case '#':
                        passcode[i] = 'k';
                        break;
                    case '?':
                        passcode[i] = 'l';
                        break;
                    case '%':
                        passcode[i] = 'm';
                        break;
                    case '}':
                        passcode[i] = 'n';
                        break;
                    case '$':
                        passcode[i] = 'o';
                        break;
                    case '<':
                        passcode[i] = 'p';
                        break;
                    case '~':
                        passcode[i] = 'q';
                        break;
                    case ';':
                        passcode[i] = 'r';
                        break;
                    case '&':
                        passcode[i] = 's';
                        break;
                    case '|':
                        passcode[i] = 't';
                        break;
                    case '€':
                        passcode[i] = 'u';
                        break;
                    case '¥':
                        passcode[i] = 'v';
                        break;
                    case '(':
                        passcode[i] = 'w';
                        break;
                    case '¿':
                        passcode[i] = 'x';
                        break;
                    case '>':
                        passcode[i] = 'y';
                        break;
                    case ']':
                        passcode[i] = 'z';
                        break;
                    default:
                        passcode[i] = ' ';
                } //Reverting the letters from the special characters back to letters.
            }
            System.out.println("YOUR DECRYPTED PASSWORD IS: ");
            System.out.println(passcode);
            break;
        case 3:  System.out.print("Enter Password Length(6-50): ");
            int len = sn.nextInt();
            if(len>=6 && len<=50){
                char[] arr={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','@','$','&','%','!','?','*'};
                Random rand = new Random();
                int i=0;
                System.out.print("Your New Password: ");
                while(i != len){
                    int num = rand.nextInt(arr.length -1)+1;
                    System.out.print(arr[num]);
                    i++;
                }
            }else if(len<6){
                System.out.println("Too weak password!");
            }else{
                System.out.println("Length exceeded limit!");
            }
            break;
        default: System.out.println("Invalid Input");
                    System.exit(0);
    }

    }
}