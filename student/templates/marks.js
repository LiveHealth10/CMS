var data1='{{ lis1 }}';
                        var d=JSON.parse(data1.replace(/&quot;/g,'"'));
                        if(d.length<7){
                        for (i = 0; i < d.length; i++) {
                          document.write("<tr><td>" + d[i].date + "</td>");  
                          document.write("<td>" + d[i].status + "</td></tr>");  
                             
                        }
                        }
                        else{
                          for (i = 0; i < 6; i++) {
                          document.write("<tr><td>" + d[i].date + "</td>");  
                          document.write("<td>" + d[i].status + "</td></tr>");  
                             
                        }
                        }
                         