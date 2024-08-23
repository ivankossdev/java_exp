package ClassUser;

public class UserStaticField {
    public String name;
    public String e_mail;
    private int id;
    static int counter;


    /*начало блока инициализатора*/
    static{
        counter = 2;
    }
    /*конец блока инициализатора*/

    public UserStaticField(String name){
        this.id = counter++;
        this.name = name;
    }
    public int getUserID(){
        return id;
    }
}
