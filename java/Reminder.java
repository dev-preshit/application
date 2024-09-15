import java.util.*;
import java.text.SimpleDateFormat;  


class CurrentDateTime extends Thread{  
    String CT,show,CTDisplay;
    HashMap<Integer, String> pre = new HashMap<>();




    public void run() {
        while (true) {
            getSystemTime();
            checkTime();
            try {
                Thread.sleep(1000);
                System.out.println("\033c");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }




    void getSystemTime() {  
        SimpleDateFormat formatterDisplay = new SimpleDateFormat("HH:mm:ss");  
        Date dateDisplay = new Date(); 
        CTDisplay =  formatterDisplay.format(dateDisplay);
        System.out.print(CTDisplay);
    }
    
    

    void addReminder() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the time (HH:mm): ");
        String timeInput = scanner.nextLine();
        System.out.print("Enter the reminder: ");
        String reminder = scanner.nextLine();



        timeInput = timeInput.replace(":", "");
        timeInput = timeInput.replaceFirst("^0+(?!$)", "");
        Integer timeInt = Integer.parseInt(timeInput);



        pre.put(timeInt, reminder);
    }

    void removeReminder() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the time (HH:mm): ");
        String timeInput = scanner.nextLine();


        timeInput = timeInput.replace(":", "");
        timeInput = timeInput.replaceFirst("^0+(?!$)", "");
        Integer timeInt = Integer.parseInt(timeInput);


        pre.remove(timeInt);
    }



    

    void checkTime(){

        SimpleDateFormat formatter = new SimpleDateFormat("HH:mm");  
        Date date = new Date(); 
        CT =  formatter.format(date);


        pre.put(500, "Wake Up!!");
        pre.put(510, "Drink Water!!");
        pre.put(700, "Drink Water!!");
        pre.put(900, "Drink Water!!");
        pre.put(1100, "Drink Water!!");
        pre.put(1300, "Drink Water!!");
        pre.put(1500, "Drink Water!!");
        pre.put(1700, "Drink Water!!");
        pre.put(1900, "Drink Water!!");
        pre.put(2100, "Drink Water!!");
        pre.put(2110, "Bed Time!!");




        CT = CT.replace(":", "");
        CT= CT.replaceFirst("^0+(?!$)", "");
        Integer intCT = Integer.parseInt(CT);


        

        if(pre.containsKey(intCT)){
            System.out.println("===|Reminder:"+ pre.get(intCT)+"|===");
        }
    }


    void showReminders() {
        if (pre.isEmpty()) {
            System.out.println("No reminders set.");
        } else {
            System.out.println("Reminders:");
            for (Map.Entry<Integer, String> entry : pre.entrySet()) {
                System.out.println("Time: " + entry.getKey() + ", Reminder: " + entry.getValue());
            }
        }
    }

}


class Reminder{
    static void line(int n,int bol)
    {
        if(bol==0)
       {
            for(int i=0;i<n;i++)
           {
              System.out.print("=");
           }
       }
       else if(bol==1)
       {
           System.out.println();
          for(int i=0;i<n;i++)
           {
               System.out.print("=");
           }
       }
       else if(bol==2)
       {
          for(int i=0;i<n;i++)
           {
               System.out.print("=");
           }
          System.out.println();
       }
       
    }
    public static void main(String[] args) {
        CurrentDateTime c=new CurrentDateTime();
        Scanner choose = new Scanner(System.in);
        boolean exit = false;
        while (!exit) {
            line(24, 1);
            System.out.print("|REMINDER|");
            line(24, 2);
            line(12, 1);
            System.out.print("|0.Do nothing|");
            line(6, 0);
            System.out.print("|1.Add Reminder|");
            line(10, 2);
            line(9, 1);
            System.out.print("|2.Show Reminder|");
            line(6, 0);
            System.out.print("|3.Delete Reminder|");
            line(7, 2);
            line(16, 1);
            System.out.print("|press any key too Exit|");
            line(18, 2);
            System.out.print("Enter your choice: ");
            int ch = choose.nextInt();

            switch (ch) {
                case 0:
                    c.start();
                    break;
                case 1:
                    c.addReminder();
                    break;
                case 2:
                    c.showReminders();
                    break;
                case 3:
                    c.removeReminder();
                    break;
                default:
                    exit = true;
                    break;
            }
        }
    }
}  

    

