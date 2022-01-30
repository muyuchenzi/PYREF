from urllib import request
import re
import pandas as pd


class Spider():
    target_url = r'https://www.huya.com/g/wzry'

    def __fetch_content(self):
        r = request.urlopen(url=Spider.target_url)
        html = r.read()
        x = str(html, encoding='utf-8')
        return x

    def __anlysis(self, html):
        pattern_name = '<i class="nick" title=".*">(.*)</i>'
        pattern_num = '<i class="js-num">(.*)万</i>'

        watch_name = re.findall(pattern_name, html)
        watch_number = re.findall(pattern_num, html)
        result = list(zip(watch_name, watch_number))
        return result

    def __output_file(self, result):
        result_dataframe = pd.DataFrame(result)
        # result_dataframe = pd.read_excel(r'E:\李震祥\temp\Review_Work\Day12\result\final.xlsx',
        #                                  index_col=0)
        xx = pd.DataFrame.sort_values(result_dataframe, by=[1], ascending=False)
        rename = pd.DataFrame.rename(xx, columns={0: '主播名', 1: '热度'})
        rename.to_excel(r'E:\李震祥\temp\Review_Work\Day12\result\final.xlsx', encoding='utf-8',
                        index=False)

    def go(self):
        html = self.__fetch_content()
        watch = self.__anlysis(html)
        self.__output_file(watch)


if __name__ == '__main__':
    spider = Spider()
    spider.go()
