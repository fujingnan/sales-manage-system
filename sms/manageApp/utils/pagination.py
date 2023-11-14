import math
from manageApp import models
from django.utils.safestring import mark_safe
import copy


class Pagination(object):
    def __init__(self,
                 request,
                 page_url_params='page',
                 query=None,
                 page_per_size=10,
                 page_inc=5):
        """

        :param request: 请求对象
        :param page_url_params: 分页在url中的参数
        :param query: 传入的获取数据库的数据对象
        :param page_per_size: 每页展示的条数
        :param page_inc: 分页栏基于当前页前后拓展的页码
        """
        self.request = request
        self.page_per_size = page_per_size
        self.query = query
        self.page_url_params = page_url_params
        self.page_inc = page_inc
        self.page_dict = copy.deepcopy(self.request.GET)


    def pagination(self):
        """
        finall_query, 最后分页每一页展示结果
        page_list_show, 分页栏展示
        page, 当前页码
        page_total_size，总页数
        :return:
        """
        page = self.request.GET.get(self.page_url_params)
        page = int(page) if page else 1
        items_nums = self.query.count()
        page_total_size = max(1, math.ceil(items_nums / self.page_per_size))
        page = min(page, page_total_size)
        if page - self.page_inc <= 0:
            start = 1
            end = min(page_total_size, self.page_per_size)
        else:
            if page + self.page_inc > page_total_size:
                start = page - self.page_inc
                end = min(page_total_size, page + self.page_inc)
            else:
                start = page - self.page_inc
                end = page + self.page_inc
        self.page_dict.setlist(self.page_url_params, [1])
        page_list_str = '<li><a href="?{}">首页</a></li>'.format(self.page_dict.urlencode())
        self.page_dict.setlist(self.page_url_params, [max(page - 1, 1)])
        page_list_str += '<li><a href="?{}">上一页</a></li>'.format(self.page_dict.urlencode())
        for i in range(start, end + 1):
            self.page_dict.setlist(self.page_url_params, [i])
            if i == page:
                page_list_str += '<li class="active"><a href="?{}">{}</a></li>'.format(self.page_dict.urlencode(), i)
                continue
            page_list_str += '<li><a href="?{}">{}</a></li>'.format(self.page_dict.urlencode(), i)

        self.page_dict.setlist(self.page_url_params, [min(page + 1, page_total_size)])
        page_list_str += '<li><a href="?{}">下一页 </a></li>'.format(self.page_dict.urlencode())
        self.page_dict.setlist(self.page_url_params, [page_total_size])
        page_list_str += '<li><a href="?{}">尾页</a></li>'.format(self.page_dict.urlencode())
        page_list_show = mark_safe(page_list_str)
        start_show = int(page - 1) * self.page_per_size
        end_show = start_show + self.page_per_size
        if not page_total_size:
            return (self.query, page_list_show, page, page_total_size)
        finall_query = self.query[start_show: end_show]
        return (finall_query, page_list_show, page, page_total_size)