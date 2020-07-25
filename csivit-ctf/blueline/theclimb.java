public class Main
{
    int kmatrix[][];
    int tmatrix[];
    int rmatrix[];
 
    public void div(String temp, int size)
    {
        while (temp.length() > size)
        {
            String substr = temp.substring(0, size);
            temp = temp.substring(size, temp.length());
            perf(substr);
        }
        if (temp.length() == size)
            perf(temp);
        else if (temp.length() < size)
        {
            for (int i = temp.length(); i < size; i++)
                temp = temp + 'x';
            perf(temp);
        }
    }
 
    public void perf(String text)
    {
        textconv(text);
        multiply(text.length());
        res(text.length());
    }
 
    // Stores the key of length n into rootnxrootn matrix kmat with elements filling rows first.
    public void keyconv(String key, int len)
    {
        kmatrix = new int[len][len];
        int c = 0;
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                kmatrix[i][j] = ((int) key.charAt(c)) - 97;
                c++;
            }
        }
    }
 
    // Stores text in a matrix
    public void textconv(String text)
    {
        tmatrix = new int[text.length()];
        for (int i = 0; i < text.length(); i++)
        {
            tmatrix[i] = ((int) text.charAt(i)) - 97;
        }
    }
 
    // kmat is a n*n matrix and tmat is a n*1 matrix. This does mat. mult. and stores in rmat
    public void multiply(int len)
    {
        rmatrix = new int[len];
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                rmatrix[i] += kmatrix[i][j] * tmatrix[j];
            }
            rmatrix[i] %= 26;
        }
    }

    // Converts and prints rmat
    public void res(int len)
    {
        String res = "";
        for (int i = 0; i < len; i++)
        {
            res += (char) (rmatrix[i] + 97);
        }
        System.out.print(res);
    }
 
 
    public static void main(String[] args)
    {
        Main obj = new Main();
        System.out.println("Enter the plain text: ");
        String text = ""; // Unknown flag.
        System.out.println(text);
        System.out.println("Enter the key: ");
        String key = "gybnqkurp";
        // g y b
        // n q k
        // u r p
        System.out.println(key);
        double root = Math.sqrt(key.length());
        // key length must be perfect square
        if (root != (long) root)
            System.out.println("Invalid key length.");
        else
        {
            int size = (int) root;   
            System.out.println("Encrypted text = ");
            obj.keyconv(key, size);
            obj.div(text, size);
        }
    }
}