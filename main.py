from translator.book_translator import PDFTransltor
from utils.project_config import ProjectConfig
from ai_model.deepseek_model import DeepSeeKModel
from ai_model.openai_model import OpenAIModel


if __name__ == '__main__':
    # 项目整体配置的初始化
    config = ProjectConfig()
    config.initialize()

    if config.model_type == "DeepSeeKModel":
        model = DeepSeeKModel(config.model_name, config.api_key)
    else:
        model = OpenAIModel(config.model_name, config.api_key)

    # 初始化一个翻译器
    transaltor = PDFTransltor(model)
    transaltor.book_translator(file_path=config.input_file, source_language=config.source_language, target_language=config.target_language, out_file_path='test', out_file_format=config.file_format)

