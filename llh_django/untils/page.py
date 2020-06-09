# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/6/9 17:59
# Tool ：PyCharm
# 分页代码封装
from django.utils.safestring import mark_safe

class Page:
    def __init__(self, current_page, data_count, page_num=11, per_page_count=10):
        self.current_page = current_page
        self.data_count = data_count
        self.page_num = page_num
        self.per_page_count = per_page_count

    @property
    def start(self):
        return (self.current_page-1)*self.per_page_count

    @property
    def end(self):
        return self.current_page*self.per_page_count

    @property
    def total_count(self):
        total_count, y = divmod(self.data_count, self.per_page_count)
        if y:
             total_count += 1
        return total_count

    @property
    def page_str(self, base_url):
        page_list = []
        if self.total_count < self.page_num:
            start_index = 1
            end_index = self.total_count + 1
        else:
            if self.current_page <= (self.page_num + 1) / 2:
                start_index = 1
                end_index = self.page_num + 1
            else:
                start_index = self.current_page - (self.page_num - 1) / 2
                end_index = self.current_page + (self.page_num + 1) / 2
                if self.current_page + (self.page_num - 1) / 2 > self.total_count:
                    end_index = self.total_count + 1
                    start_index = self.total_count - self.page_num + 1
        # 上一页
        if self.current_page == 1:
            prev = '<a class="page" href="javascript:void(0);">上一页</a>'
        else:
            prev = '<a class="page" href="%s?page=%s">上一页</a>' % (base_url, self.current_page - 1)
        page_list.append(prev)

        for page in range(int(start_index), int(end_index)):
            if page == self.current_page:
                temp = '<a class="page active" href="%s?page=%s">%s</a>' % (base_url, page, page)
            else:
                temp = '<a class="page" href="%s?page=%s">%s</a>' % (base_url, page, page)
            page_list.append(temp)

        # 下一页
        if self.current_page == self.total_count:
            nex = '<a class="page" href="javascript:void(0);">下一页</a>'
        else:
            nex = '<a class="page" href="%s?page=%s">下一页</a>' % (base_url, self.current_page + 1)
        page_list.append(nex)

        # 跳转
        jump = """
                <input type="text" /><a onclick='jumpTo(this, "%s?page=");'>跳转</a>
                <script>
                    function jumpTo(ths, base){
                        var val = ths.previousSibling.value;
                        location.href = base + val;
                    }
                </script>
            """ % (base_url,)
        page_list.append(jump)
        page_str = mark_safe("".join(page_list))
        return page_str
