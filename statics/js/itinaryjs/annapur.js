var coll = document.getElementsByClassName("collapsible");
            var i;

            for (i = 0; i < coll.length; i++) {
            coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var content = this.nextElementSibling;
                if (content.style.display === "block") {
                content.style.display = "none";
                } else {
                content.style.display = "block";
                }
            });
            }


            /* slider */

            var slideIndex = 1;
            showDivs(slideIndex);
            
            function plusDivs(n) {
              showDivs(slideIndex += n);
            }
            
            function showDivs(n) {
              var i;
              var x = document.getElementsByClassName("mySlides");
              if (n > x.length) {slideIndex = 1}
              if (n < 1) {slideIndex = x.length}
              for (i = 0; i < x.length; i++) {
                x[i].style.display = "none";  
              }
              x[slideIndex-1].style.display = "block";  
            }

class="jscolor" style="color:black">class="jsnumbercolor" style="color:red"> class="jskeywordcolor" style="color:mediumblue">var slideIndex = class="jsnumbercolor" style="color:red">0;
carousel();
            
class="jskeywordcolor" style="color:mediumblue">function carousel() {
  class="jsnumbercolor" style="color:red"> class="jskeywordcolor" style="color:mediumblue">var i;
  class="jskeywordcolor" style="color:mediumblue">var x = document.class="jspropertycolor" style="color:black">getElementsByClassName(class="jsstringcolor" style="color:brown">"mySlides");
  class="jskeywordcolor" style="color:mediumblue">for (i = class="jsnumbercolor" style="color:red">0; i < x.class="jspropertycolor" style="color:black">length; i++) {
class="jsnumbercolor" style="color:red">     x[i].class="jspropertycolor" style="color:black">style.class="jspropertycolor" style="color:black">display class="jsnumbercolor" style="color:red"> = class="jsstringcolor" style="color:brown">"none";
  }
  slideIndex++;
  class="jsnumbercolor" style="color:red"> class="jskeywordcolor" style="color:mediumblue">if (slideIndex > x.class="jspropertycolor" style="color:black">length) {slideIndex = class="jsnumbercolor" style="color:red">1}
  class="jsnumbercolor" style="color:red"> x[slideIndex-class="jsnumbercolor" style="color:red">1].class="jspropertycolor" style="color:black">style.class="jspropertycolor" style="color:black">display = class="jsstringcolor" style="color:brown">"block";
  setTimeout(carousel, class="jsnumbercolor" style="color:red"> class="jsnumbercolor" style="color:red">2000); class="commentcolor" style="color:green">// Change image every 2 seconds
}
class="jsnumbercolor" style="color:red">