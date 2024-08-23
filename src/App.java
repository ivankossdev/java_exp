import ClassUser.User;
import ClassUser.UserStaticField;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, Led!");
        String str = "my string";
        long lng = 15000555L;
        System.out.printf("Example string %s \nLong intger %d\n", str, lng);
        String res = func(2, 10);

        System.out.printf("Func result %s\n", res);
        String[] arrayString = new String[3];

        setArrayString(arrayString);
        getArrayString(arrayString);

        User u1 = new User("u1", "u1@u.ru");
        System.out.printf("Create user %s\ne-mail %s\n", u1.name, u1.e_mail);
        System.out.printf("User id %d\n", u1.getId());

        User u2 = new User("u2");
        System.out.printf("Create user %s\n", u2.name);

        UserStaticField usf1 = new UserStaticField("usf1");
        System.out.printf("Create user %s id = %d\n", usf1.name, usf1.getUserID());

        UserStaticField usf2 = new UserStaticField("usf2");
        System.out.printf("Create user %s id = %d\n", usf2.name, usf2.getUserID());
    }

    static String func(int a, int b){
        int r = (a + b) * 2;
        String result = String.format("%d + %d = %d", a, b, r);
        
        return result;
    }

    static void setArrayString(String[] a){
        for(int i = 0; i < 3; i++){
            a[i] = String.format("string_%d", i);
        }
    }

    static void getArrayString(String[] a){
        for (String myString : a) {
            System.out.println(myString);
        }
    }
}
