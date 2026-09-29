from translator.file_writer import FileWriter
from translator.pdf_parser import parse_pdf
from translator.translator_chain import TranslationChain
from utils.log_utils import log


class PDFTransltor:
    """
    翻译一本PDF文件
    """

    def __init__(self, model):
        self.book = None
        self.chain = TranslationChain(model)
        self.writer = FileWriter(self.book)

    def book_translator(self, file_path, source_language, target_language, out_file_format="pdf", out_file_path=None, pages=None):
        """
        翻译一本书
        :param file_path:
        :param source_language:
        :param target_language:
        :param out_file_format: 输出文件格式
        :param out_file_path: 输出文件路径
        :param pages: 翻译的页数
        :return:
        """
        self.book = parse_pdf(file_path, pages)
        self.writer.book = self.book
        for page_index, page in enumerate(self.book.pages):
            for content_index, content in enumerate(page.content):
                translator_text, status = self.chain.run(content, source_language, target_language)

                log.debug(f"翻译之后的内容是 {translator_text}")
                self.book.pages[page_index].content[content_index].set_translation(translator_text, status)

        self.writer.save_book(out_file_path, out_file_format)

