import java.io.BufferedReader;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.ServletException;
 
import java.io.IOException;
 
import org.eclipsejetty.server.Server;
import org.eclipsejetty.server.Request;
import org.eclipsejetty.server.handler.AbstractHandler;

/** 
 Skeleton of a ContinuousIntegrationServer which acts as webhook
 See the Jetty documentation for API documentation of those classes.
*/
public class ContinuousIntegrationServer extends AbstractHandler
{
    public void handle(String target,
                       Request baseRequest,
                       HttpServletRequest request,
                       HttpServletResponse response) 
        throws IOException, ServletException
    {
        response.setContentType("text/html;charset=utf-8");
        response.setStatus(HttpServletResponse.SC_OK);
        baseRequest.setHandled(true);

        System.out.println(target);
        BufferedReader r = request.getReader();
        while (r.ready()) {
            System.out.println(r.readLine());
        }
        
        // here you do all the continuous integration tasks
        // for example
        // 1st clone your repository
        // 2nd compile the code

        response.getWriter().println("CI job done!");
    }
 
    // used to start the CI server in command line
    public static void main(String[] args) throws Exception
    {
        Server server = new Server(1234);
        server.setHandler(new ContinuousIntegrationServer()); 
        server.start();
        server.join();
    }
}
