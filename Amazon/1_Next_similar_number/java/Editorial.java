package project.programmer.Amazon.Next_similar_numbers;

public class Editorial {
    public void swap(char[] arr, int i,int j){
        char temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    public String solve(String A) {
        char[] a=A.toCharArray();
        int n=a.length;
        int i;
        for(i=n-1;i>0;i--){
            if(a[i]>a[i-1]) break;
        }
        
        if(i==0) return "-1";
        else{
            int x=a[i-1], min=i;
            for(int j=i+1;j<n;j++){
                if(a[j]>x && a[j]<a[min]){
                    min=j;
            }}
            swap(a,i-1,min);
            Arrays.sort(a,i,n);
            String res="";
            for(int k=0;k<n;k++){
                res+=a[k];
            }
            // System.out.println(res);
            return res;
            
        }
        // return "-1";
    }
}
