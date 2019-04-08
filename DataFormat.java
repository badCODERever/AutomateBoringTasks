import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.DataFormatter;
import java.io.File;
import java.io.FileInputStream;

public class DataFormat 
{
    public static void main(String[] args) throws Exception
    {
        File file=new File(" ");//File Name .xlx formate
        FileInputStream fis=new FileInputStream(file);
        HSSFWorkbook wb=new HSSFWorkbook(fis);
        HSSFSheet sheet = wb.getSheetAt(0);
        int rownum=sheet.getLastRowNum();
        DataFormatter dataFormatter=new DataFormatter();
        for(int i=1;i<=rownum;i++)
        {
	        String data=dataFormatter.formatCellValue(sheet.getRow(i).getCell(0));//get all the first cell values
            System.out.println(data);//printing first cell values 
        }
	}
}
