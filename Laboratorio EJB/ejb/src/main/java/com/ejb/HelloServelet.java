package com.ejb;

import javax.ejb.EJB;
import javax.ejb.Stateless;

@WebServlet("/hello")
public class HelloServelet extends HttpServlet {

    @EJB
    HelloBean helloBean;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/plain");
        response.getWriter().write(helloBean.sayHello("usuario"));
    }
}
