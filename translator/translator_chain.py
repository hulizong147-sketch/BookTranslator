from ai_model.model import Model
from book.content import ContentType
from utils.log_utils import log


class TranslationChain:
    """
    负责调用langchain来完成文本的翻译
    """

    def __init__(self, model):
        self.langchain = model.make_prompt() | model.create_llm()

    def run(self, content, source_language, target_language):
        """
        翻译具体的文本
        :param content:
        :param source_language:
        :param target_language:
        :return:
        """
        text = ''
        result = ''

        if content.content_type == ContentType.TEXT:
            text = f'请按照要求翻译以下内容{content.original}'
        elif content.content_type == ContentType.TABLE:
            text = f'请按照要求翻译以下内容，严格以JSON 二维数据格式返回(例如 [["行1列1", "行1列2"], ["行2列1", "行2列2"]]), 不要包含markdown代码标记块或者其他文本 {content.get_original_to_string()}'
        result = self.langchain.invoke({
            'source_language': source_language,
            'target_language': target_language,
            'text': text
        })
        log.info(result.content)

        return result.content, True
