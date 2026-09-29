import pdfplumber

from book.book import Book
from book.content import Content, ContentType, TableContent
from book.page import Page
from utils.exception import PageOutRangeException
from utils.log_utils import log


def parse_pdf(file_path, pages=None):
    """
    解析pdf文件的函数  返回解析之后的文本对象
    :param file_path:
    :param pages:
    :return:
    """
    book = Book(file_path)

    with pdfplumber.open(file_path) as pdf:

        if pages and pages > len(pdf.pages):
            raise PageOutRangeException(len(pdf.pages), pages)

        if pages is None:
            pages_arr = pdf.pages
        else:
            pages_arr = pdf.pages[:pages]

        for pdf_page in pages_arr:
            page = Page()

            raw_text = pdf_page.extract_text()
            tables = pdf_page.extract_tables()

            # 在raw_text删掉表格的内容
            for table in tables:
                for row in table:
                    for cell in row:
                        raw_text = raw_text.replace(cell, "", 1)

            if raw_text:
                lines = raw_text.splitlines()
                clear_lines = [line.strip() for line in lines if line.strip()]
                clear_text = "\n".join(clear_lines)

                text_content = Content(content_type=ContentType.TEXT, original=clear_text)
                page.add_content(text_content)
                log.debug(f"pdf文件解析之后的内容 {clear_text}")


            if tables:
                for table in tables:
                    table_content = TableContent(content_type=ContentType.TABLE, original=table)
                    page.add_content(table_content)
                    log.debug(f"pdf文件解析之后表格的内容 {table}")
            book.add_page(page)
    return book


if __name__ == '__main__':
    book = parse_pdf("../test/test.pdf")

