package ClassUser;

public class User {
    public String name;
    public String e_mail;
    int id;

    public User(String _name){
        name = _name;
        id = 10;
        e_mail = "No e-mail";
    }

    public User(String _name, String _e_mail){
        name = _name;
        id = 10;
        e_mail = _e_mail;
    }

    public int getId(){
        return id;
    }
}
