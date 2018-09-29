
public class StringUtil {
    public static String concat(String a, String b) {
        return a + b;
    }

    public static String remove_duplicate(String a) {
        for (int i = 0; i < a.length(); i++) {
            if (a.substring(i).equals(a.substring(i + 1))) {
                a = a.substring(i + 1, a.size() - 1);
                i -= 1;
            }
        }

        return a;
    }

    public static String duplicate(String a, int round) {
        String result = "";
        for (int i = 0; i < round; i++) {
            result += a;
        }

        return result;
    }

    public static int find(String a, char c) {
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == (c)) {
                return i;
            }
        }

        return 0;
    }
}