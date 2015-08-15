/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package pdftotext;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

/**
 *
 * @author Shivani
 */
public class PdfToText {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        String folderPath = "C:\\Users\\Shivani\\Desktop\\toTXT\\VirtualReality";
        String folderName = "CompSciVirRel";
        File folder = new File(folderPath);
        File[] listOfFiles = folder.listFiles();

    for (int i = 0; i < listOfFiles.length; i++) {
      if (listOfFiles[i].isFile()) {
       // System.out.println("File " + listOfFiles[i].getName());
      } else if (listOfFiles[i].isDirectory()) {
       // System.out.println("Directory " + listOfFiles[i].getName());
      }
    }
        
//        
        
        for(int i = 0; i < listOfFiles.length; i++)
        {
            
            if (listOfFiles[i].isFile())
            {
                System.out.println("File " + listOfFiles[i].getName());
                PDFManager pdfManager = new PDFManager();
                String filePath = folderPath + "\\" + listOfFiles[i].getName();
                pdfManager.setFilePath(filePath);
                String content = pdfManager.ToText();
                String fname = folderName + "_" + listOfFiles[i].getName();
                String newfname = fname.replace(" ", "_");
                String newFile = folderPath + "\\TEXT\\" + newfname + ".txt";
                File file = new File(newFile);
 
	// if file doesnt exists, then create it
                if (!file.exists()) 
                {
                    file.createNewFile();
		}
 
                FileWriter fw = new FileWriter(file.getAbsoluteFile());
                BufferedWriter bw = new BufferedWriter(fw);
                bw.write(content);
                bw.close();
                
            }
        }
      
    }
}
