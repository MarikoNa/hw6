#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import cgi


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(u"""
            <html>
             <head>
              <title>パタトクカシーー</title>
             </head>
             <body>
              <form action="/result" method="post">
                <input type = "text" name="text1"><br>
                <input type = "text" name="text2"><br>
                <input type = "submit" name = "submit">
              </form>
              </body>
             </html>
            """)

class ResultPage(webapp2.RequestHandler):
    def post(self):
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        text1 = self.request.get("text1")
        text2 = self.request.get("text2")
        result = "".join(i+j for i, j in zip(text1,text2))
        self.response.out.write(u"""
              <html>
              <head>
              <title>パタトクカシーー</title>
             </head>
        """)
        if(result != ""):
            self.response.out.write(u"""
               <body>
            　<font size="10">%s</font>
		 <hr>
                </body>
             """%result)
        self.response.out.write(u"""
             <body>
              <form action="/result" method="post">
                <input type = "text" name="text1"><br>
                <input type = "text" name="text2"><br>
                <input type = "submit" name = "submit">
              </form>
              </body>
             </html>
            """)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ("/result", ResultPage)
], debug=True)
