import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Tester {
	public static void main(String[] args) throws InterruptedException {
		System.setProperty("webdriver.gecko.driver","path\\geckodriver-v0.26.0-win64\\geckodriver.exe");
		WebDriver driver = new FirefoxDriver();
		driver.get("https://www.saucedemo.com/index.html");
		WebDriverWait wait = new WebDriverWait(driver, 3);
    
	    	//**********************DOM ELEMENTS**************************
        WebElement DOM_Username = driver.findElement(By.xpath("//*[@id=\"user-name\"]"));
        WebElement DOM_Password = driver.findElement(By.xpath("//*[@id=\"password\"]"));
        WebElement DOM_Submit = driver.findElement(By.xpath("//*[@id=\"login_button_container\"]/div/form/input[3]"));
        
        //**********************TEST CASES********************************
        String[] usernames = {"standard_userX","standard_userY","standard_user","standard_user"};
        String[] passwords = {"standard_userX","secret_sauce","secret_sauceZ","secret_sauce"};
        for(int i=0;i<4;i++)
        {
        	
        		//*******Clearing WebElements**************
        		DOM_Password.clear();
        		DOM_Username.clear();
        		
    	        DOM_Username.sendKeys(usernames[i]);
    	        DOM_Password.sendKeys(passwords[i]);
    	        DOM_Submit.click();
    	        TimeUnit.SECONDS.sleep(2);	        
    	        
    	        //****************TEST-CASE******************
    	        String Actual_Url="https://www.saucedemo.com/inventory.html";
    	        String Expected_Url= driver.getCurrentUrl();
    	        if(Actual_Url.equalsIgnoreCase(Expected_Url))
    	        {
    	            System.out.println("Test passed");
    	        }
    	        else
    	        {
    	            System.out.println("Test failed");
    	        }
    	        //***********Introducing Delay to Show Various Test Cases - 3Seconds *****************
    	        TimeUnit.SECONDS.sleep(3);
			
	        }
	}
}
