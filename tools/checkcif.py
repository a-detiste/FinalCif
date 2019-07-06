#  ----------------------------------------------------------------------------
#  "THE BEER-WARE LICENSE" (Revision 42):
#  daniel.kratzert@ac.uni-freiburg.de> wrote this file.  As long as you retain
#  this notice you can do whatever you want with this stuff. If we meet some day,
#  and you think this stuff is worth it, you can buy me a beer in return.
#  Dr. Daniel Kratzert
#  ----------------------------------------------------------------------------
import json
from pathlib import Path
from urllib import request

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebPage(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.load(QUrl("https://checkcif.iucr.org/"))
        self.loadFinished.connect(self._on_load_finished)

    def _on_load_finished(self):
        print("Finished Loading")
        self.page().toHtml(self.Callable)

    def Callable(self, html_str):
        self.html = html_str
        self.page().runJavaScript(
            """
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState === 4 && this.status === 200) {
                    document.getElementsByTagName("body").innerHTML =
                    this.responseText;
                }
            };
            xhttp.open("POST", "//checkcif.iucr.org/cgi-bin/checkcif_hkl.pl", true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.send("filecif=='/Users/daniel/GitHub/FinalCif/test-data/DK_zucker2_0m.cif'");
            
            """
        )
        # self.page().runJavaScript(
        #    "document.getElementsByName('filecif')[0].value = '/Users/daniel/GitHub/FinalCif/test-data/DK_zucker2_0m.cif'")
        # self.page().runJavaScript("document.getElementsByName('UPLOAD')[0].click()")
        # self.page().runJavaScript(
        #    """
        #    let fileInput = document.querySelector('input');
        #    fileInput.addEventListener("input", ev => {
        #        ev.preventDefault();
        #        fileInput.files = e.dataTransfer.files;
        #    }
        #    );
        #    //var x = document.createElement("INPUT");
        #    //x.setAttribute("type", "file");
        #    """
        # )


def get_checkcif():
    file_name = '/Users/daniel/GitHub/FinalCif/test-data/DK_zucker2_0m.cif'
    out_file = "cifreport.html"

    params = {
        "file"      : Path(file_name).read_text(encoding='ascii', errors='ignore'),
        "runtype"   : "symmonly",
        "referer"   : "checkcif_server",
        "outputtype": 'HTML',
        'validtype' : 'checkcif_only'
    }
    print('Report request sent')
    url = 'http://checkcif.iucr.org/cgi-bin/checkcif_hkl.pl'

    response = request.urlopen(url, data=bytes(json.dumps(params), encoding='ascii'), timeout=150)
    Path(out_file).write_bytes(response.read())


if __name__ == "__main__":
    get_checkcif()
    # app = QApplication(sys.argv)
    # web = WebPage()
    # web.show()
    # sys.exit(app.exec_())
