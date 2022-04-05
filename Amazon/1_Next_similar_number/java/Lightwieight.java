package project.programmer.Amazon;

public class Lightwieight {
    public String solve(String A) {
        int n = A.length();
        char[] arr = new char[n];
        for (int i=0;i<n;i++){
            arr[i] = A.charAt(i);
        }
        int i=0;
        for( i = n-1 ; i >0;i--){
            if(arr[i-1] < arr[i])
            break;
        }
       // System.out.println(i);
        if(i==0)
        return "-1";
        int smallest = i;
        for (int j = i ; j<n;j++){
            if(arr[j] > arr[i-1] && arr[j] <= arr[smallest])
             smallest = j;
        }
        char temp = arr[i-1];
        arr[i-1] = arr[smallest];
        arr[smallest] = temp;
    
        Arrays.sort(arr,i,n);
       
        
        String result = new String(arr);
        return result;
        
    }
}
