
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table, PageBreak

from book.content import ContentType
from utils.log_utils import log
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import pagesizes, colors


class FileWriter:
    def __init__(self, book):
        self.book = book

    def save_book(self, out_file_path=None, file_format="PDF"):
        """
        负责把翻译之后的数据写入文件
        :param out_file_path:
        :param file_format: md pdf
        :return:
        """
        if file_format.lower() == 'pdf':
            return self.save_book_pdf(out_file_path)
        elif file_format.lower() == 'md':
            return self.save_book_md(out_file_path)
        else:
            log.warning("当前的文件格式不支持 仅支持pdf和md格式")
            return ''

    def save_book_pdf(self, out_file_path):
        """
        把数据写入到pdf文件中
        :param out_file_path: 
        :return: 
        """""
        if out_file_path is not None:

            # test.pdf ->  test_translator.pdf
            subfix = self.book.file_path[self.book.file_path.rindex("."):]
            out_file_path = self.book.file_path.replace(subfix, "_translator.pdf")

            log.debug(f"pdf原文件路径是 {self.book.file_path} 翻译之后的路径是 {out_file_path}")

            pdfmetrics.registerFont(TTFont('SimSun', "../fonts/simsun.ttc"))
            style = ParagraphStyle('SimSun', fontName='SimSun', fontSize=12)
            doc = SimpleDocTemplate(out_file_path, pagesize=pagesizes.letter)
            pdf_data = []

            for page in self.book.pages:
                for content in page.content:
                    if content.status:
                        if content.content_type == ContentType.TEXT:
                            paragraph = Paragraph(text=content.translation, style=style)
                            pdf_data.append(paragraph)
                        elif content.content_type == ContentType.TABLE:
                            # reportlab 表格坐标约定为 (列, 行)，-1 表示最后一行/列
                            table_style = TableStyle(
                                [
                                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('FONTNAME', (0, 0), (-1, 0), 'SimSun'),
                                    ('FONTSIZE', (0, 0), (-1, 0), 14),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                    ('FONTNAME', (0, 1), (-1, -1), 'SimSun'),
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                                ]
                            )
                            table = Table(data=content.translation.values.tolist())
                            table.setStyle(table_style)
                            pdf_data.append(table)

                if page != self.book.pages[-1]:
                    pdf_data.append(PageBreak())

            doc.build(pdf_data)
            log.info("pdf文件写入完成")
            return out_file_path

    def save_book_md(self, out_file_path):
        """
        把数据写入到md文件中
        :param out_file_path:
        :return:
        """

        if out_file_path is not None:
            subfix = self.book.file_path[self.book.file_path.rindex("."):]
            out_file_path = self.book.file_path.replace(subfix, "_translator.md")
            log.debug(f"pdf原文件路径是 {self.book.file_path} 翻译之后的路径是 {out_file_path}")

            with open(out_file_path, 'w', encoding="utf-8") as md_file:
                for page in self.book.pages:
                    for content in page.content:
                        if content.status:
                            if content.content_type == ContentType.TEXT:
                                md_file.write(content.translation + "\n")
                            elif content.content_type == ContentType.TABLE:
                                df = content.translation
                                rows = df.values.tolist()
                                header_row = rows[0]
                                body_row = rows[1:]

                                header = '| ' + " | ".join(cell for cell in header_row) + ' | ' + "\n"
                                tr = '| ' + " | ".join(['----']*len(header_row)) + ' | ' + "\n"
                                t_body = ''
                                for row in body_row:
                                    r = [" | ".join(row)]
                                    t_body += '| ' + " | ".join(r) + ' | ' + '\n'
                                md_file.write(header + tr + t_body)

                    if page != self.book.pages[-1]:
                        md_file.write("\n---\n\n")

            log.info("md文件写入完成")
            return out_file_path
