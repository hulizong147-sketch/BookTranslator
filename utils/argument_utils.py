import argparse


class ArgumentUtils:
    """
    命令行参数解析对象
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="书籍翻译")
        self.parser.add_argument('--config', type=str, default="config.yaml", help='项目的整体配置文件')
        self.parser.add_argument('--model_type', type=str, default='DeepSeeKModel',
                                 choices=['DeepSeeKModel', 'OpenAIModel'], help='选择DeepSeeK还是OpenAI的模型')
        self.parser.add_argument('--model_name', type=str, help='大语言模型的名字')
        self.parser.add_argument('--input_file', type=str, help='需要翻译的书籍所属的文件路径')
        self.parser.add_argument('--file_format', type=str, help='翻译之后生成的文件格式')
        self.parser.add_argument('--source_language', type=str, help='书籍的原始语言')
        self.parser.add_argument('--target_language', type=str, help='翻译之后的语言')

    def parse_arg(self):
        """
        解析和验证命令中的参数
        :return:
        """
        args = self.parser.parse_args()
        return args


if __name__ == '__main__':
    arg = ArgumentUtils()
    print(arg.parse_arg())
