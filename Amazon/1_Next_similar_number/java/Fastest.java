package project.programmer.Amazon;

public class Fastest {
    static void swap(char[] a, int i, int j){
        char temp= a[i];
        a[i]= a[j];
        a[j]= temp;
    }
    public String solve(String A) {
        char[] arr= A.toCharArray();
        int n= arr.length;
        int i;
        for(i=n-1; i>0; i--){
            if(arr[i]> arr[i-1])
            break;

        }
        if(i==0)
        return "-1";
        else{
            int x=arr[i-1], min=i;
            for (int j = i + 1; j < n; j++)
            {
                if (arr[j] > x && arr[j] < arr[min])
                {
                    min = j;
                }
            }
            swap(arr, i-1, min);
            Arrays.sort(arr, i, n);
            String res= String.valueOf(arr);
            return res;
        }
    }
}
