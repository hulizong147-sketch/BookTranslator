

class PageOutRangeException(Exception):
    def __init__(self, book_total, trans_pages):
        self.book_total = book_total
        self.trans_pages = trans_pages
        super(PageOutRangeException, self).__init__("页数超过了PDF最大页数")