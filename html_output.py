
class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def colletc_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        fout = open('out.html', 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" %data['url'])
            fout.write("<td>%s</td>" %data['title'])
            fout.write("<td><nobr>%s</nobr></td>" %data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()